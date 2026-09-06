import math
import pathlib
import sys

import numpy as np


sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from stem_axis_geometry import (  # noqa: E402
    fit_oriented_axis,
    is_fresh_stamp,
    localize_keypoint_cluster,
    quality_gate,
    summarize_axis_frames,
    valid_depth_mask,
)


K = np.array(
    [[400.0, 0.0, 320.0], [0.0, 400.0, 240.0], [0.0, 0.0, 1.0]],
    dtype=np.float64,
)


def xyz_from_uvz(u, v, z):
    return np.array([(u - 320.0) * z / 400.0, (v - 240.0) * z / 400.0, z])


def test_localize_keypoint_selects_nearest_supported_depth_cluster():
    near = np.array(
        [xyz_from_uvz(100 + dx, 120 + dy, 0.80 + 0.001 * dx) for dx in range(-3, 4) for dy in range(-2, 3)]
    )
    far = np.array(
        [xyz_from_uvz(100 + dx, 120 + dy, 1.40) for dx in range(-2, 3) for dy in range(-2, 3)]
    )
    points = np.vstack([near, far, [[np.nan, 0.0, 0.0]]])

    result = localize_keypoint_cluster(
        points, K, (100.0, 120.0), radius_px=8.0, min_points=8
    )

    assert result is not None
    assert result["support"] >= 8
    assert result["point"][2] == pytest_approx(0.80, abs=0.015)


def test_localize_keypoint_rejects_sparse_depth():
    points = np.array([xyz_from_uvz(100, 120, 0.8)] * 3)
    assert (
        localize_keypoint_cluster(
            points, K, (100.0, 120.0), radius_px=5.0, min_points=4
        )
        is None
    )


def test_fit_axis_recovers_ordered_direction_with_outlier():
    expected = np.array([0.2, -0.1, 0.97], dtype=np.float64)
    expected /= np.linalg.norm(expected)
    origin = np.array([0.1, 0.05, 0.7])
    samples = np.array([origin + expected * s for s in (0.0, 0.04, 0.08, 0.12)])
    samples[1] += np.array([0.001, -0.001, 0.0005])
    samples = np.vstack([samples, [0.5, 0.5, 1.5]])
    order = np.array([0.0, 1.0, 2.0, 3.0, np.nan])

    result = fit_oriented_axis(samples, order=order, residual_threshold_m=0.01)

    assert np.dot(result["axis"], expected) > 0.999
    assert result["span_m"] > 0.10
    assert result["inlier_count"] == 4
    assert result["residual_p95_m"] < 0.003


def test_quality_gate_rejects_short_or_unstable_axis():
    base = {
        "inlier_count": 4,
        "inlier_ratio": 1.0,
        "span_m": 0.08,
        "residual_p95_m": 0.003,
    }
    assert quality_gate(base)["passed"] is True

    short = dict(base, span_m=0.01)
    decision = quality_gate(short)
    assert decision["passed"] is False
    assert "span" in decision["reasons"]


def test_summarize_axis_frames_orients_sign_and_reports_angle_p95():
    axes = []
    for deg in (0.0, 2.0, -3.0, 4.0):
        rad = math.radians(deg)
        axes.append([math.sin(rad), 0.0, math.cos(rad)])
    axes.append([0.0, 0.0, -1.0])

    summary = summarize_axis_frames(axes, attempted_frames=6)

    assert summary["valid_frames"] == 5
    assert summary["valid_rate"] == pytest_approx(5.0 / 6.0)
    assert summary["angular_p95_deg"] < 5.0
    assert summary["axis"][2] > 0.99


def test_is_fresh_stamp_rejects_cached_or_future_frame():
    assert is_fresh_stamp(100.0, 101.5, max_age_s=2.0) is True
    assert is_fresh_stamp(100.0, 102.1, max_age_s=2.0) is False
    assert is_fresh_stamp(103.0, 102.0, max_age_s=2.0) is False


def test_valid_depth_mask_rejects_zero_nan_and_out_of_range():
    depth = np.array([[0.0, np.nan, 0.14, 0.15, 1.0, 3.0, 3.01]])
    assert valid_depth_mask(depth).tolist() == [[False, False, False, True, True, True, False]]


def pytest_approx(value, **kwargs):
    import pytest

    return pytest.approx(value, **kwargs)
