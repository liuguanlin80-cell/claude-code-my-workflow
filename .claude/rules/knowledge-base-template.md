---
paths:
  - "thesis/**/*.docx"
  - "analysis/**/*.R"
  - "figures/**/*"
  - "tables/**/*"
  - "refs/**"
---

# Thesis Knowledge Base: XBP1 调控猪妊娠相关母胎界面分子网络（本科）

> 这份文件是"本项目的统一术语表 + 写作/分析共识"。
> Claude 在写段落、写图注、改方法、检查一致性时会先读它。

---

## 1) 术语与缩写（优先级：论文一致性）

### 生物学术语
| 缩写/术语 | 全称/中文 | 备注（使用规则） |
|---|---|---|
| D09 / D12 | 妊娠第 9 天 / 第 12 天 | 围植入期；正文/图注都用 D09、D12 这种格式 |
| TE | trophoblast（滋养层） | 单细胞胚胎谱系之一 |
| EPI | epiblast（上胚层） | 单细胞**胚胎**谱系之一 |
| PRE | primitive endoderm（原始内胚层） | 单细胞胚胎谱系之一 |
| IM | intermediate/transition（过渡态） | 单细胞胚胎谱系之一 |
| Epi / Epithelium | 子宫内膜上皮细胞 | **注意：与胚胎 EPI 不是一个东西** |
| EECs | 猪子宫内膜原代上皮细胞 | bulk RNA-seq 与 siRNA 模型 |
| EEOs | 猪子宫内膜上皮类器官 | STF083010、E2/P4 处理等实验 |
| UPR | 未折叠蛋白反应 (unfolded protein response) | XBP1 所属通路 |
| IRE1 | 肌醇需求酶 1 (inositol-requiring enzyme 1) | 剪切 XBP1 mRNA 的酶 |
| XBP1s | 剪切型 XBP1 (spliced XBP1) | 有活性的转录因子 |
| XBP1u | 未剪切型 XBP1 (unspliced XBP1) | 无活性形式 |
| ER stress | 内质网应激 | UPR 的触发条件 |
| STF083010 | IRE1 核酸内切酶抑制剂 | EEO 实验中使用；抑制 XBP1 剪切 |
| E2 | 雌二醇 (estradiol) | 类器官培养激素 |
| P4 | 孕酮 (progesterone) | 类器官培养激素 |

### 实验方法术语
| 缩写/术语 | 全称/中文 | 备注 |
|---|---|---|
| si-XBP1 | XBP1 小干扰 RNA | EECs 敲低实验 |
| si-Control | 阴性对照 siRNA | 对照组 |
| RT-qPCR | 实时荧光定量 PCR | 验证基因表达水平 |
| IF | 免疫荧光 (immunofluorescence) | 蛋白定位验证 |
| IHC | 免疫组化 (immunohistochemistry) | 组织切片蛋白检测 |

### 生物信息工具术语
| 缩写/术语 | 全称 | 备注 |
|---|---|---|
| Seurat | 单细胞分析包 | 关键步骤：SCTransform、PCA、UMAP、聚类 |
| CellChat | 细胞通讯推断工具 | 报告"communication probability"等术语时需解释含义 |
| DESeq2 | bulk RNA-seq 差异分析 | 默认 BH 校正；可对 log2FC 做 shrink |
| SCTransform | Seurat 归一化方法 | 替代 NormalizeData+ScaleData |
| VST | 方差稳定变换 (variance stabilizing transformation) | DESeq2 归一化方法 |
| DEGs | 差异表达基因 (differentially expressed genes) | padj<0.05, \|log2FC\|>1 |
| GSEA | 基因集富集分析 | 必须说明排序统计量与背景基因集（universe） |
| GO | 基因本体论 (Gene Ontology) | 功能富集分析 |
| KEGG | 京都基因与基因组百科全书 | 通路富集分析 |
| STRING | 蛋白互作网络数据库 | PPI 分析 |
| PPI | 蛋白-蛋白互作 (protein-protein interaction) | STRING 网络 |

---

## 2) Notation / 写法规范（统一格式）

| 规则 | 规范写法 | 示例 | 不要这样写 |
|---|---|---|---|
| 基因/蛋白区分 | 若写 mRNA：用基因名；若写蛋白：写"蛋白"或用大写+Protein | "XBP1 mRNA""XBP1 蛋白" | mRNA/蛋白混用不说明 |
| 组别命名 | Control / si-XBP1 / DMSO / STF083010 等 | "si-XBP1 vs Control（n=3）" | 只写"实验组/对照组"不清楚 |
| 显著性 | 优先写 padj，并说明 BH | "padj<0.05（BH）" | 只写 p<0.05 不说明校正 |
| 效应量 | 报告 log2FC（必要时说明 shrink） | "log2FC_shr" | 只给显著性不报效应量 |
| 时间点 | D09 / D12 / D0 / D4 / D6 | "D0-STF083010" | 9d/12d 这种不统一写法 |

