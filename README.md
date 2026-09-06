# teasci｜茶芽主动视觉研究协作仓库

目标：以开发板、720p 双目深度相机和可搭建的电动相机平台，研究自然茶树芽叶视觉问题；投稿目标口径为 **JCR Q1–Q3**。当前处于选题收敛与先导实验准备阶段，尚无本项目实验结果，尚未确认新颖性或具体投稿期刊。

**合作者先读：[当前共识与边界](docs/CURRENT_STATE.md) → [证据纠正记录](docs/DECISIONS.md) → [任务台账](docs/TASKS.md)。** 较早建议保存在档案中，不能覆盖最新纠正。

## 当前研究定位

用户 U18 已将本轮调查限定为：在自然茶树的固定区域内，初始目标数量和位置未知；在相同观察预算与误检约束下，利用双目几何和观察历史选择补充视角，能否比固定扫描和已有主动视觉方法发现更多独立茶芽？

这是用户明确的调查问题，尚非已验证方法。最新结果见 [限定问题现状审查](literature/REGIONAL_DISCOVERY_REVIEW_2026-09-06.md)：问题框架已有高度接近研究，等误检与实际预算收益仍需实验。具体算法和协议是助手建议，待先导数据确认。不要求第一篇完成整套自主采摘产品，也不把“低成本相机”“概率云”“移动视角”单独当作创新。

## 查找入口

| 想了解什么 | 去哪里 |
| --- | --- |
| 硬件条件、用户认可的简化、未确定事项 | [CURRENT_STATE](docs/CURRENT_STATE.md) |
| 为什么从 ROI 转向区域主动视觉；哪些旧推断已纠正 | [DECISIONS](docs/DECISIONS.md) |
| 开始新工作前查重、认领、提交成果的办法 | [CONTRIBUTING](CONTRIBUTING.md) |
| 下一步实验、职责与完成条件 | [TASKS](docs/TASKS.md) |
| 行动前要准备什么、何时进入正式比较 | [PREPARATION](docs/PREPARATION.md)、[协议冻结表](experiments/templates/protocol_freeze.md) |
| 关键近邻、可引用结论及不能外推的内容 | [文献审查入口](literature/README.md)、[最新证据审查](literature/CURRENT_AUDIT.md) |
| 四轮历史审查中全部文献条目的可搜索台账 | [literature_index.csv](literature/literature_index.csv) |
| 已经用过的检索词，避免重新广搜 | [search_log.csv](literature/search_log.csv) |
| 曾讨论过的 38 个可检验问题 | [question_index.csv](literature/question_index.csv)，当前优先级仍以任务台账为准 |
| 最小可行实验与指标分母 | [EXPERIMENT_PLAN](docs/EXPERIMENT_PLAN.md)、[METRICS](docs/METRICS.md) |
| 数据字段、实验版本、空白记录表 | [实验记录入口](experiments/README.md) |
| 用户逐条原话、最近两轮答复和较早四份报告 | [对话与原始报告档案](archive/README.md) |

先导协议已修订为 `pilot-v0.2` 建议版：同一截止清单评价发现率与精确率、观察后再改变场景核验、限定稳定回放、分开机制与系统比较、保存完整快照、采用三种去留判断。修订来源见 D22–D27。现在可认领 T01/T02/T04 开展盘点、标注定义和开发试采；型号、场地、预算与记录程序验收等进入条件仍需实际证据。

## 接手规则

1. 先查任务编号、DOI 和已有报告；为同一问题继续补证，不另开一轮无边界搜索。
2. 在任务台账认领一项，注明预计交付物；未分配姓名表示尚未有人接手。
3. 把结果写成“证据/实验 → 支持什么 → 不支持什么 → 对当前决策的影响”。失败和无收益同样归档。
4. 新结论与旧结论冲突时，在决策记录中追加纠正，并更新当前状态；历史报告保持原样。

## 本次入库范围

维护日期：2026-09-06。包含当前可取得的对话内容、四份 2026-09-05 原始审查报告、后续证据纠正和可执行协作模板。**这不是聊天平台的全量原始导出**；覆盖限制见档案说明。尚未导入真实茶树数据、训练权重或算法代码；表格模板没有填造实验结果。

更新文献索引：`python tools/build_indexes.py`。检查文件链接、索引和档案完整性：`python tools/validate_repository.py`。
