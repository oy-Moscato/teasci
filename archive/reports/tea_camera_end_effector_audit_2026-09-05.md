**相机与茶芽采摘末端结合：近距离局部视觉路线的重复风险补充审查**

日期：2026-09-05。已知资源：开发板、720p 双目深度相机；可定期接触真实茶树，可搭电动相机平台。假定相机型号、最小工作距离、开发板算力、末端结构和执行机构自由度尚未确定。本报告不把“能够搭建”写成“已经完成”。

**结论**

工程上值得做，但“相机装到末端、靠近目标、只看局部、远处粗定位后近处校正”已被已有研究覆盖，不能独立作为新颖性主张。本轮比此前一般 ROI 查新找到更直接的茶叶近邻：Sensors 2024 年的远近景分层定位，以及 2023 年公开的茶芽二次定位专利。跨领域还存在低分辨率双目相机与剪枝刀一体工作的实体研究。

能够稳定获得茶树样本和搭建电动平台，提升的是完成真实实验的可行性。是否达到 SCI 三区及以上，仍取决于具体方法或结构贡献、独立测试和目标期刊；本轮未使用 WoS 订阅库做入藏核验，也未核验年度中科院/JCR 分区。下列“期刊”是出版类型，不等于本次已经逐篇验证 SCIE 状态。会议、公开作者稿和专利单列。

本轮保留 24 条主题检索式，另做题名、摘要、正文与版本核验。核心保留 13 项文献/技术公开记录。不是完整领域文献计量，也不是论文文字相似度报告。

**最接近的证据**

等级：F＝已读到支持判断的正文段；A＝原始摘要；S＝出版商或作者来源检索片段；M＝题名/元数据，具体方法待读。不能由低等级证据推断未读过的算法细节。

