#!/usr/bin/env python
# coding: utf-8
"""No-motion ROS1 probe for a manually audited proxy stem axis.

Publishes only geometry evidence:
  /proxy_stem/origin  geometry_msgs/PointStamped
  /proxy_stem/axis    geometry_msgs/Vector3Stamped

It never imports or publishes chassis, arm, gripper, navigation or grasp
commands.  The output remains proxy-domain evidence even when all gates pass.
"""

from __future__ import division, print_function

import argparse
import json
import math
import os
import sys
import time

import numpy as np

import rospy
from geometry_msgs.msg import PointStamped, Vector3Stamped
from sensor_msgs.msg import CameraInfo, PointCloud2


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from stem_axis_geometry import (  # noqa: E402
    fit_oriented_axis,
    localize_keypoint_cluster,
    quality_gate,
    summarize_axis_frames,
)


def parse_keypoints(text):
    points = []
    for item in text.split(";"):
        fields = item.split(",")
        if len(fields) != 2:
            raise ValueError("keypoints must be u,v;u,v;...")
        points.append((float(fields[0]), float(fields[1])))
    if len(points) < 2:
        raise ValueError("at least two ordered keypoints are required")
    return points


def point_cloud_xyz(cloud):
    offsets = dict((field.name, field.offset) for field in cloud.fields)
    for name in ("x", "y", "z"):
        if name not in offsets:
            raise ValueError("PointCloud2 missing field %s" % name)
    byte_order = ">" if cloud.is_bigendian else "<"
    dtype = np.dtype(
        {
            "names": ("x", "y", "z"),
            "formats": (byte_order + "f4", byte_order + "f4", byte_order + "f4"),
            "offsets": (offsets["x"], offsets["y"], offsets["z"]),
            "itemsize": cloud.point_step,
        }
    )
    structured = np.ndarray(
        shape=(int(cloud.height), int(cloud.width)),
        dtype=dtype,
        buffer=cloud.data,
        strides=(int(cloud.row_step), int(cloud.point_step)),
    )
    return np.column_stack(
        (
            structured["x"].reshape(-1),
            structured["y"].reshape(-1),
            structured["z"].reshape(-1),
        )
    )


def vector_list(value):
    return [float(item) for item in np.asarray(value).reshape((-1,))]


def publish_geometry(origin_pub, axis_pub, cloud_header, origin, axis):
    origin_msg = PointStamped()
    origin_msg.header = cloud_header
    origin_msg.point.x, origin_msg.point.y, origin_msg.point.z = vector_list(origin)
    origin_pub.publish(origin_msg)

    axis_msg = Vector3Stamped()
    axis_msg.header = cloud_header
    axis_msg.vector.x, axis_msg.vector.y, axis_msg.vector.z = vector_list(axis)
    axis_pub.publish(axis_msg)


