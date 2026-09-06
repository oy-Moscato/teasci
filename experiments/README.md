# 实验记录

当前只有空白模板，没有本项目实测数据或采集/评价程序。建议协议 `pilot-v0.2` 修订了字段结构；模板不含数据，不表示日志功能已实现或验收。已有外部记录若需迁移，保留原件、注明原版本并检查字段含义，不能只改版本号。行动顺序见 [PREPARATION](../docs/PREPARATION.md)，协议见 [EXPERIMENT_PLAN](../docs/EXPERIMENT_PLAN.md)，指标见 [METRICS](../docs/METRICS.md)。

| 模板 | 每行是什么 |
| --- | --- |
| [hardware_inventory.csv](templates/hardware_inventory.csv) | 一个硬件或软件配置项，未测信息留空 |
| [regions.csv](templates/regions.csv) | 一个区域、场景、真值版本组合的边界定义与真值统计 |
| [scene_batches.csv](templates/scene_batches.csv) | 一个非破坏观察批次、参考复拍、变化质检与后验核验时序 |
| [runs.csv](templates/runs.csv) | 一次策略运行与场景、数据批次、比较层、版本、预算、时间模式 |
| [observations.csv](templates/observations.csv) | 一次观察尝试及分阶段时间；回放时关联原始采集记录 |
| [targets.csv](templates/targets.csv) | 一个场景/真值版本内的独立真值芽梢，仅评价侧可读 |
| [predictions.csv](templates/predictions.csv) | 一条观测级预测及可用时间；同一运行可用 track_id 关联 |
| [output_snapshots.csv](templates/output_snapshots.csv) | 一个预算点的不可变清单元记录，空输出也必须有一行 |
| [output_items.csv](templates/output_items.csv) | 截止清单的一条已确认存在的输出，保留伪目标与残留重复 |
| [output_matches.csv](templates/output_matches.csv) | 一条输出的后验真值匹配，仅评价侧可读 |
| [outcomes.csv](templates/outcomes.csv) | 一个真值目标在一个快照下的状态及历史诊断，仅评价侧可读 |
| [protocol_freeze.md](templates/protocol_freeze.md) | 一次比较的工作协议、冻结参数、证据及进入条件 |
| [run_report.md](templates/run_report.md) | 一次实验的可复核说明 |

## 关联与版本

`region_id` 表示固定空间区域；`scene_version` 表示物理状态；`ground_truth_version` 表示该状态的标注修订。区域表和目标表使用这三个字段定位同一评价场景，不能跨版本混用计数。场景被触碰、移除或发生超出预定判据的变化时换场景版本；仅修订标注则换真值版本，并对所有方法一致重算。`regions.csv` 的总数只在真值充分时填写；未决项另计并按冻结规则报告影响范围。

`batch_id` 关联一次采集批次，可被多次回放运行引用；同一场景可能有多个批次。所有相关批次的非破坏观察结束后才可开始改变场景的真值核验。`qc_status`（质检状态）取 `pass`（满足稳定性判据）、`changed`（发生超限变化）、`uncertain`（未确定）；规则版本和证据须可追溯，不用空值冒充通过。

`run_id`、`observation_id`、`prediction_id`、`snapshot_id` 各自在数据集中唯一。`output_id` 在快照内唯一；它与 `snapshot_id` 共同连接输出及匹配。`target_id` 在场景/真值版本内唯一。`track_id` 只是系统对象标识，不能直接当真值身份；评价一一匹配不要求机器人永远返回同一芽。

`view_index` 从 1 起按运行内观察尝试顺序递增，不表示不同位姿数量；`pose_id` 标识位姿，`source_observation_id` 指向原始采集索引。静态回放重复访问同一位姿时，新建观察事件，但复用同一原始记录。`charged_event` 为 0 或 1，失败是否收费按冻结规则；`charged_events` 为截止累计收费事件数。初始和正常重复观察必须收费。`event_status`（事件状态）取 `completed`（完成）、`failed`（失败）、`timeout`（超时）。无效图记失败并说明原因；帧数和推理次数记录实际值，不能绕过每事件冻结上限。

## 输出与匹配

`output_snapshots.csv` 记录截止可用状态版本，`item_count` 必须等于对应条目数。空清单保存元记录且条目数为零，不能以缺失文件代表空结果。运行起点建立初始清单版本；尚无观察时 `last_observation_index` 和 `charged_events` 为 0，保持未知目标数，不从真值初始化对象。`output_hash` 是归档的不可变输出清单文件的 SHA256；文件路径和哈希对应关系在数据清单中登记。

