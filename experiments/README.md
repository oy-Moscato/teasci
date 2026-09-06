# 实验记录

当前只有空白模板，没有本项目实测数据。协议见 [EXPERIMENT_PLAN](../docs/EXPERIMENT_PLAN.md)，指标见 [METRICS](../docs/METRICS.md)。

| 模板 | 每行是什么 |
| --- | --- |
| [hardware_inventory.csv](templates/hardware_inventory.csv) | 一个硬件或软件配置项，未测信息留空 |
| [regions.csv](templates/regions.csv) | 一个预先界定的区域及其真值核验状态 |
| [runs.csv](templates/runs.csv) | 一次算法/策略运行与版本、预算、条件 |
| [observations.csv](templates/observations.csv) | 一次实际相机观察及各阶段时间 |
| [targets.csv](templates/targets.csv) | 一个区域内独立真值芽梢 |
| [predictions.csv](templates/predictions.csv) | 一个预测实例；同一运行中跨观察使用 track_id |
| [outcomes.csv](templates/outcomes.csv) | 一个真值目标在某次运行中的最终状态 |
| [run_report.md](templates/run_report.md) | 一次实验的可复核说明 |

`region_id` 连接真值和运行，`run_id` 连接观察/预测/结果。时间单位统一为秒、长度为米；位姿字段在运行报告声明坐标系。CSV 空值代表未记录，数值 0 代表实际为零；不要混用。

`observation_id` 唯一标识一次观察；`prediction_id` 标识一条观测级预测；`track_id` 标识系统认为的独立对象。评价时按预先定义的最终清单与真值一一匹配，不能对每帧重复累加 TP。

图像/深度/日志通过相对路径或团队可访问的数据集版本引用；记录 SHA256。标注图中用于人工真值的标记不能被算法利用。算法运行时不读取 `targets.csv` 或真值相关字段。

建议结果路径为 `experiments/results/<run_id>/`；尚未有实验时不预填成果。大型原始图像、视频或模型权重不直接混入文献仓库，先约定数据存储位置。
