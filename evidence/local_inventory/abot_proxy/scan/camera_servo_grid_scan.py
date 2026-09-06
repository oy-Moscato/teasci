#!/usr/bin/env python
# coding: utf-8
"""Camera-only servo grid scan for locating the ABOT white gripper.

The scanner publishes only ``riki_msgs/Servo``.  It refuses to run when a
publisher is connected to either the normal or safety-remapped velocity topic.
"""

from __future__ import division, print_function

import argparse
import json
import os
import threading
import time

import cv2
import numpy as np


def serpentine_grid(horizontal, pitch):
    result = []
    horizontal = [int(value) for value in horizontal]
    for row, pitch_value in enumerate([int(value) for value in pitch]):
        row_values = horizontal if row % 2 == 0 else list(reversed(horizontal))
        result.extend((yaw, pitch_value) for yaw in row_values)
    return result


def white_gripper_score(image_bgr):
    image = np.asarray(image_bgr, dtype=np.uint8)
    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("expected BGR image")
    height, width = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (0, 0, 180), (179, 70, 255))
    kernel = np.ones((3, 3), dtype=np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    count, labels, stats, _ = cv2.connectedComponentsWithStats(mask, 8)
    best = None
    image_area = float(height * width)
    for label in range(1, count):
        x, y, w, h, area = [int(value) for value in stats[label]]
        if x <= 0 or y <= 0 or x + w >= width or y + h >= height:
            continue
        area_ratio = area / image_area
        if area_ratio < 0.0005 or area_ratio > 0.15:
            continue
        fill = area / float(max(w * h, 1))
        center_x = x + 0.5 * w
        center_y = y + 0.5 * h
        dx = abs(center_x - 0.5 * width) / (0.5 * width)
        centrality = max(0.0, 1.0 - dx)
        lower_weight = 0.35 + 0.65 * (center_y / float(height))
        compactness = min(w, h) / float(max(w, h))
        score = area_ratio * fill * (0.5 + 0.5 * compactness)
        score *= (0.35 + 0.65 * centrality) * lower_weight
        candidate = {
            "score": float(score),
            "bbox": [x, y, w, h],
            "area_px": area,
            "area_ratio": float(area_ratio),
            "fill_ratio": float(fill),
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate
    if best is None:
        return {"score": 0.0, "bbox": None, "area_px": 0, "area_ratio": 0.0, "fill_ratio": 0.0}
    return best


def _parse_csv(value):
    return [int(item.strip()) for item in value.split(",") if item.strip()]


def _assert_no_velocity_publishers(rospy):
    import rosgraph

    master = rosgraph.Master(rospy.get_name())
    publishers, _, _ = master.getSystemState()
    by_topic = dict(publishers)
    offenders = {}
    for topic in ("/cmd_vel", "/safety_disabled/cmd_vel"):
        if by_topic.get(topic):
            offenders[topic] = by_topic[topic]
    if offenders:
        raise RuntimeError("velocity publishers present: %s" % offenders)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizontal", default="30,60,90,120,150")
    parser.add_argument("--pitch", default="15,30,45,60,75,90")
    parser.add_argument("--settle", type=float, default=1.2)
    parser.add_argument("--restore", default="90,30")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--image-topic", default="/camera/rgb/image_raw")
    args = parser.parse_args()

    import rospy
    from cv_bridge import CvBridge
    from riki_msgs.msg import Servo
    from sensor_msgs.msg import Image

    rospy.init_node("camera_servo_grid_scan", anonymous=True)
    _assert_no_velocity_publishers(rospy)
    if not os.path.isdir(args.output_dir):
        os.makedirs(args.output_dir)

    bridge = CvBridge()
    lock = threading.Lock()
    latest = {"stamp": None, "image": None}

    def callback(message):
        image = bridge.imgmsg_to_cv2(message, "bgr8")
        with lock:
            latest["stamp"] = message.header.stamp.to_sec()
            latest["image"] = image.copy()

    rospy.Subscriber(args.image_topic, Image, callback, queue_size=1)
    publisher = rospy.Publisher("/servo", Servo, queue_size=1)
    deadline = time.time() + 8.0
    while latest["image"] is None and time.time() < deadline and not rospy.is_shutdown():
        rospy.sleep(0.05)
    if latest["image"] is None:
        raise RuntimeError("no RGB image received")

    records = []
    restore = _parse_csv(args.restore)
    if len(restore) != 2:
        raise ValueError("restore must be yaw,pitch")
    try:
        for index, (yaw, pitch) in enumerate(
            serpentine_grid(_parse_csv(args.horizontal), _parse_csv(args.pitch))
        ):
            _assert_no_velocity_publishers(rospy)
            before = latest["stamp"]
            publisher.publish(Servo(Servo1=yaw, Servo2=pitch))
            rospy.sleep(max(args.settle, 0.2))
            deadline = time.time() + 3.0
            while latest["stamp"] == before and time.time() < deadline:
                rospy.sleep(0.02)
            with lock:
                stamp = latest["stamp"]
                image = latest["image"].copy()
            result = white_gripper_score(image)
            filename = "scan_%02d_yaw_%03d_pitch_%03d.jpg" % (index, yaw, pitch)
            raw_filename = "raw_%02d_yaw_%03d_pitch_%03d.jpg" % (index, yaw, pitch)
            cv2.imwrite(os.path.join(args.output_dir, raw_filename), image)
            annotated = image.copy()
            if result["bbox"] is not None:
                x, y, w, h = result["bbox"]
                cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(
                annotated,
                "yaw=%d pitch=%d score=%.6f" % (yaw, pitch, result["score"]),
                (10, 24),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (0, 0, 255),
                2,
            )
            cv2.imwrite(os.path.join(args.output_dir, filename), annotated)
            record = dict(result)
            record.update(
                {
                    "index": index,
                    "yaw": yaw,
                    "pitch": pitch,
                    "stamp": stamp,
                    "file": filename,
                    "raw_file": raw_filename,
                }
            )
            records.append(record)
            print(json.dumps(record, sort_keys=True))
    finally:
        publisher.publish(Servo(Servo1=restore[0], Servo2=restore[1]))
        rospy.sleep(1.0)

    records.sort(key=lambda item: item["score"], reverse=True)
    manifest = {
        "image_topic": args.image_topic,
        "restore": restore,
        "count": len(records),
        "ranked": records,
    }
    with open(os.path.join(args.output_dir, "manifest.json"), "w") as output:
        json.dump(manifest, output, indent=2, sort_keys=True)
        output.write("\n")


if __name__ == "__main__":
    main()
