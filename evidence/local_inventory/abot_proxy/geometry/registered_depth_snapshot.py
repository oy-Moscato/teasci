#!/usr/bin/env python
# coding: utf-8
"""Save one organized registered PointCloud2 frame as depth and XYZ arrays."""

from __future__ import print_function

import argparse
import json
import os
import sys
import threading

import cv2
import numpy as np
import rospy
from sensor_msgs.msg import PointCloud2


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from stem_axis_geometry import is_fresh_stamp, valid_depth_mask  # noqa: E402
from stem_axis_live_probe import point_cloud_xyz  # noqa: E402


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default="/camera/depth_registered/points")
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--max-age", type=float, default=2.0)
    parser.add_argument("--min-valid-ratio", type=float, default=0.001)
    args = parser.parse_args()

    rospy.init_node("registered_depth_snapshot", anonymous=True)
    deadline = rospy.Time.now().to_sec() + args.timeout
    condition = threading.Condition()
    latest = {"seq": 0, "cloud": None}

    def callback(message):
        with condition:
            latest["seq"] += 1
            latest["cloud"] = message
            condition.notify_all()

    subscriber = rospy.Subscriber(args.topic, PointCloud2, callback, queue_size=1)
    cloud = None
    xyz = None
    valid = None
    stale_count = 0
    invalid_count = 0
    consumed_seq = 0
    while rospy.Time.now().to_sec() < deadline:
        with condition:
            remaining = max(0.1, deadline - rospy.Time.now().to_sec())
            condition.wait(remaining)
            if latest["seq"] == consumed_seq or latest["cloud"] is None:
                continue
            consumed_seq = latest["seq"]
            candidate = latest["cloud"]
        now_s = rospy.Time.now().to_sec()
        if not is_fresh_stamp(candidate.header.stamp.to_sec(), now_s, args.max_age):
            stale_count += 1
            continue
        candidate_xyz = point_cloud_xyz(candidate).reshape((int(candidate.height), int(candidate.width), 3))
        candidate_valid = valid_depth_mask(candidate_xyz[:, :, 2])
        if float(candidate_valid.mean()) < args.min_valid_ratio:
            invalid_count += 1
            continue
        cloud = candidate
        xyz = candidate_xyz
        valid = candidate_valid
        break
    subscriber.unregister()
    if cloud is None:
        raise RuntimeError("no fresh point cloud received")
    depth = xyz[:, :, 2]
    np.save(args.prefix + "_xyz.npy", xyz)
    np.save(args.prefix + "_depth.npy", depth)

    color_input = np.zeros(depth.shape, dtype=np.uint8)
    color_input[valid] = np.clip((depth[valid] - 0.15) / 2.85 * 255.0, 0, 255).astype(np.uint8)
    color_map = getattr(cv2, "COLORMAP_TURBO", cv2.COLORMAP_JET)
    color = cv2.applyColorMap(255 - color_input, color_map)
    color[~valid] = (64, 64, 64)
    cv2.imwrite(args.prefix + "_depth_color.png", color)

    metadata = {
        "width": int(cloud.width),
        "height": int(cloud.height),
        "frame_id": cloud.header.frame_id,
        "stamp": cloud.header.stamp.to_sec(),
        "valid_ratio": float(valid.mean()),
        "valid_count": int(valid.sum()),
        "stale_frames_discarded": int(stale_count),
        "invalid_frames_discarded": int(invalid_count),
    }
    with open(args.prefix + "_metadata.json", "w") as output:
        json.dump(metadata, output, indent=2, sort_keys=True)
        output.write("\n")
    print(json.dumps(metadata, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