`output_items.csv` 只收录已确认存在、尚未删除的对外输出，因此 `existence_confirmed` 均为 1；原始候选保留在预测表。等级是否准入另用 `grade_accepted`，不能用分级拒绝删除主发现率的已确认对象。`support_observation_ids` 用分号分隔，只能引用截止前已开放的观察；缺少可靠三维位置时留空并保存匹配证据，不能填零坐标冒充测量。

每条输出在评价表必须有一条记录，包括错误输出。`match_status`（匹配状态）取 `correct`（正确匹配）、`duplicate`（同芽残留重复）、`spurious`（无符合区域/对象定义的真值匹配）、`unresolved`（证据未决）。同一快照内一个真值最多对应一条 `correct`；重复条目保留关联目标但不计正确。匹配冲突按冻结规则处理，不人工选出有利于某个方法的配对。未决项保留输出分母并报告正确数的可能范围，不静默排除。`grade_correct` 仅在可判定分级时填写，存在正确不自动代表分级正确。

`predictions.csv` 的 `accepted` 只表示观测级候选达到固定原始候选门槛，不是融合后的确认状态或等级准入；门槛含义在冻结表说明。`available_s` 用于判断候选何时可用。`outcomes.csv` 的 `ever_detected` 和 `first_detected_s` 只汇总该快照截止前的已可用候选，`confirmed_in_snapshot` 表示该真值是否仍被清单正确表示。主精确率必须从输出和匹配表计算，真值侧结果表不能表达全部伪目标和重复。

## 时间、数据与隔离

`time_mode`（时间模式）取 `live`（现场）、`replay_events`（事件预算回放）、`replay_estimated`（成本模型时间回放）。`budget_type`（预算类型）取 `view_events`（收费观察事件数）、`wall_time`（现场墙钟秒数）、`estimated_time`（模型估计秒数）；`wall_time` 只适用于现场，`estimated_time` 只适用于成本模型回放。每个运行可有多个预定预算点。

`cutoff_s`、`state_available_s`、观测阶段时间和候选/条目中的相对时间遵循运行时间模式，以共同运行起点为零。现场为真实经过秒数；事件回放记录的秒数只是回放运行时间；时间回放为同一成本模型时钟，必须登记测量来源与模型版本。禁止将后两者写成实测平台时间。`budget_value` 在事件预算中为事件数，在时间预算中等于 `cutoff_s`。事件快照在第 K 个收费事件处理完保存，同时记录最后尝试序号；不得使用额外观察。

`state_available_s` 是不可变清单版本已对外可用的时间，时间截止须满足它不晚于 `cutoff_s`；`recorded_s` 始终是归档程序自真实运行开始的经过秒数，`recorded_at` 是实际归档日期时间。现场归档可晚于截止，但只能保存截止前已固定的版本；回放的实际归档时间不能与模拟截止直接比较。`scan_wall_time_s` 始终记录真实执行墙钟时长，在回放中不代表实体扫描时间。分项时间有重叠时不直接相加。

`source_capture_at` 是原始拍摄日期时间，批次的 `_at`、运行的 `start_time`/`end_time` 以及 `recorded_at` 使用含时区的 ISO 8601；其他相对时间单位为秒。长度为米，姿态四元数顺序是 `qx,qy,qz,qw`，坐标系与变换方向在冻结表声明。CSV 空值表示未记录或不适用，原因须说明；布尔值用 0/1，未知不能填 0。可观测性字段用 `visible`（已见证可见）、`not_visible_in_checked_set`（已检查集合内不可见）、`unknown`（未确定），并给出所指视图集。

图像、深度、日志通过相对路径或团队可访问的数据版本引用，在 `data_manifest_path` 登记原始左右图、深度、位姿、成本依据、输出清单及 SHA256。图像侧真值标记不得进入算法输入。区域定义和标定可作为输入，区域真值统计、目标表、输出匹配、真值结果表及未选视图仅评价/采集侧可读。控制器只接收已选视图与可用历史；冻结表写明实际隔离措施，不能只靠“约定不看”。

建议结果路径为 `experiments/results/<run_id>/`；尚未有实验时不预填成果。大型原始图像、视频或模型权重不直接混入文献仓库，先约定数据存储位置。
