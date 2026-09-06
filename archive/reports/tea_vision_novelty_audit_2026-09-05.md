**茶树芽叶视觉项目：选题与方法重复风险广度审查**

检索截止：2026-09-05。项目条件：开发板型号未定、720p 双目深度相机；对象为仍生长在茶树上的芽叶；主任务为形态分级，备选为相机对准和采摘。合作者可能偏机械设计与基础控制，也可能偏现代控制理论。

**审查结论**

此前提出的“让 ROI 裁剪成为有反馈的计算决策”需要降低创新预期。闭环 ROI、ROI 与视觉伺服结合、主动选择视点并决定停止时间，均已有直接方法论文。茶芽轻量化分级、结构关键点、双目定位，以及负压引导末端的偏差容忍也已有同领域工作。换用茶叶、720p 相机或低成本开发板，单独看都不足以证明方法创新。

这并不等于项目不能发表，也不意味着研究近似就是学术不端。当前还没有完整方法、实验结果与论文文本，能审查的是拟议贡献与已有研究的重合风险。应用论文可以凭明确的问题建模、必要的工程改进、可信的真实实验及可推广的发现形成贡献；不能预先保证录用或分区。

在当前资源下，优先保留“在树芽叶完整分级所需的证据如何被经济地补全”，将软件裁剪和真实相机位移作为不同的观测动作。相机对准可作为后续验证任务，不能作为避开重复的自动退路。采摘需要更完整的实体试验，暂不宜只凭现有相机和开发板定为第一篇主线。

**范围与证据边界**

本次保存了 42 条主题和题名检索记录，另做针对性来源核验。检索覆盖茶叶分级、ROI 与边缘计算、主动视觉、视点与停止决策、视觉伺服、双目定位、末端容错。以下保留 26 条与判断直接相关的文献或状态记录。该数量是筛选后的记录数，不是完整领域文献数。

采用出版商页面、会议官方论文集、作者公开论文和机构仓储作为技术判断来源。仅有题名或搜索摘要的条目降低证据等级；未将 ResearchGate、聚合站的介绍作为最终方法事实依据。本次未使用 Web of Science/Scopus 订阅库做完整检索导出，未逐篇核验年度 SCIE 入藏状态；“期刊论文”不自动等于已经核验的“SCI 收录论文”。会议和预印本单列，但它们同样影响创新性判断。

证据等级：F＝已读到支持判断的正文方法段；A＝已核对原始摘要；S＝主要依据出版商或作者来源的搜索索引片段；M＝仅核对题名、发表信息，具体方法待读。F 不代表逐页精读或复现实验。风险等级是定性判断，不是查重百分比。

**拟议贡献与已有工作的对应**

| 拟议主张 | 最接近的证据 | 重合判断 | 仍需区分的部分 |
|---|---|---|---|
| 轻量网络在开发板上做茶芽分级 | J01、J02 | 同领域高风险 | 具体硬件测量、不同工况的泛化，以及超出常规模块替换的贡献 |
| 关键点、叶片数量、芽叶结构辅助分级 | J02 | 同领域高风险 | 结构证据是否完整、同一枝梢的叶片归属、缺失证据对应的行动决策 |
| 双目图像分割后定位采摘点 | J04 | 同领域高风险 | 低质深度的可识别失效模式及其处理，不能仅换一款相机 |
| ROI 动态扩张、跨帧补齐边界目标 | J05、J09、C01 | 通用方法及邻近茶叶场景高风险 | J05 为采后分选；在树遮挡与输送带边界截断不同 |
| 让 ROI 接受跟踪反馈并控制计算 | J09、C02、C03 | 通用方法很高风险 | 软件裁剪、传感器读出、传输、推理调度分别发生在哪一层 |
| 预设视点切换、融合判断、足够确定时停止 | J10、J11、J12 | 通用方法很高风险 | 茶芽结构的可观测性，以及替代通用置信度的任务证据模型 |
| ROI 调度与相机对准组成闭环 | J08、J09、J13；J14 待精读 | 高风险 | 非刚性目标、动作相关的观测误差和时延是否产生已有方法未解决的问题 |
| 在视觉伺服中加入事件触发或 MPC | J13 | 通用方法很高风险 | 触发检测推理与触发控制优化不是同一件事，需要证明新增机制 |
| 负压引导或柔顺结构扩大采摘容差 | J07、P04 | 同领域很高风险 | 新的具体结构及容差—损伤—成功率关系，或新的控制贡献 |

