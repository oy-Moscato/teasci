# 本机既有资料证据索引

整理日期：2026-09-06。

## 使用边界

这些资料来自本机另一个茶园采摘项目及其 ABOT-X4 代理实验，供 `teasci` 先导实验准备参考。它们不是 `teasci` 已完成的自然茶树主动视觉实验，不改变仓库根 `README.md` 与 `docs/CURRENT_STATE.md` 中“本项目尚无实验结果”的状态。

来源别名：

- `SRC-PROJECT`：桌面 `sci与ros2项目`。索引未写入本机用户绝对路径。
- `SRC-ABOT`：`SRC-PROJECT` 内 ABOT-X4 本机权威资料目录。索引省略了目录名中的局域网地址。

未上传全部82帧、公开/合成数据集、模型权重、虚拟环境、SDK、日志目录或运行环境。本机原件均保留原位。

## 文件清单与来源

| 仓库路径 | 用途 | 来源与日期 | 类型/删改 |
| --- | --- | --- | --- |
| `LOCAL_INVENTORY_SUMMARY_2026-09-06.md` | 本次轻量盘点结论 | 本次整理，2026-09-06 | 新建摘要；不是原始实验记录 |
| `METRIC_PROVENANCE.md` | 追踪9.36%、1.008°、10.50 mm的原文、结果与函数 | 本次整理，2026-09-06 | 新建证据说明；没有补跑实验 |
| `SHA256SUMS` | 上传内容完整性校验 | 本次整理，2026-09-06 | 不包含自身和会继续维护的 `INDEX.md` |
| `camera_session_82_frames/calibration.json` | GeminiPro 会话内参、depth-to-color 与尺度 | `SRC-PROJECT/tea_picking/tools/geminipro_workbench/runtime/captures/geminipro_real_adapter_smoke_20260804/calibration.json`，会话日期2026-08-04 | 原件完整副本，未改 |
| `camera_session_82_frames/frames_first3_last3_EXCERPT.jsonl` | 展示82帧会话首3条、末3条合同 | 同会话 `frames.jsonl` | **节选**；六条 JSONL 记录未改写。原文件历史 `domain_tag=tea_garden_proxy` 已知会误导，实际画面为室内，不能按字段名当作茶园数据 |
| `camera_session_82_frames/frame_00000000/rgb_00000000.png` | 一组对应彩色原图 | 同会话 `rgb/00000000.png` | 原件完整副本，未改 |
| `camera_session_82_frames/frame_00000000/depth_00000000.png` | 同一帧Y16深度图 | 同会话 `depth/00000000.png` | 原件完整副本，未改 |
| `camera_session_82_frames/frame_00000000/invalid_mask_00000000.png` | 同一帧无效深度掩膜 | 同会话 `invalid_mask/00000000.png` | 原件完整副本，未改 |
| `abot_proxy/reports/06_RGB高分辨率解耦修复与标定门_20260720.md` | 相机坐标变换、临时内外参及物理标定缺口 | `SRC-ABOT/06_...md`，2026-07-20 | 内容副本；仅将未上传附件的失效链接改为原相对路径文字并注明未纳入，事实文字未改 |
| `abot_proxy/reports/09_现场植物代理闭环验证_20260724.md` | 9.36%深度有效率、50%定位率和安全拒绝原文 | `SRC-ABOT/09_...md`，2026-07-24 | **脱敏/链接整理副本**；删除登录名、局域网地址和路由名称；未上传附件改为路径文字，科学内容未改 |
| `abot_proxy/reports/10_现场代理茎3D方向闭环_20260724.md` | 29/30、1.008°与10.50 mm原文 | `SRC-ABOT/10_...md`，2026-07-24 | 内容副本；已上传代码/JSON链接改指本目录，未上传附件改为原相对路径文字，事实文字未改 |
| `abot_proxy/scan/manifest.json` | 两轴5x6、共30视角的图名、yaw、pitch与时间戳 | `SRC-ABOT/artifacts/现场代理茎3D方向_20260724/wide_scan/manifest.json`，2026-07-24 | 原件完整副本，未改；不含30张图 |
| `abot_proxy/scan/camera_servo_grid_scan.py` | 两轴角度网格和舵机命令实现 | `SRC-ABOT/tools/camera_servo_grid_scan.py` | 原件完整副本，未改 |
| `abot_proxy/config_notes/servo_axis_control_EXCERPT.txt` | Servo1/Servo2 与左右/上下转轴关系 | `SRC-ABOT/sources/物流搬运实践快速上手指南.txt` 第50-52行 | **节选**；省略无关操作说明 |
| `abot_proxy/config_notes/camera_tf_runtime_EXCERPT.txt` | 现场运行时 camera/depth/rgb/optical frame 静态TF | `SRC-ABOT/artifacts/RGB七档视频流实测_20260720/logs/final_processes.txt` 第299-302行 | **脱敏节选**；去除PID、状态和本机日志路径 |
| `abot_proxy/geometry/registered_depth_snapshot.py` | 深度有效掩膜调用及 `valid.mean()` 比例写出 | `SRC-ABOT/tools/registered_depth_snapshot.py` | 原件完整副本，未改 |
| `abot_proxy/geometry/stem_axis_geometry.py` | 深度门、点到轴残差、P95、方向角中位数/P95计算 | `SRC-ABOT/tools/stem_axis_geometry.py` | 原件完整副本，未改 |
| `abot_proxy/geometry/stem_axis_live_probe.py` | 30帧现场采样、质量门和聚合写出 | `SRC-ABOT/tools/stem_axis_live_probe.py` | 原件完整副本，未改 |
| `abot_proxy/geometry/test_stem_axis_geometry.py` | 相关几何函数的既有单元测试 | `SRC-ABOT/tools/test_stem_axis_geometry.py` | 原件完整副本，未改；本次未执行测试 |
| `abot_proxy/geometry/final_30frames.json` | 29个有效帧逐帧轴、残差及聚合结果 | `SRC-ABOT/artifacts/现场代理茎3D方向_20260724/final_30frames.json`，2026-07-24 | 原件完整副本，未改 |

