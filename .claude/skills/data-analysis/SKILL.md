---
name: data-analysis
description: End-to-end R data analysis workflow for thesis bioinformatics (scRNA-seq, bulk RNA-seq, organoid validation)
disable-model-invocation: true
argument-hint: "[analysis goal, e.g. 'volcano plot for si-XBP1 bulk RNA-seq' or 'CellChat analysis D09 vs D12']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
---

# Data Analysis Workflow

Run an end-to-end data analysis in R: load, explore, analyze, and produce publication-ready output.

**Input:** `$ARGUMENTS` — a description of the analysis goal or dataset path.

---

## Constraints

- **Follow R code conventions** in `.claude/rules/r-code-conventions.md`
- **Save all scripts** to `analysis/` with numbered names (01_xxx.R, 02_xxx.R)
- **Save all figure outputs** to `figures/` (naming: `fig_章节_序号_描述.pdf`)
- **Save all table outputs** to `tables/`
- **Use `saveRDS()`** for every computed object — downstream scripts may need them
- **Use project theme** (`theme_thesis`) and project color palette for all figures
- **Run r-reviewer** on the generated script before presenting results

---

## Workflow Phases

### Phase 1: Setup and Data Loading

1. Read `.claude/rules/r-code-conventions.md` for project standards
2. Create R script with proper header (title, author, purpose, inputs, outputs)
3. Load required packages at top (`library()`, never `require()`)
4. Set seed once at top: `set.seed(20260210)`
5. Load and inspect the dataset

### Phase 2: Exploratory Data Analysis

Generate diagnostic outputs:
- **Summary statistics:** dimensions, cell/sample counts, variable types
- **Quality control:** nFeature/nCount distributions, %MT, doublet scores (scRNA); PCA/sample correlation (bulk)
- **Group comparisons:** condition-specific summaries

Save all diagnostic figures to `figures/diagnostics/`.

### Phase 3: Main Analysis

Based on the research question:
- **scRNA-seq:** Seurat pipeline (QC, SCTransform, PCA, UMAP, clustering, marker genes)
- **Cell communication:** CellChat (create object, identify interactions, compare D09 vs D12)
- **Bulk RNA-seq:** DESeq2 (design formula, contrast, shrinkage, DEGs, volcano, MA)
- **Enrichment:** clusterProfiler (GO, KEGG, GSEA with specified universe and rank statistic)
- **PPI network:** STRING (export gene list for web tool or use STRINGdb package)
- **RT-qPCR:** delta-delta-Ct calculation, bar plots with error bars

### Phase 4: Publication-Ready Output

**Tables:**
- Use `writexl::write_xlsx()` for supplementary tables
- Use `knitr::kable()` for inline display
- Include: gene names, log2FC, padj, direction, annotation

**Figures:**
- Use `ggplot2` with `theme_thesis()` and project color palette
- Dimensions: 170mm width, 300 DPI, `units = "mm"`
- Output: PDF (primary, via `cairo_pdf`) and PNG (backup)
- Naming: `figures/fig_章节_序号_描述.pdf`
- Include proper axis labels (sentence case, units)

### Phase 5: Save and Review

1. `saveRDS()` for all key objects (Seurat objects, DESeq2 results, CellChat objects)
2. Create output directories with `dir.create(..., recursive = TRUE)`
3. Run the r-reviewer agent on the generated script:

```
Delegate to the r-reviewer agent:
"Review the script at analysis/[script_name].R"
```

4. Address any Critical or High issues from the review.

---

## Script Structure Template

```r
# ============================================================
# [Descriptive Title]
# Author: [from project context]
# Purpose: [What this script does]
# Inputs: [Data files]
# Outputs: [Figures, tables, RDS files]
# ============================================================

# 0. Setup ----
library(Seurat)        # or DESeq2, CellChat, etc.
library(tidyverse)
library(ggplot2)

set.seed(20260210)

source("analysis/utils/theme_thesis.R")  # project theme + palette

dir.create("figures", recursive = TRUE, showWarnings = FALSE)
dir.create("tables", recursive = TRUE, showWarnings = FALSE)

# 1. Data Loading ----

# 2. Quality Control ----

# 3. Main Analysis ----

# 4. Figures and Tables ----

# 5. Export ----
# saveRDS() for all objects, ggsave() for all figures
```

---

## Important

- **Reproduce, don't guess.** If the user specifies an analysis, run exactly that.
- **Show your work.** Print summary statistics before jumping to results.
- **Check for issues.** Missing genes, empty clusters, low cell counts.
- **Use relative paths.** All paths relative to repository root.
- **No hardcoded values.** Use variables for thresholds, gene lists, etc.