| 编号 | 论文/技术公开 | 等级 | 重合与区别 |
|---|---|---|---|
| J01 | Yang et al. *Vision-Based Localization Method for Picking Points in Tea-Harvesting Robots*. Sensors, 2024, 24(21), 6777. DOI: 10.3390/s24216777。[出版商](https://www.mdpi.com/1424-8220/24/21/6777)；[原始摘要](https://pubmed.ncbi.nlm.nih.gov/39517674/) | A | 明确有远近景分层视觉伺服：远景识别茶芽 ROI，近景处理茶梗，再融合深度定位采摘点。是本方案首要茶叶基线。其定位结果不能等同于实体低损伤采摘成功率，也不能转移为用户相机精度。 |
| J02 | Barth, Hemming and van Henten. *Design of an eye-in-hand sensing and servo control framework for harvesting robotics in dense vegetation*. Biosystems Engineering, 2016, 146, 71–84. DOI: 10.1016/j.biosystemseng.2015.12.001。[作者机构记录与摘要](https://research.wur.nl/en/publications/design-of-an-eye-in-hand-sensing-and-servo-control-framework-for-/) | A | 密集植被中的末端相机、视觉反馈、轨迹修正和多视点已有框架。验证采用人工甜椒植被的实验室定性试验；可以与真实茶树条件区分，但不能再宣称首创眼在手上农业闭环。 |
| J03 | Liang et al. *Palm vision and servo control strategy of tomato picking robot based on global positioning*. Computers and Electronics in Agriculture, 2025, 237, 110668. DOI: 10.1016/j.compag.2025.110668。[出版商](https://www.sciencedirect.com/science/article/abs/pii/S0168169925007744) | S | 掌心视觉、全局定位与视觉伺服构成直接邻近架构。原始索引涉及全局相机和掌心相机；本次全文访问受限，不据此填写未核验的控制算法、成功率或精度。 |
| J04 | Chen et al. *Dynamic visual servo control methods for continuous operation of a fruit harvesting robot working throughout an orchard*. Computers and Electronics in Agriculture, 2024, 219, 108774. DOI: 10.1016/j.compag.2024.108774。[出版商](https://www.sciencedirect.com/science/article/abs/pii/S0168169924001650) | S | 动态视觉伺服与连续采摘操作已有系统研究。只把观察、移动、采摘串成连续流程不足以形成新框架；具体动态控制律仍需全文对比。 |
| J05 | Kan et al. *A Progressive Hybrid Automatic Switching Visual Servoing Method for Apple-Picking Robots*. Agriculture, 2026, 16(5), 620. DOI: 10.3390/agriculture16050620。[出版商](https://www.mdpi.com/2077-0472/16/5/620) | S | 已有基于深度切换的混合视觉伺服。仅提出“远近阶段切换控制器”风险高；切换阈值必须有新的任务或误差依据。 |
| J06 | Li et al. *Development and field evaluation of a robotic harvesting system for plucking high-quality tea*. Computers and Electronics in Agriculture, 2023, 206, 107659. DOI: 10.1016/j.compag.2023.107659。[出版商](https://www.sciencedirect.com/science/article/pii/S0168169923000479) | M/S | 真实茶叶采摘系统与实地验证的直接领域参照。此次未取得全文，不能因其参考文献出现 eye-in-hand 就认定自身一定采用同样配置。 |
| J07 | He et al. *Localization of Tea Shoots for Robotic Plucking Using Binocular Stereo Vision*. Journal of Field Robotics, 2025. DOI: 10.1002/rob.22559。[原始摘要](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22559) | A，本轮沿用前次已核对来源 | 茶梢双目分割、匹配、三角测量与采摘点定位已有。换成低分辨率相机不能单独成为算法创新。 |
| J08 | Wang et al. *Automated tea shoot picking using the YOLO network and Mamba images segmentation for top-view detection with a monocular camera*. Journal of Agricultural Engineering，2025 年在线、2026 年卷期。DOI: 10.4081/jae.2025.1637。[原始摘要](https://www.agroengineering.org/jae/article/view/1637) | A，本轮沿用前次已核对来源 | 已采用茶梢检测、裁剪、分割及红外反馈驱动末端的方案。单目顶视可作为减少不可靠深度依赖的对照；模拟茶园实验不能直接推广为自然茶园表现。 |
| J09 | Zhu et al. *Deviation Tolerance Performance Evaluation and Experiment of Picking End Effector for Famous Tea*. Agriculture, 2021, 11(2), 128. DOI: 10.3390/agriculture11020128。[出版商](https://www.mdpi.com/2077-0472/11/2/128) | S，本轮沿用前次已核对来源 | 负压引导末端与偏差容忍评价已有直接研究。需比较具体结构或新的误差利用机制，不能把“容差大”作为未经比较的创新。 |
| J10 | Huang et al. *Towards autonomous premium tea harvesting: A high-efficiency and high-quality path planning based on optimized IABFMT* algorithm in unstructured canopies*. Smart Agricultural Technology, 2025, 12。[出版商](https://www.sciencedirect.com/science/article/pii/S2772375525005489)；[作者机构发表记录](https://jdgcxy.ncu.edu.cn/English/Faculty/MastersSupervisor/c1c991eabff947ffbe272d4813399d3b.htm) | S | 检索片段涉及机械臂运动中的近距离相机点云，主线为路径规划。本轮未取得正文，保留为后续精读项；不据题名声称其已实现本项目全部视觉反馈与剪切功能。 |
| C01 | Cuevas-Velasquez et al. *Real-time Stereo Visual Servoing for Rose Pruning with Robotic Arm*. ICRA, 2020, 7050–7056. DOI: 10.1109/ICRA40945.2020.9197272。[作者全文](https://homepages.inf.ed.ac.uk/rbf/PAPERS/HCICRA20.pdf)；[机构出版记录](https://research.wur.nl/en/publications/real-time-stereo-visual-servoing-for-rose-pruning-with-robotic-ar/) | F，会议论文 | 末端双目相机＋细枝剪切＋实时位置更新。正文相机为 752×480，近距使用约 3 cm 基线，刀具布局考虑切割动作与视野。已明显接近“低像素、近距离、局部看准”。其按高度剪枝与茶芽采摘等级、嫩梗损伤要求不同。 |
| P01 | Kim, Silwal and Kantor. *Autonomous Robotic Pepper Harvesting: Imitation Learning in Unstructured Agricultural Environments*. arXiv:2411.09929，2024。[作者公开全文](https://arxiv.org/html/2411.09929v1) | F，按公开稿记录，未确认后续期刊版本 | 剪夹机构集成鱼眼相机，位置安排考虑采后果实和机构状态可见性。相机与刀具整合及可见性安排已有相邻研究；其模仿学习方法与用户计划不同。 |
| T01 | 《一种用于名优茶嫩芽采摘的二次定位方法》。CN116138036A，2023-05-23 公开；CN116138036B，2024-04-02 授权公告。[A 文本](https://patents.google.com/patent/CN116138036A/zh)；[B 文本](https://patents.google.com/patent/CN116138036B/zh) | F；多次复定位条款主要由原始记录的检索索引核对 | 固定相机与末端相机分别执行初定位和二次定位，采摘点与角度进行坐标转换。B 文本检索索引还明确包含多次二次定位和误差门限。属于技术公开，不能当作期刊实验性能证据；这里仅作方法重复审查，不作法律状态或实施权利判断。 |

**关键判断：哪些主张已经不够**

| 主张 | 判断 |
|---|---|
| 相机固定到末端，靠近目标观察 | J02、C01 已直接覆盖基础架构 |
| 低分辨率相机也能靠近看准 | C01 使用比 720p 更低的图像分辨率，不能用像素数单独区分 |
| 远景检测芽叶，近景定位茶梗 | J01 已有同领域直接研究 |
| 固定相机粗定位，末端相机二次校正 | T01 已有直接茶芽技术公开，J03 有果实邻近方案 |
| 不重建整个植物，只观察局部 | 已有局部感知/视觉伺服路线；应具体说明省掉哪些处理及其代价 |
| 误差小于阈值后执行剪切 | 普通阈值终止已有；需与实测低损伤范围及动作期间不确定性结合并比较 |
| 更换相机位置、补光、加 ROI、加 PID/MPC | 都可能是有用实现，但每项本身不能保证形成独立创新 |

C01 摘要强调不必预先完整扫描整个植物，但正文仍有预设局部扫描和点云融合步骤。因此准确比较应是“无需完整外围重建”，不能误写成“完全没有扫描或点云”。J01 摘要描述分层视觉伺服，但本轮未逐项核对其闭环频率及是否连续控制，不能把摘要术语等同于高频连续反馈。

**对“机械相对误差小、近距离看得准”的技术审查**

相机与固定刀座刚性连接，可使二者的几何关系相对稳定。这个关系必须经标定和重复试验测量，不能假设为零误差。通过目标相对末端的视觉反馈，可以补偿一部分机器人绝对定位偏差；刀口装配偏差、支架受载变形、回差、刀具开合引起的运动以及枝梢摆动仍然存在。

相机若安装在会开合或明显变形的夹指上，相机—刀口关系可能随动作变化；若相机单独在电动滑台上移动而刀具不动，也不能直接沿用固定相机—刀具变换。电动平台应明确移动的是整个刚性组件，还是相机与刀具两个独立部件。

靠近通常增加目标的像素占比，但三维定位不保证随距离缩短持续变好。最小对焦距离、景深、双目有效重叠视场、有效视差范围、细梗纹理、运动模糊和自身遮挡都可能成为限制。720p 本身不能推出毫米精度或最小可用距离。二维图像居中也不等于沿深度方向已到正确剪切平面。

“看准而不看全”适合已经选定目标后的末端执行阶段；完整等级判断仍需要足够的同梢结构证据。可先用同一相机在较远处选定目标，再移动到近处。若用人工指定目标启动终端实验，应把终端成功率与整套自动选芽采摘成功率分开报告。

**仍值得验证的两种贡献路径**

路径 A，机械设计与基础控制：围绕同一待采目标，联合确定相机、固定刀座及导向结构的布局，使目标更长时间同时满足“可观察、可进入刀口、可低损伤切断”。

可做的具体设计变量包括相机相对固定刀座的偏置与角度、相机到剪切平面的距离、导向入口形状、刀片开启位置及遮挡轮廓。可制作可调试验件，例如固定刀座侧面的观察开口或偏置相机安装位，让茶梗与工具参照在关键接近阶段可见。是否采用导向槽要由实测决定：它可能改善入槽，也可能推动或损伤嫩梗。这里只提出待试验的结构候选，不声称这些单个形式前所未有。

机械贡献要落实为相对既有布局的具体改动及有效范围的扩大。只优化支架安装角度、再报告检测准确率提升，通常不足以证明完整的采摘结构贡献。

路径 B，现代控制：围绕最后接近到刀片闭合的阶段，处理近距深度掉失、刀具自遮挡、信息时延和枝梢运动的耦合。可研究何时继续观察、何时换一个小视点、何时已有足够把握执行，以及动作后如何验证是否采到。

切断准入条件应联系实测末端低损伤范围和闭合期间的目标位移。一般“置信度大于阈值”和“定位误差低于阈值”不是新控制理论。新方法必须说明在怎样的误差、时延与植物运动条件下有效，并优于普通二次定位与连续视觉伺服。如果控制器只调整两个平移方向，就只报告该任务所覆盖的自由度，不能推论完整六自由度定位能力。

两条路径可以共用实验台，但第一篇应明确主贡献。按当前硬件约束，建议先评估路径 A 所需的可观察与可剪切范围，再由失败数据决定是否投入路径 B。

**首轮决定去留的实验**

| 实验 | 变量与方法 | 独立评价 |
|---|---|---|
| 相机—刀口几何稳定性 | 不同位置、接近方向、刀片状态；重复定位；负载前后 | 独立刻度夹具或参考测量确定相机—剪切平面的误差与漂移 |
| 接近距离扫描 | 从可用远端逐步靠近实际茶芽；比较几个相机安装偏置 | 茶梗像素宽度、深度有效率、定位误差、刀口/目标可见性；找出可用区间 |
| 不切断的对准 | 在代表性枝梢前执行接近、停下、退出，加入可重复初始偏差 | 对准误差、失跟、误切换目标、任务时间，不能只用检测置信度自证精度 |
| 低损伤容差测量 | 对独立真实茶芽施加受控横向/纵向偏差及角度差后剪切 | 完整采下率、错误剪切、芽叶/母枝损伤；建立结构对应的允许范围 |
| 实体闭环比较 | 相同模型、相机、末端和任务预算，比较一次定位、近距二次定位、连续局部视觉伺服、提出的方法 | 所有启动任务的成功率、拒绝/超时率、动作次数、耗时和板端资源 |
| 结构与控制分离比较 | 基准结构/新结构 × 基准控制/新控制 | 区分性能来自相机靠近、结构改动还是控制方法，避免只与最弱方案比较 |

同一枝梢可以反复进行非破坏性对准调试，但只算一个独立生物对象；真实采摘具有破坏性，应对相似枝梢分组并随机安排方法。按植株与日期划分调参和最终测试，保留自然遮挡与运动样本。手动扶叶、去遮挡等操作如果使用，应单独说明，不与原始自然条件混合计算。

评估相机安装改动时，尽可能保持相同工作距离或将距离作为独立变量，否则不能区分布局收益与目标单纯放大的收益。计时从任务启动到结束，包含移动、稳定、推理、复核、剪切和重试。若允许放弃困难目标，同时报告覆盖率；不能只对完成剪切的样本计算成功率。

**建议的题目边界**

可供预实验检验的题目：面向茶芽低损伤采摘的相机—刀具布局与局部视觉反馈方法。

这个题目只是限定研究范围，尚不是已经成立的创新结论。只有当试验证明某个具体结构或控制机制，在相同资源下扩大可靠剪切范围或降低损伤，才适合把贡献写进摘要。若最终仅证明将相机靠近能改善定位，应将其作为平台验证，继续寻找主贡献。

若相机近距离无法可靠成像或提供深度，可先采用可靠工作距离＋较长工具前伸量，并实测由此增加的几何/挠度误差；是否使用单目局部几何或额外传感器，应由数据决定，不能预设 720p 双目一定适合刀口附近。

**本轮保留的主题检索式**

下面列出 24 条主题/题名检索式；另有针对 DOI、原始摘要及具体方法段的核验检索。搜索索引和排序会变化，记录供复查范围。

1. `"tea picking" "eye-in-hand"`

2. `"tea" "camera" "end-effector" "visual servoing"`

3. `"tea harvesting" "close-range" camera`

4. `"tea" "eye in hand" camera harvesting`

5. `"harvesting" "wrist-mounted" camera "visual servoing"`

6. `"fruit picking" "coarse-to-fine" "eye-in-hand"`

7. `"Towards autonomous premium tea harvesting"`

8. `"Vision-Based Localization Method for Picking Points in Tea-Harvesting Robots"`

9. `"Development and field evaluation of a robotic harvesting system for" tea`

10. `"Design of an eye-in-hand sensing and servo control framework" site:research.wur.nl`

11. `"Dynamic visual servo control methods for continuous" harvesting`

12. `采茶 机器人 末端 相机 手眼 近距离 二次 定位`

13. `"Vision-Based Localization Method for Picking Points" PMC`

14. `"Towards autonomous premium tea harvesting" camera wrist`

15. `"harvesting" "camera" "gripper" "occlusion" "peduncle" visual servo`

16. `"eye-in-hand" "tea" "secondary" localization`

17. `"tea picking" "camera" "integrated" end effector`

18. `"harvesting" "end-effector" "camera placement" visibility`

19. `"Palm vision and servo control strategy of tomato picking" `

20. `"A Progressive Hybrid Automatic Switching Visual Servoing" `

21. `"Vision-Based Localization" "6777" "Abstract"`

22. `"Real-Time Constrained Visual Servoing for Agricultural" `

23. `"robot" "harvesting" "camera" "capture region" tolerance`

24. `"harvesting" "gripper" "blind" "visual servoing"`