**期刊近邻：茶叶任务**

| 编号 | 原始论文与来源 | 证据 | 已有内容与本项目的差别 |
|---|---|---|---|
| J01 | Tang et al. *A Lightweight Tea Bud-Grading Detection Model for Embedded Applications*. Agronomy, 2025, 15(3), 582. DOI: 10.3390/agronomy15030582。[出版商](https://www.mdpi.com/2073-4395/15/3/582) | S，发表信息已核验 | “茶芽分级＋轻量化＋嵌入式应用”已有明确同题研究。本次未取得足够正文支持具体开发板部署配置，不能把标题当作完整硬件验证。 |
| J02 | Yao et al. *Tea bud pose estimation and grading detection network based on improved YOLOv7*. Frontiers in Plant Science, 2026. DOI: 10.3389/fpls.2026.1786144。[全文](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.1786144/full) | F | YOLO-PC 同时估计姿态与分级，针对一芽一叶、一芽两叶标注芽顶、叶尖、叶基及采摘点。正文说明重度遮挡样本有标注排除规则。因此“加入结构关键点”不能独立宣称新颖；对不可充分观察的芽叶如何主动补证仍须另行比较。 |
| J03 | Hong et al. *An end-to-end detection and classification model for tea leaf grading in complex orchard environments*. Frontiers in Plant Science, 2026. DOI: 10.3389/fpls.2026.1814763。[全文](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2026.1814763/full) | F | Tea-DETR 检测自然茶园中的单叶等级，数据采集包含俯视、斜视与正视。其 T1—T4 是单叶发育与嫩度视觉类别，不是本项目的一芽几叶类别；多视角采集训练数据不等于在线选择下一视点。 |
| J04 | He et al. *Localization of Tea Shoots for Robotic Plucking Using Binocular Stereo Vision*. Journal of Field Robotics, 2025. DOI: 10.1002/rob.22559。[原始摘要](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22559) | A | 已结合双眼实例分割、实例配对、选择性立体匹配、三角测量与采摘点模板。单纯“双目＋分割＋三维定位”重合明显；其定位实验不能直接代表用户的 720p 相机精度。 |
| J05 | Zhang et al. *Design and implementation of a compact fresh tea-leaf sorting system for integrated harvesting–sorting equipment in hilly mountainous tea garden*. Artificial Intelligence in Agriculture, 2026. DOI: 10.1016/j.aiia.2026.04.010。[出版商](https://www.sciencedirect.com/science/article/pii/S2589721726000425) | S | 出版商检索片段明确提出通过区域跟踪和增长改善跨图像边界叶片识别的动态 ROI。属于采后鲜叶分选，不能据此判定在树主动分级已被完整覆盖；但“茶叶动态 ROI”不是空白。正文获取受限，网络结构与量化性能不在本报告中转述。 |
| J06 | Wang et al. *Automated tea shoot picking using the YOLO network and Mamba images segmentation for top-view detection with a monocular camera*. Journal of Agricultural Engineering，2025 年在线，2026 年卷期。DOI: 10.4081/jae.2025.1637。[原始摘要](https://www.agroengineering.org/jae/article/view/1637) | A | 明确采用 YOLO 找茶梢、裁剪单梢、Mamba 分割、定位并驱动末端；上下运动使用红外传感反馈。其试验为模拟茶园环境。不能再把“检测—裁剪—精分割—机械动作”整体当作新框架。 |
| J07 | Zhu et al. *Deviation Tolerance Performance Evaluation and Experiment of Picking End Effector for Famous Tea*. Agriculture, 2021, 11(2), 128. DOI: 10.3390/agriculture11020128。[出版商](https://www.mdpi.com/2077-0472/11/2/128) | S | 直接研究负压引导采摘末端和偏差容忍评价。机械创新需要落实为具体结构差异和实体对比；这篇不是后文列出的撤稿论文。 |

**期刊近邻：跨领域方法**

| 编号 | 原始论文与来源 | 证据 | 已有内容与本项目的差别 |
|---|---|---|---|
| J08 | Dahmouche et al. *Dynamic visual servoing from sequential regions of interest acquisition*. The International Journal of Robotics Research, 2012, 31(4), 520–537. DOI: 10.1177/0278364911436082。[原始摘要](https://journals.sagepub.com/doi/10.1177/0278364911436082) | A | 用包含视觉特征的 ROI 顺序采集支持动态视觉伺服，处理采样频率和处理时延问题，包含高速并联机器人实验。其采集层机制与普通整帧拍摄后软件裁剪不同，但“ROI＋视觉闭环＋减时延”已有明确前例。 |
| J09 | Chen et al. *Closed-Loop Region of Interest Enabling High Spatial and Temporal Resolutions in Object Detection and Tracking via Wireless Camera*. IEEE Access, 2021, 9, 87340–87350. DOI: 10.1109/ACCESS.2021.3086499。[IEEE](https://ieeexplore.ieee.org/document/9454528)；[作者机构存档](https://dspace.mit.edu/handle/1721.1/139785) | S | 题名与原始索引明确覆盖闭环 ROI、实时跟踪反馈和无线相机采集；还考虑宽视场扫描。用户的有线/本地推理条件可能不同，但不能主张首次闭环 ROI。机构全文本次访问受限。 |
| J10 | Atanasov et al. *Nonmyopic View Planning for Active Object Classification and Pose Estimation*. IEEE Transactions on Robotics, 2014, 30(5), 1078–1090. DOI: 10.1109/TRO.2014.2320795。[作者全文](https://existentialrobotics.org/ref/Atanasov_ActiveObjectRecognition_TRO14.pdf) | F | 联合选择视点序列、停止时间及分类/姿态假设，权衡移动代价和误判代价。正文 VI 节及式 (2) 明确包含继续观察与停止决策。其对象和观察模型不同，但“有限视点＋反馈选视点＋停止”已被直接覆盖。 |
| J11 | Jayaraman and Grauman. *End-to-End Policy Learning for Active Visual Categorization*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2019，在线版本 2018。DOI: 10.1109/TPAMI.2018.2840991。[出版商](https://www.computer.org/10.1109/TPAMI.2018.2840991)；[作者全文](https://www.engineering.upenn.edu/~dineshj/publication/jayaraman-2018-end/jayaraman-2018-end.pdf) | A | 主动视觉分类已研究感知、跨视图证据整合和观测行动的联合学习。换成强化学习或端到端策略不自动产生新的选题空间。 |
| J12 | Zhang et al. *Occlusion Avoidance for Harvesting Robots: A Lightweight Active Perception Model*. Sensors, 2026, 26(1), 291. DOI: 10.3390/s26010291。[出版商](https://www.mdpi.com/1424-8220/26/1/291)；[PMC 全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC12788279/) | A | 已有轻量感知与采摘遮挡规避的农业主动视觉工作，研究对象为果实。不能把“农业遮挡时移动相机”当作新颖点；茶芽同梢结构和等级判据需要单独提出。 |
| J13 | Zhang, Yao and Qian. *Event-Triggered Nonlinear Visual Predictive Control Strategy for Robots*. Journal of Intelligent & Robotic Systems, 2025, 111, 80. DOI: 10.1007/s10846-025-02292-7。[原始摘要及 PDF 入口](https://link.springer.com/article/10.1007/s10846-025-02292-7) | A | 已有事件触发非线性视觉预测控制，涉及视场、关节和运动约束及计算负担。该论文触发控制律/优化，不能直接等同于触发检测网络；新方案必须说明节省的是哪部分计算及其闭环后果。 |
| J14 | Tang et al. *A real-time perception–motion codesign method for image-based visual servoing in embodied intelligence systems*. Journal of Industrial Information Integration, 2025, 48, 100933. DOI: 10.1016/j.jii.2025.100933。[出版商](https://www.sciencedirect.com/science/article/pii/S2452414X25001566) | M | 题名直接涉及感知—运动协同设计，是控制方向定题前必须取得全文的近邻。此次访问受限，不据题名推断其具体 ROI、时延或触发机制，也不单凭它判定方案完全重复。 |

**容易误判成直接重复的期刊条目**

| 编号 | 原始论文与来源 | 证据 | 排除或降低直接相关性的原因 |
|---|---|---|---|
| J15 | *Lightweight Multi-View Fusion Network for Non-Destructive Chlorophyll and Nitrogen Content Estimation in Tea Leaves Using Front and Back RGB Images*. Agronomy, 2025. DOI: 10.3390/agronomy15102355。[出版商](https://www.mdpi.com/2073-4395/15/10/2355) | S | 正反面 RGB 融合估计叶绿素/氮含量；不是在树芽叶形态分级的在线视点策略。只说明“茶叶多视图融合”已有邻近研究。 |
| J16 | *Multi-view multi-task deep neural network for effective tea classification and quantitative flavor factor evaluation*. Computers and Electronics in Agriculture, 2026. DOI: 10.1016/j.compag.2026.111618。[出版商](https://www.sciencedirect.com/science/article/abs/pii/S0168169926002139) | S | 茶分类与风味因子评价，任务和输入视图语义不同；不能据关键词 multi-view、tea、classification 宣称完整覆盖本项目。 |
| J17 | *Rapid Extraction of Tea Bud Phenotypic Parameters ‘In Situ’ Combining Key Point Recognition and Depth Image Fusion*. Agriculture, 2026, 16(6), 704. DOI: 10.3390/agriculture16060704。[出版商](https://www.mdpi.com/2077-0472/16/6/704) | S | 原位茶芽关键点与深度融合已有表型测量应用。对“加深度、量尺寸”的新颖性构成近邻，但不能推断已实现主动分级闭环。 |

**会议论文：不列作 SCI 期刊，但必须比较**

| 编号 | 文献与来源 | 证据 | 对 ROI 路线的影响 |
|---|---|---|---|
| C01 | Najibi et al. *AutoFocus: Efficient Multi-Scale Inference*. ICCV, 2019。[CVF 官方论文](https://openaccess.thecvf.com/content_ICCV_2019/html/Najibi_AutoFocus_Efficient_Multi-Scale_Inference_ICCV_2019_paper.html) | A | 先粗看，再选择区域做细尺度推理。只做粗检测后裁剪放大，难以构成新方法。 |
| C02 | Chin et al. *AdaScale: Towards Real-time Video Object Detection using Adaptive Scaling*. MLSys, 2019。[官方论文集](https://proceedings.mlsys.org/paper_files/paper/2019/hash/b3ac5aacb06c91fda1af776a677100ab-Abstract.html) | A | 根据视频信息自适应选择输入尺度。ROI 方案若同时改变分辨率，应与这种计算分配思路比较。 |
| C03 | Jiang et al. *Flexible High-resolution Object Detection on Edge Devices with Tunable Latency*（Remix）. MobiCom, 2021. DOI: 10.1145/3447993.3483274。[作者机构](https://www.microsoft.com/en-us/research/publication/flexible-high-resolution-object-detection-on-edge-devices-with-tunable-latency/) | A | 延迟预算下的区域划分与检测计算配置已有研究。新方案需要证明超出一般的预算分配与分块推理。 |
| C04 | *Achieving Real-time Visual Tracking with Low-Cost Edge AI*. ICCPS, 2024. DOI: 10.1109/ICCPS61052.2024.00035。[IEEE](https://ieeexplore.ieee.org/document/10571650/) | S | 低成本边缘视觉跟踪已有直接近邻，检索发现其涉及自适应 ROI。具体算法和篇幅应取得作者稿再定量比较，不用题名保证部署结果。 |

**预印本与作者公开稿：单列发表状态**

| 编号 | 文献与来源 | 证据 | 对本项目的影响 |
|---|---|---|---|
| P01 | *ROI-Gated SAHI: Content-Adaptive Slicing-Based Inference for Efficient Object Detection*. arXiv:2608.23923，2026-08-25。[原文](https://arxiv.org/abs/2608.23923) | A | 前景候选限制切片细化，并采用路由策略。其摘要也报告固定 ROI 门控在所测完整数据上并非总能提速。属于近期预印本，不能称成熟 SCI 证据；可提醒本项目检验候选生成开销和场景稠密度。 |
| P02 | *Perception-Control Coupled Visual Servoing for Textureless Objects Using Keypoint-Based EKF*. arXiv:2602.06834，2026-02。[原文](https://arxiv.org/abs/2602.06834) | A | 已将关键点、EKF、相机运动反馈和不确定性感知控制结合。仅添加 EKF/协方差难以形成新颖点；其刚性物体任务与非刚性茶芽要明确区分。 |
| P03 | *From Keypoints to Predictive Distributions: Post-Hoc Uncertainty for YOLO-Pose Models*. arXiv:2607.26921，2026-07-29。[原文](https://arxiv.org/abs/2607.26921) | A | 为 YOLO-Pose 增加并校准空间预测分布已有近期公开工作。“关键点带不确定性”本身不是充分创新。 |
| P04 | Zhang et al. *Research on the Tender Leaf Identification and Mechanically Perceptible Plucking Finger for High-quality Green Tea*. 作者公开稿 arXiv:2405.05500，2024；记录关联 DOI: 10.1002/jsfa.13987。[作者公开稿](https://arxiv.org/abs/2405.05500) | A | 已结合嫩叶识别、有限元确定夹指/应变片设计和夹持力反馈。不能把“视觉＋柔性夹指＋力反馈”独立当作新贡献。本次未取得关联期刊页面，故不自行填写该期刊版本年份、卷期或入藏状态。 |

**撤稿记录**

R01：*Intelligent Tea-Picking System Based on Active Computer Vision and Internet of Things*，2021，DOI: 10.1155/2021/5302783，已出现出版商撤稿通知。[Wiley 官方撤稿通知](https://onlinelibrary.wiley.com/doi/10.1155/sec/9829724)

该条从有效技术证据中排除，不用来支持“系统已可靠实现”。它与 J07 的 2021 年 Agriculture 末端容差论文是两篇不同文章，不应混淆。

**基础控制合作者：建议保留的窄问题**

可供验证的题目方向：面向在树芽叶完整分级的预算约束观测决策——联合选择 ROI 补全与相机视点。

关键问题不是是否检测到了芽尖，而是当前观察是否包含足够信息，能够判断同一枝梢的一芽一叶/一芽两叶结构。先验证以下失败原因是否能被可靠区分，再决定是否发展为方法：

| 失败来源 | 可能有效的动作 | 必须验证的事实 |
|---|---|---|
| 同一原图中的芽叶结构被软件 ROI 切掉 | 扩大 ROI 或改变局部推理尺度 | 原始图像确实含有所需证据；扩大窗口收益足以抵消附加计算 |
| 关键叶片或叶基被其他叶片遮住 | 切换到具有实际位置变化的视点 | 新视点真正显露同梢结构，且没有把邻梢叶片错误归入 |
| 双目深度不可信 | 重采样、改变视点，或在足够的 RGB 证据下不用深度 | 深度质量指标能预测误差，替代动作确实改善最终决策 |
| 证据已足够或继续观察价值过低 | 停止分级，或输出无法可靠判定 | 停止规则在不同场景下校准，报告覆盖率而非只报告被接受样本准确率 |

以上是研究假设，不是已查明的空白。一般主动感知本来就允许多种观测动作，因此不能只把动作数量或代价函数加权求和当作创新。需要形成并验证茶芽结构的可观测性模型、失败原因识别机制，或确有必要的轻量求解方法。

机械合作者可负责可重复的相机位移机构、视点标定、回差与重复定位测量，以及移动后稳定等待时间。若目标是解除遮挡，应让相机光心产生横向或弧线位移；只在近似同一光心旋转的云台主要改变对准方向，不能期待产生足够视差来“看见叶片后面”。具体机构行程由真实芽叶尺寸和遮挡几何确定，不预设未经测量的毫米数。

**现代控制合作者：可发展但难度更高的窄问题**

可供验证的题目方向：具有 ROI 截断与间歇深度失效的茶芽相机对准中，感知计算调度与控制的协同设计。

必须先回答：同样的控制输入，在不同 ROI 尺度、检测频率和深度质量下，会怎样改变测量偏差、测量缺失及数据年龄？如果观测仅被建成固定方差噪声、固定时延，再接入常规 MPC，通常不足以区别 J08、J13、P02 等研究。

可考虑让调度器选择“何时运行昂贵检测、处理哪块区域、何时回到全图”，让控制器根据观测年龄和可靠性限制运动。方法贡献应落在可测量的耦合机制、相应的调度/估计/控制方法及适用条件，而不只是几个成熟模块的串接。

理论与实验主张要匹配实际机构：两轴云台对准不等于完整六自由度机器人定位；仅有录制视频回放不能证明物理闭环稳定性。对非刚性芽叶只能在明示的运动、误差和时延假设下讨论相应稳定或有界性质。实体指标至少包括对准误差、失跟率、重新捕获时间、任务完成时间和开发板计算开销。

J14 的全文尚未取得；在把“感知—运动协同设计”写为主创新前，必须补读其方法与实验，否则这个方向的查新仍有明确缺口。

**若扩展采摘，贡献类型需先分清**

若主张机械设计创新，应提供区别于 J07、P04 的具体结构，并比较相同视觉误差条件下的允许偏差区域、采摘成功率和损伤率。只有增加负压或柔性材料不足以说明改进。

若主张控制创新，可以采用已有末端，不必强行另造结构；但应实测该末端容差，并验证策略如何利用容差减少无效对准或额外观察。真实损伤率和采摘成功率需要真实芽叶与实体动作试验，不能由定位误差或仿真成功率替代。

**最小验证设计：让实验能够否定方案**

建议先做一批独立枝梢的预实验，按实际出现的截断、遮挡、深度失效和普通清晰情况分层记录；预实验数量不作为正式论文样本量保证。

| 比较项 | 回答的核心问题 |
|---|---|
| 完整画面、固定 ROI、启发式动态 ROI | 收益来自去背景/输入尺度，还是来自新的反馈机制？ |
| 单视点多帧、固定顺序视点、置信度阈值切换 | 相机运动是否比同等时间内的重复观察更有效？ |
| 信息增益或贝叶斯风险选视点＋停止 | 是否超过成熟主动分类策略，而不仅超过不移动相机？ |
| 相同观察策略下去掉结构证据模型 | 方法是否确实依赖芽叶特有的结构问题？ |
| 控制方向：周期检测、事件触发、常规视觉伺服/预测控制 | 新调度是否在同等资源下改善真实控制结果？ |
| RGB 单独、深度融合、质量门控深度 | 双目对这款相机、这类细芽叶是否有稳定的净收益？ |

所有比较应尽量固定检测骨干、训练数据与评价对象，测量相同总任务时间或报告精度—时间—覆盖率曲线。总时间包括运动、稳定、成像、传输、推理及重试。报告每次任务调用网络次数、实际输入尺寸和板端时间；把每个 ROI 都缩放到同样大小并运行同一网络，并不因原图裁剪更小就自动节省一次推理的主要计算量。

训练/测试按茶树、枝梢、采集批次分离；同一芽叶的相邻帧和不同视点不能跨集合。分级真值要由足够完整的观察确认，而不是让模型对看不见的叶片自证正确。允许拒判时，同时报告覆盖率、分级错误和拒判情况。

如果扩 ROI 已能解决大多数错误且明显便宜于移动，优先发展纯视觉计算策略；如果相机位移能暴露关键结构而通用置信度策略选不对动作，主动分级才具有更明确的研究依据；如果新策略在公平预算下不优于成熟基线，应先修改机制再定论文题目。

**可复核检索记录**

以下为已保存的 42 条原始检索式，保留引号及排除项。搜索引擎排序和索引会变化；这些记录可复查检索范围，不能保证重新查询得到完全相同结果。


1. `"tea" "dynamic ROI" sorting`

2. `"tea bud" "grading" "embedded"`

3. `"tea" "active vision" picking`

4. `"tea shoots" "binocular" localization`

5. `"tea" "multi-view" grading "classification"`

6. `"tea" "end effector" "tolerance"`

7. `"adaptive" "ROI" "edge" "object detection" feedback`

8. `"AdaZoom" "object detection"`

9. `"AutoFocus" "Efficient Multi-Scale Inference"`

10. `"AdaScale" "real-time video object detection"`

11. `"Remix" "object detection" high resolution`

12. `"dynamic" "cropping" "classification" "early"`

13. `"active vision" "classification" "view" "stopping"`

14. `"next best view" "fruit" "classification"`

15. `"active perception" "harvesting" "viewpoint" "occlusion"`

16. `"multi-view" "recognition" "view selection" "budget"`

17. `"event-triggered" "visual" "perception" "computation"`

18. `"visual servoing" "ROI" "delay"`

19. `"Dynamic visual servoing from sequential regions of interest" `

20. `"Closed-Loop Region of Interest Enabling High Spatial and" `

21. `"Nonmyopic View Planning for Active Object Classification and Pose Estimation" DOI`

22. `"AdaScale" site:proceedings.mlsys.org`

23. `"AutoFocus: Efficient Multi-Scale Inference" site:openaccess.thecvf.com`

24. `"Achieving Real-time Visual Tracking with Low-Cost Edge AI"`

25. `"visual servoing" "perception" "co-design" latency`

26. `"perception control" "adaptive" "resolution"`

27. `"Dynamic visual servoing" "2012" "10.1177"`

28. `"Closed-Loop Region of Interest" "10.1109"`

29. `"tea" "active" "grading" "view" -site:researchgate.net -site:facebook.com`

30. `"tea" "uncertainty" "grading" detection`

31. `"A real-time perception–motion codesign method" `

32. `"Closed-Loop Region of Interest" Chen Huang Rupp`

33. `"End-to-end policy learning for active visual categorization" DOI`

34. `"AdaZoom" "9786052" DOI`

35. `"tea" "classification" "next-best-view"`

36. `"tea" "ROI" "feedback"`

37. `"Closed-Loop Region of Interest" "feedback" site:ieeexplore.ieee.org`

38. `"Closed-Loop Region of Interest" "Abstract" site:dspace.mit.edu`

39. `"tea shoot" grading "active" viewpoint`

40. `"tea bud" grading topology keypoints graph occlusion`

41. `茶树 芽叶 分级 主动视觉 视点 ROI`

42. `"tea" "grading" "structural" keypoint leaf`
