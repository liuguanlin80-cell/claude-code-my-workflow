# CLAUDE.MD — 本科毕业论文项目（Claude Code 工作流）

**Project:** 本科毕业论文：XBP1 调控猪子宫内膜上皮细胞妊娠相关分子网络
**Institution:** 东北农业大学
**Branch:** main

---

## 你在做什么（项目一句话）

你正在撰写本科毕业论文，主题围绕 **围植入期（D09/D12）母胎界面单细胞分析 + 上皮细胞 XBP1 干扰的 bulk RNA-seq + 子宫内膜上皮类器官（EEOs）功能验证**。

---

## 核心原则（每次都遵守）

- **先计划（Plan-first）**：任何"多文件/不确定/需要做选择"的任务，先给计划（保存到 `quality_reports/plans/`），我等你一句"同意计划/继续"再执行。
- **可复现（Reproducible）**：所有结果必须能用脚本重跑得到（R 脚本、参数、版本、随机种子写清楚）。
- **证据优先（Evidence-first）**：论文中的每个结论必须能追溯到：图表/统计结果/原始数据/可靠文献（不允许编造引用）。
- **一次只改一类东西**：先把"分析/图"跑通再写结论；或先改"文字/结构"再统一润色。
- **质量门槛（Quality gates）**：低于 80/100 的输出不提交（commit）。

---

## 单一事实来源（Single source of truth）

- **论文正文（最终交付）**：`thesis/论文_word版.docx`（Claude 禁止直接编辑，由 Hook 保护）
- **分析与可复现产物**：`analysis/` 下的 R 脚本 + `figures/`、`tables/` 输出
- **参考文献**：`Bibliography_base.bib`
- **术语与写作共识**：`.claude/rules/knowledge-base-template.md`

---

## Word 输出约定

- 每段正文输出都标注：`[章节: X.X 标题]` + `[位置: 段落描述]`
- 纯文本格式（不用 Markdown），可直接粘贴到 Word
- 基因名用下划线标记（用户在 Word 中改为斜体）：`_XBP1_`
- 引用占位：`[AuthorYear]`，用户在 Word 中插入引文管理器引用
- 引用格式标准：GB/T 7714-2015（详见 `.claude/rules/citation-conventions.md`）
- 前 3 个 session 每完成关键阶段附加 `[同步摘要]` bullet 列表

---

## 目录结构

```
my-project/
├── CLAUDE.md
├── MEMORY.md
├── thesis/
│   └── 论文_word版.docx              # 最终版论文（Word）—— .gitignore
├── analysis/                          # R 脚本（01_.. 02_.. 递增编号）
│   ├── 01_scRNA_qc_clustering.R
│   ├── 02_scRNA_cellchat.R
│   ├── 03_bulk_deseq2.R
│   ├── 04_bulk_enrichment.R
│   ├── 05_eeo_rtqpcr.R
│   └── utils/                         # 共用函数（调色板、主题等）
├── data/                              # 原始/中间数据（大文件 gitignore）
│   ├── raw/
│   └── processed/
├── figures/                           # 脚本生成的图（禁止手工改图）
├── tables/                            # 脚本生成的表
├── refs/                              # 文献（bib/pdf）
├── quality_reports/
│   ├── plans/
│   ├── session_logs/
│   └── reviews/
└── explorations/                      # 试验区（低门槛，做完再迁移到 analysis/）
```

---

## 常用命令（Windows）

```bash
# 运行单个分析脚本
Rscript analysis/01_scRNA_qc_clustering.R

# 运行全部分析（按编号顺序）
for %f in (analysis\*.R) do Rscript "%f"
```

---

## 你的论文"固定信息"（以后别乱改）

### 研究对象与关键节点（写作/作图都统一用这些说法）
- 围植入期：D09（着床早期）与 D12（母体妊娠识别/互作增强）
- 单细胞：胚胎谱系（EPI/TE/PRE/IM），子宫内膜 8 类细胞（Stromal、Endothelial、Epithelium、Perivascular、T/NK/Macrophage/B）
- 上皮模型：猪子宫内膜原代上皮细胞（EECs）+ si-XBP1 干扰 + bulk RNA-seq
- 类器官：猪子宫内膜上皮类器官（EEOs），XBP1 抑制剂 STF083010；激素 E2/P4 处理；RT-qPCR/IF 等验证

### 统计与表述习惯（统一标准）
- 统计显著性：优先报告校正后 p 值（padj），并写清楚校正方法（默认 BH）。
- 火山图/差异分析：同时报告 **效应量（log2FC）** 与显著性（padj）。
- 图注必须包含：组别、n、方法、阈值、软件/包名、统计检验。

---

## 论文章节进度

| 章节 | 状态 | 核心内容 |
|------|------|----------|
| 摘要（中/英） | 待完善 | 研究目的/方法/结果/结论 |
| 1 文献综述 | 待润色 | UPR/XBP1、围植入期、类器官 |
| 2 材料与方法 | 待补充 | scRNA/bulk/EEOs 三套方法 |
| 3.1 单细胞结果 | 进行中 | UMAP/标记基因/CellChat |
| 3.2 bulk RNA-seq | 进行中 | DESeq2/富集/GSEA/PPI |
| 3.3 类器官验证 | 进行中 | STF083010/E2P4/RT-qPCR/IF |
| 4 讨论 | 待写 | 整合三部分 |
| 参考文献 | 待格式化 | GB/T 7714-2015 |

---

## 我怎么配合你（你只需要一句话指令）

你直接说：
- "帮我把 3.1 这段单细胞结果写成更像论文的段落，保留所有数字和结论"
- "把 bulk RNA-seq 的差异分析流程写成方法学（DESeq2/VST/PCA/火山图/阈值）"
- "把图 2（CellChat）图注写成中英双语、学术风格"

我会：先给你计划（如果需要）→ 执行 → 检查一致性与可复现性 → 给你可直接粘贴的结果。

---

## 任务清单（你可以随时让我更新）

- [ ] 摘要（中英文）与关键词补全
- [ ] 文献综述润色（UPR/XBP1 通路、围植入期调控、类器官模型）
- [ ] 方法学写完整：单细胞（Seurat/CellChat）、bulk（DESeq2/GSEA/STRING）、类器官（STF083010/E2/P4/RT-qPCR）
- [ ] 结果段落润色：每张图都做到"图注+正文互相匹配"
- [ ] 讨论：整合三部分实验结果，提出 XBP1 调控网络模型
- [ ] 参考文献按 GB/T 7714-2015 统一格式
- [ ] 致谢