---

## 3) 论文结构映射（你现在的论文长这样）

| 章节 | 核心问题 | 关键方法 | 关键产物 |
|---|---|---|---|
| 3.1 单细胞（母胎界面） | D09/D12 母胎界面细胞组成与互作 | Seurat + CellChat | UMAP、标记基因气泡图、TE–Epi 互作通路/配体受体 |
| 3.2 bulk RNA-seq（si-XBP1） | XBP1 敲低引发的转录重塑 | DESeq2 + 富集/GSEA + PPI | PCA、相关性、火山图、MA 图、GO/KEGG、GSEA、STRING 网络 |
| 3.3 类器官（EEOs）验证 | XBP1 对黏附/屏障等功能分子影响 | STF083010 + E2/P4 + RT-qPCR/IF/IHC | 形态学统计、RT-qPCR、免疫荧光/组化图 |

---

## 4) 统计阈值与报告规则（固定下来）

### 通用规则
| 项目 | 默认规则 |
|---|---|
| bulk 差异 | DESeq2；BH 校正；默认 padj<0.05, \|log2FC\|>1；同时报告 log2FC |
| 富集 | 说明背景基因集（universe）与排序统计量；避免"只贴图不解释" |
| 图注 | 必须写：n、统计检验、阈值、软件/包名、关键参数（如 SCT/UMAP） |
| 可复现 | 每张图对应一个脚本；脚本写清楚输入/输出路径与随机种子 |

### scRNA-seq 报告规范
- 报告：QC 前后总细胞数、nFeature/nCount 阈值、%MT 阈值
- 聚类：resolution 参数、聚类数、标记基因筛选条件（padj, log2FC, pct.1, pct.2）
- UMAP：使用的 PC 数、n_neighbors/min_dist（若非默认值）

### Bulk RNA-seq (DESeq2) 报告规范
- 报告：每组样本数 (n)、归一化方法（VST/rlog）、design formula
- DEGs：padj 阈值（默认 0.05, BH）、log2FC 阈值（默认 1）、shrinkage 方法
- 总是报告：DEG 总数、上调数、下调数

### RT-qPCR 报告规范
- 报告：内参基因、delta-delta-Ct 方法、生物学重复数、技术重复数
- 统计检验：Student's t-test 或 ANOVA（说明具体方法），误差棒 = SD 或 SEM（说明）
- 显著性标注：* p<0.05, ** p<0.01, *** p<0.001

### 图注检查清单
```
[ ] 简短描述性标题
[ ] 组别名称和样本量 (n)
[ ] 统计检验方法
[ ] 显著性阈值和校正方法
[ ] 软件/包及版本
[ ] 关键参数（resolution, thresholds 等）
```

---

## 5) 常见坑（提前规避）

### Anti-Patterns（不要这样做）
| 反例 | 后果 | 正确做法 |
|---|---|---|
| 图注不写 n/阈值/方法 | 审稿人/老师无法复核 | 图注补齐关键要素 |
| "显著上调/下调"但不给效应量 | 结论不可信 | 同时报告 log2FC 与 padj |
| 单细胞把 Epi 和 EPI 混写 | 读者误解 | 固定：Epi=子宫内膜上皮；EPI=胚胎上胚层 |
| 手工改图（PS/截图） | 不可复现 | 图必须由脚本生成并保存参数 |
| 引用未核实的文献 | 答辩被质疑 | 标注"[需核实]"让用户确认 |

### R Code Pitfalls
| Bug/坑 | 影响 | 修复 |
|---|---|---|
| SCTransform/归一化后又混用未归一化矩阵 | 结果不一致 | 明确使用哪个 assay/slot |
| 子集分析忘记重跑 PCA/UMAP | UMAP 不可信 | 子集后重新降维与聚类 |
| CellChat 输入对象/分组字段不一致 | 互作结果偏差 | 固定 meta 字段命名并写入脚本 |
| DESeq2 shrinkage 方法不一致 | log2FC 值不可比 | 全项目统一用 apeglm 或 ashr |
| ΔΔCt 计算忘记减参考基因 | fold change 错误 | 先减参考基因再减对照组 |