## 已知缺失项

- `teasci` 用户所述开发板和720p双目相机与上述 GeminiPro/ABOT 设备是否为同一硬件：**未知**。
- 原始双目左图、右图输出与标定：**未找到**；现有程序只证明 RGB/Depth。
- 云台相机物理安装图、相对本体外参、转轴交点、角度零位、行程、重复定位和回差测量：**未找到**。现有TF仅为运行时快照，不能当作物理标定完成。
- 30视角扫描的30张图、目标级跨视角对应和相机SE(3)位姿：本次未上传；原资料也没有标定后的相机位姿或茶芽对应。
- 9.36%初始帧对应的原始depth/XYZ数组或metadata：**未找到**；仅有报告原文和相同口径的计算函数。
- 真实茶树/茶芽 RGB-D 多视角数据、视频、相机轨迹、P0/P1/P2或4KP/seg标注、茶芽模型权重：**未找到**。
- 0.3/0.5/0.8 m 物理精度、深度绝对误差、云台角度重复性和跨视角配准误差：**未完成或未找到**。
- 湛江茶园实际访问、许可、采集日期与熟练人工真值核验记录：现有内容只有计划，**不能写成已完成**。

## 脱敏检查

- 未发现 API key、token、密码、私钥或认证头。
- 三份报告仅整理离开原目录后失效的相对链接；`09_...md` 另删除了与科学证据无关的本地登录和网络入口。
- TF 节选删除了PID和本机运行日志路径。
- 图像为室内设备冒烟场景，未发现人物；未对像素作修改。

## 本次整理验证

- 11个标为“原件完整副本”的 JSON、PNG、Python 和 manifest 文件已与本机来源逐一比对 SHA256，全部一致。
- `frames_first3_last3_EXCERPT.jsonl` 已与原82行文件的首3行、末3行逐行比对，六行全部一致。
- 三个 JSON 与六行 JSONL 均通过解析；30视角 manifest 的 `count=30`，82帧原 manifest 行数为82。
- 仓库链接校验对本次新增内容不再报断链。仓库 `main` 自身已有4份 `archive/reports/*.md` 与 `archive/manifest.json` 记录哈希不匹配；本分支未修改这些历史档案或清单，因此全仓校验仍以该基线问题退出1。