def run(args):
    audited_uv = parse_keypoints(args.keypoints)
    rospy.init_node("proxy_stem_axis_probe", anonymous=True)
    origin_pub = rospy.Publisher("/proxy_stem/origin", PointStamped, queue_size=1)
    axis_pub = rospy.Publisher("/proxy_stem/axis", Vector3Stamped, queue_size=1)

    camera_info = rospy.wait_for_message(
        args.camera_info_topic, CameraInfo, timeout=args.wait_timeout
    )
    intrinsics = np.asarray(camera_info.K, dtype=np.float64).reshape((3, 3))
    frames = []
    accepted_axes = []
    accepted_origins = []

    for frame_index in range(args.frames):
        frame = {"index": frame_index, "accepted": False, "reject": None}
        try:
            cloud = rospy.wait_for_message(
                args.point_cloud_topic, PointCloud2, timeout=args.wait_timeout
            )
            if cloud.header.frame_id != args.expected_frame:
                raise ValueError(
                    "point cloud frame %s != %s"
                    % (cloud.header.frame_id, args.expected_frame)
                )
            xyz = point_cloud_xyz(cloud)
            localized = []
            supports = []
            for uv in audited_uv:
                result = localize_keypoint_cluster(
                    xyz,
                    intrinsics,
                    uv,
                    radius_px=args.radius_px,
                    min_depth=args.min_depth,
                    max_depth=args.max_depth,
                    depth_bin_size=args.depth_bin_size,
                    min_points=args.min_points,
                    min_cluster_fraction=args.min_cluster_fraction,
                )
                if result is None:
                    raise ValueError("no supported depth cluster at uv=%s" % (uv,))
                localized.append(result["point"])
                supports.append(result["support"])

            fit = fit_oriented_axis(
                np.asarray(localized),
                order=np.arange(len(localized), dtype=np.float64),
                residual_threshold_m=args.residual_threshold_m,
            )
            gate = quality_gate(
                fit,
                min_inliers=args.min_axis_inliers,
                min_inlier_ratio=args.min_inlier_ratio,
                min_span_m=args.min_span_m,
                max_residual_p95_m=args.max_residual_p95_m,
            )
            frame.update(
                {
                    "stamp": cloud.header.stamp.to_sec(),
                    "frame_id": cloud.header.frame_id,
                    "keypoints_xyz": [vector_list(point) for point in localized],
                    "supports": supports,
                    "axis": vector_list(fit["axis"]),
                    "origin": vector_list(fit["origin"]),
                    "span_m": float(fit["span_m"]),
                    "residual_p95_m": float(fit["residual_p95_m"]),
                    "inlier_count": int(fit["inlier_count"]),
                    "inlier_ratio": float(fit["inlier_ratio"]),
                    "accepted": bool(gate["passed"]),
                    "reject": gate["reasons"],
                }
            )
            if gate["passed"]:
                accepted_axes.append(fit["axis"])
                accepted_origins.append(fit["origin"])
                publish_geometry(origin_pub, axis_pub, cloud.header, fit["origin"], fit["axis"])
        except Exception as error:
            frame["reject"] = str(error)
        frames.append(frame)
        rospy.sleep(args.sample_interval)

    summary = {
        "schema": "abot-proxy-stem-axis-v1",
        "proxy_domain": True,
        "plant_identity": "unverified_campus_plant",
        "axis_contract": "positive_audited_base_to_tip_KP1_to_KP4",
        "motion_authorized": False,
        "keypoints_uv": [list(point) for point in audited_uv],
        "attempted_frames": args.frames,
        "accepted_frames": len(accepted_axes),
        "geometry_passed": False,
        "decision": "REJECT_NO_VALID_AXIS",
        "frames": frames,
    }
    if accepted_axes:
        aggregate = summarize_axis_frames(accepted_axes, attempted_frames=args.frames)
        origin_array = np.asarray(accepted_origins)
        distances = np.linalg.norm(origin_array, axis=1)
        aggregate_serializable = {
            "axis": vector_list(aggregate["axis"]),
            "valid_frames": int(aggregate["valid_frames"]),
            "valid_rate": float(aggregate["valid_rate"]),
            "angular_median_deg": float(aggregate["angular_median_deg"]),
            "angular_p95_deg": float(aggregate["angular_p95_deg"]),
            "origin_median": vector_list(np.median(origin_array, axis=0)),
            "distance_median_m": float(np.median(distances)),
            "distance_min_m": float(np.min(distances)),
        }
        summary["aggregate"] = aggregate_serializable
        stability_pass = (
            aggregate["valid_rate"] >= args.min_valid_rate
            and aggregate["angular_p95_deg"] <= args.max_angular_p95_deg
        )
        summary["geometry_passed"] = bool(stability_pass)
        if not stability_pass:
            summary["decision"] = "REJECT_AXIS_UNSTABLE_OR_SPARSE"
        elif aggregate_serializable["distance_min_m"] > args.max_reach_m:
            summary["decision"] = "REJECT_OUT_OF_REACH"
        else:
            summary["decision"] = "PROXY_AXIS_PASS_MOTION_STILL_FORBIDDEN"

    payload = json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True)
    print(payload)
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write(payload)
            output_file.write("\n")
    return 0 if summary["geometry_passed"] else 2


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keypoints", required=True)
    parser.add_argument("--frames", type=int, default=30)
    parser.add_argument("--point-cloud-topic", default="/camera/depth_registered/points")
    parser.add_argument("--camera-info-topic", default="/camera/rgb/camera_info")
    parser.add_argument("--expected-frame", default="camera_rgb_optical_frame")
    parser.add_argument("--radius-px", type=float, default=16.0)
    parser.add_argument("--min-depth", type=float, default=0.15)
    parser.add_argument("--max-depth", type=float, default=3.0)
    parser.add_argument("--depth-bin-size", type=float, default=0.02)
    parser.add_argument("--min-points", type=int, default=6)
    parser.add_argument("--min-cluster-fraction", type=float, default=0.10)
    parser.add_argument("--residual-threshold-m", type=float, default=0.02)
    parser.add_argument("--min-axis-inliers", type=int, default=3)
    parser.add_argument("--min-inlier-ratio", type=float, default=0.70)
    parser.add_argument("--min-span-m", type=float, default=0.03)
    parser.add_argument("--max-residual-p95-m", type=float, default=0.015)
    parser.add_argument("--min-valid-rate", type=float, default=0.70)
    parser.add_argument("--max-angular-p95-deg", type=float, default=15.0)
    parser.add_argument("--max-reach-m", type=float, default=0.55)
    parser.add_argument("--sample-interval", type=float, default=0.15)
    parser.add_argument("--wait-timeout", type=float, default=5.0)
    parser.add_argument("--output")
    return parser


if __name__ == "__main__":
    sys.exit(run(build_parser().parse_args()))
