"""Pure-numpy geometry for the ABOT field stem-axis proxy experiment.

The proxy keeps the project contract: the positive axis points from the
audited stem base (KP1 side) toward the audited tip (KP4 side).  This module
does not classify a plant and does not authorize robot motion.
"""

from __future__ import division

import itertools
import math

import numpy as np


def is_fresh_stamp(stamp_s, now_s, max_age_s=2.0):
    """Return true only for non-future data inside the configured age gate."""
    age = float(now_s) - float(stamp_s)
    return 0.0 <= age <= float(max_age_s)


def valid_depth_mask(depth, min_depth=0.15, max_depth=3.0):
    array = np.asarray(depth, dtype=np.float64)
    finite = np.isfinite(array)
    valid = np.zeros(array.shape, dtype=np.bool_)
    valid[finite] = (array[finite] >= float(min_depth)) & (array[finite] <= float(max_depth))
    return valid


def _camera_matrix(intrinsics):
    matrix = np.asarray(intrinsics, dtype=np.float64).reshape((3, 3))
    fx, fy = float(matrix[0, 0]), float(matrix[1, 1])
    if not np.isfinite(matrix).all() or fx <= 0.0 or fy <= 0.0:
        raise ValueError("invalid camera intrinsics")
    return matrix


def project_points(points_xyz, intrinsics, min_depth=0.15, max_depth=3.0):
    """Project finite camera-frame XYZ points and retain source indices."""
    points = np.asarray(points_xyz, dtype=np.float64).reshape((-1, 3))
    matrix = _camera_matrix(intrinsics)
    finite = np.isfinite(points).all(axis=1)
    depth_ok = np.zeros(points.shape[0], dtype=np.bool_)
    depth_ok[finite] = (
        (points[finite, 2] >= float(min_depth))
        & (points[finite, 2] <= float(max_depth))
    )
    finite &= depth_ok
    indices = np.flatnonzero(finite)
    selected = points[indices]
    if selected.size == 0:
        return np.empty((0, 2)), indices
    u = matrix[0, 0] * selected[:, 0] / selected[:, 2] + matrix[0, 2]
    v = matrix[1, 1] * selected[:, 1] / selected[:, 2] + matrix[1, 2]
    return np.column_stack((u, v)), indices


def localize_keypoint_cluster(
    points_xyz,
    intrinsics,
    keypoint_uv,
    radius_px=14.0,
    min_depth=0.15,
    max_depth=3.0,
    depth_bin_size=0.02,
    min_points=8,
    min_cluster_fraction=0.10,
):
    """Localize one audited 2D keypoint using its nearest supported depth bin."""
    if radius_px <= 0.0 or depth_bin_size <= 0.0 or min_points <= 0:
        raise ValueError("radius, bin size and min_points must be positive")
    points = np.asarray(points_xyz, dtype=np.float64).reshape((-1, 3))
    uv, indices = project_points(points, intrinsics, min_depth, max_depth)
    if uv.size == 0:
        return None
    target = np.asarray(keypoint_uv, dtype=np.float64).reshape((2,))
    dist2 = np.sum((uv - target) ** 2, axis=1)
    local_indices = indices[dist2 <= float(radius_px) ** 2]
    local = points[local_indices]
    if local.shape[0] < min_points:
        return None

    bins = np.floor(local[:, 2] / float(depth_bin_size)).astype(np.int64)
    support_needed = max(
        int(min_points),
        int(math.ceil(local.shape[0] * float(min_cluster_fraction))),
    )
    chosen = None
    for bin_id in sorted(np.unique(bins)):
        cluster = local[bins == bin_id]
        if cluster.shape[0] >= support_needed:
            chosen = cluster
            break
    if chosen is None:
        return None
    return {
        "point": np.median(chosen, axis=0),
        "support": int(chosen.shape[0]),
        "candidate_count": int(local.shape[0]),
        "depth_median_m": float(np.median(chosen[:, 2])),
    }


def _line_residuals(points, origin, axis):
    delta = points - origin
    along = np.outer(np.dot(delta, axis), axis)
    return np.linalg.norm(delta - along, axis=1)


