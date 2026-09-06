# 三项现场指标的来源与计算边界

整理日期：2026-09-06。本页只追踪既有记录，不补算新实验，不把代理植物结果写成茶芽结果。

## 1. 约 9.36% 深度有效率

- 原文：`abot_proxy/reports/09_现场植物代理闭环验证_20260724.md` 第 25 行，记录户外初始帧在 `0.15-3.0 m` 范围内的有效像素率约 `9.36%`，有效深度中位数约 `2.106 m`。
- 相关函数：`abot_proxy/geometry/stem_axis_geometry.py::valid_depth_mask()` 将有限深度且位于 `[0.15, 3.0] m` 的像素标为有效；`registered_depth_snapshot.py` 以 `valid.mean()` 写出 `valid_ratio`。
- 状态：**原文已找到，口径相关函数已找到；精确对应这一个 9.36% 初始帧的原始 XYZ/depth 数组或 metadata 未在限定目录中找到，因此不能独立重算该数字。**

## 2. 约 1.008° 方向偏差

- 原文：`abot_proxy/reports/10_现场代理茎3D方向闭环_20260724.md` 第 72 行。
- 原始结果：`abot_proxy/geometry/final_30frames.json` 的 `aggregate.angular_median_deg=1.0076688283611526`，四舍五入为 `1.008°`；29/30 帧有效。
- 计算函数：`stem_axis_geometry.py::summarize_axis_frames()` 先归一化每帧方向、处理轴向符号，再计算平均单位轴；各帧与平均轴的夹角为 `degrees(arccos(dot))`，最后取中位数与 P95。
- 状态：**原文、聚合结果和计算函数均已找到。**它衡量代理茎轴的帧间方向稳定性，不是茶芽姿态绝对误差。

## 3. 10.50 mm 拟合残差

- 原文：`abot_proxy/reports/10_现场代理茎3D方向闭环_20260724.md` 第 76 行，并在第 120 行明确警告它不等于绝对三维精度。
- 原始结果：`final_30frames.json` 保存每个有效帧的 `residual_p95_m`。29 个有效帧的该字段中位数为 `0.010503640510746048 m`，即 `10.503640510746048 mm`，报告取两位小数为 `10.50 mm`。
- 计算函数：`stem_axis_geometry.py::_line_residuals()` 计算点到拟合轴的正交距离；`fit_oriented_axis()` 对最终内点取残差第 95 百分位。报告再对29个有效帧的 `residual_p95_m` 取中位数。
- 状态：**原文、逐帧结果和计算函数均已找到。**该量是代理关键点直线拟合残差，不是相机绝对深度精度，也没有替代 0.3/0.5/0.8 m 物理标定。
