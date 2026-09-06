# 协作与减少重复工作

## 开始前

1. 阅读 [CURRENT_STATE](docs/CURRENT_STATE.md) 与 [DECISIONS](docs/DECISIONS.md)。
2. 查 [TASKS](docs/TASKS.md) 是否有人正在做同一项；在本表认领，注明预期交付物。
3. 文献工作按 DOI/题名搜索 [文献索引](literature/literature_index.csv)；检索词查 [search_log](literature/search_log.csv)。`Hxxx` 是历史条目 ID，同一 DOI 多个条目表示证据来源不同，不代表多篇论文。
4. 需要补证时写明缺失字段，例如“目标由谁选择”“分母是否包含未检出芽”“是否反馈选视点”，而不是重新搜一遍茶叶机器人。

## 交付

- 建议分支名 `docs/T03-method-comparison` 或 `experiment/T05-fixed-scan`，提交说明引用任务/决策编号。
- 文献新增条目写进 `literature/current_sources.json`：原始来源 URL、证据类型、核查范围、结论边界、后续需查什么。先核对版本/撤稿状态。
- 新检索记录加到 `literature/additional_searches.json`；记录实际提交的查询，不补造不存在的逐次日志。
- 运行 `python tools/build_indexes.py` 更新索引，再运行 `python tools/validate_repository.py`。
- 实验使用 `experiments/templates/`，保留 protocol、模型、校准、平台和代码版本。真实数据大文件单独保存并登记可访问位置；不要把访问凭证放进仓库。
- 完成后更新任务状态和交付物链接；若结论改变选题，追加 Dxx 并同步 CURRENT_STATE。

## 证据状态

`F`：核过相关原文段落，不等于已复现整个实验。`A`：原始/作者机构摘要。`S`：题名、元数据或出版方检索片段。`NEWS`：记者对团队的原始报道。`COMPANY`：企业自述。`RETRACTED`：已撤稿记录。`HISTORY`：从既有报告迁移，核查深度以原报告为准，本次未重复审读。`PENDING`：待核验线索。

新闻可证明有公开演示/团队主张，不能代替可复核实验分母。方法近邻不要求都为 SCI 论文，但期刊、会议、预印本、专利必须分开记录。不能把“未检出”升级为“无人研究”。

## 避免结论漂移

四份历史报告原样保存。任何纠正写入现行文档，不静默重写旧报告；档案哈希用于核对保存完整性。不要把报告中的旧优先级带回当前任务。

本仓库维护不等于后台自动同步聊天。后续讨论产生新决定时，把新内容与相应证据写入同一套文档；只有实际提交完成后才视为已同步。