def fit_oriented_axis(points_xyz, order=None, residual_threshold_m=0.015):
    """Robustly fit and orient a 3D line through ordered stem keypoints."""
    points = np.asarray(points_xyz, dtype=np.float64).reshape((-1, 3))
    finite = np.isfinite(points).all(axis=1)
    points = points[finite]
    if points.shape[0] < 2:
        raise ValueError("at least two finite keypoints are required")
    if residual_threshold_m <= 0.0:
        raise ValueError("residual_threshold_m must be positive")

    if order is None:
        ordered = np.arange(finite.shape[0], dtype=np.float64)[finite]
    else:
        raw_order = np.asarray(order, dtype=np.float64).reshape((-1,))
        if raw_order.shape[0] != finite.shape[0]:
            raise ValueError("order length must match input points")
        ordered = raw_order[finite]

    best_mask = None
    best_score = None
    for first, second in itertools.combinations(range(points.shape[0]), 2):
        delta = points[second] - points[first]
        norm = np.linalg.norm(delta)
        if norm < 1e-6:
            continue
        axis = delta / norm
        residuals = _line_residuals(points, points[first], axis)
        mask = residuals <= float(residual_threshold_m)
        count = int(mask.sum())
        median = float(np.median(residuals[mask])) if count else float("inf")
        score = (count, -median)
        if best_score is None or score > best_score:
            best_score = score
            best_mask = mask
    if best_mask is None or int(best_mask.sum()) < 2:
        raise ValueError("no non-degenerate axis fit")

    inliers = points[best_mask]
    origin = np.mean(inliers, axis=0)
    _, _, vh = np.linalg.svd(inliers - origin, full_matrices=False)
    axis = vh[0]

    ordered_inliers = ordered[best_mask]
    finite_order = np.isfinite(ordered_inliers)
    if int(finite_order.sum()) >= 2:
        scores = np.dot(inliers[finite_order] - origin, axis)
        order_values = ordered_inliers[finite_order]
        covariance = np.sum(
            (scores - np.mean(scores)) * (order_values - np.mean(order_values))
        )
        if covariance < 0.0:
            axis = -axis
    elif np.dot(points[-1] - points[0], axis) < 0.0:
        axis = -axis

    residuals = _line_residuals(points, origin, axis)
    final_mask = residuals <= float(residual_threshold_m)
    final_inliers = points[final_mask]
    projections = np.dot(final_inliers - origin, axis)
    span = float(np.percentile(projections, 95) - np.percentile(projections, 5))
    return {
        "origin": origin,
        "axis": axis / np.linalg.norm(axis),
        "inlier_count": int(final_mask.sum()),
        "inlier_ratio": float(final_mask.mean()),
        "span_m": span,
        "residual_p95_m": float(np.percentile(residuals[final_mask], 95)),
        "residuals_m": residuals,
        "inlier_mask": final_mask,
    }


def quality_gate(
    result,
    min_inliers=3,
    min_inlier_ratio=0.70,
    min_span_m=0.03,
    max_residual_p95_m=0.015,
):
    """Apply fail-closed per-frame geometry thresholds."""
    reasons = []
    if int(result["inlier_count"]) < int(min_inliers):
        reasons.append("inliers")
    if float(result["inlier_ratio"]) < float(min_inlier_ratio):
        reasons.append("ratio")
    if float(result["span_m"]) < float(min_span_m):
        reasons.append("span")
    if float(result["residual_p95_m"]) > float(max_residual_p95_m):
        reasons.append("residual")
    return {"passed": not reasons, "reasons": reasons}


def summarize_axis_frames(axes, attempted_frames=None):
    """Summarize sign-ambiguous per-frame axes as one oriented direction."""
    array = np.asarray(axes, dtype=np.float64).reshape((-1, 3))
    finite = np.isfinite(array).all(axis=1)
    array = array[finite]
    if array.shape[0] == 0:
        raise ValueError("no finite axes")
    norms = np.linalg.norm(array, axis=1)
    array = array[norms > 1e-9]
    array = array / np.linalg.norm(array, axis=1, keepdims=True)
    reference = array[0].copy()
    for index in range(array.shape[0]):
        if np.dot(array[index], reference) < 0.0:
            array[index] *= -1.0
    axis = np.mean(array, axis=0)
    axis /= np.linalg.norm(axis)
    for index in range(array.shape[0]):
        if np.dot(array[index], axis) < 0.0:
            array[index] *= -1.0
    dots = np.clip(np.dot(array, axis), -1.0, 1.0)
    angles = np.degrees(np.arccos(dots))
    attempted = int(attempted_frames) if attempted_frames is not None else len(axes)
    return {
        "axis": axis,
        "valid_frames": int(array.shape[0]),
        "attempted_frames": attempted,
        "valid_rate": float(array.shape[0]) / max(attempted, 1),
        "angular_median_deg": float(np.median(angles)),
        "angular_p95_deg": float(np.percentile(angles, 95)),
        "angles_deg": angles,
    }
