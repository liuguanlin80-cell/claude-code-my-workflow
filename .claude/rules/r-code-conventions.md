---
paths:
  - "**/*.R"
  - "analysis/**/*.R"
  - "explorations/**/*.R"
---

# R Code Standards

**Standard:** Senior Principal Data Engineer + PhD researcher quality

---

## 1. Reproducibility

- `set.seed()` called ONCE at top (YYYYMMDD format)
- All packages loaded at top via `library()` (not `require()`)
- All paths relative to repository root
- `dir.create(..., recursive = TRUE)` for output directories

## 2. Function Design

- `snake_case` naming, verb-noun pattern
- Roxygen-style documentation
- Default parameters, no magic numbers
- Named return values (lists or tibbles)

## 3. Domain Correctness

- Seurat: verify QC thresholds documented, SCTransform assay used consistently, subset + re-PCA/UMAP done correctly
- DESeq2: verify design formula correct, contrast specified correctly, shrinkage method documented (apeglm/ashr/normal)
- CellChat: verify input object and grouping metadata field consistent across analyses
- RT-qPCR: verify delta-delta-Ct calculation correct, reference gene specified
- Check known package bugs (document below in Common Pitfalls)

## 4. Visual Identity

```r
# --- Thesis color palette (bioinformatics semantic colors) ---
col_d09        <- "#F39C12"   # warm orange (D09 timepoint)
col_d12        <- "#8E44AD"   # purple (D12 timepoint)
col_up         <- "#27AE60"   # green (upregulated / significant positive)
col_down       <- "#C0392B"   # red (downregulated / significant negative)
col_ns         <- "#95A5A6"   # gray (non-significant)
col_primary    <- "#2C3E50"   # dark blue-gray (main text/axes)
col_accent     <- "#3498DB"   # blue (secondary markers/highlights)
# Cell type colors: use Seurat::DiscretePalette(n, "polychrome")
```

### Custom Theme
```r
theme_thesis <- function(base_size = 12) {
  theme_minimal(base_size = base_size) +
    theme(
      plot.title = element_text(face = "bold", size = base_size + 2),
      axis.title = element_text(size = base_size),
      axis.text  = element_text(size = base_size - 1),
      legend.position = "bottom",
      panel.grid.minor = element_blank(),
      strip.text = element_text(face = "bold")
    )
}
```

### Figure Dimensions for Thesis (Word A4)
```r
# Single-column figure
ggsave(filepath, width = 170, height = 120, units = "mm", dpi = 300, device = cairo_pdf)
# Wide/heatmap figure
ggsave(filepath, width = 170, height = 200, units = "mm", dpi = 300, device = cairo_pdf)
```

## 5. RDS Data Pattern

**Heavy computations saved as RDS; downstream scripts load pre-computed data.**

```r
saveRDS(result, file.path(out_dir, "descriptive_name.rds"))
```

Missing saveRDS means analysis cannot be resumed without re-running expensive computations (e.g., Seurat SCTransform, DESeq2, CellChat).

## 6. Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Missing `units = "mm"` in ggsave | Wrong figure size | Always include `units = "mm", dpi = 300` |
| Hardcoded paths | Breaks on other machines | Use relative paths from repo root |
| Chinese characters garbled in PDF | Broken axis labels | Use `cairo_pdf` device or `showtext` package |
| SCTransform then mixing assays | Inconsistent results | Track which assay/slot is active |
| Subset without re-PCA/UMAP | UMAP unreliable | Always re-run dimensionality reduction after subset |
| CellChat metadata field mismatch | Wrong interaction results | Fix meta field naming in script |

## 7. Line Length & Mathematical Exceptions

**Standard:** Keep lines <= 100 characters.

**Exception: Mathematical Formulas** -- lines may exceed 100 chars **if and only if:**

1. Breaking the line would harm readability of the math (bioinformatics formulas, matrix ops, statistical calculations)
2. An inline comment explains the mathematical operation:
   ```r
   # Delta-delta-Ct: normalize to reference gene then to control group
   ddct <- (ct_target - ct_ref) - mean(ct_target_control - ct_ref_control)
   ```
3. The line is in a numerically intensive section (enrichment calculations, normalization routines)

**Quality Gate Impact:**
- Long lines in non-mathematical code: minor penalty (-1 to -2 per line)
- Long lines in documented mathematical sections: no penalty

## 8. Bioinformatics Object Naming Conventions

| Object type | Prefix | Example |
|-------------|--------|---------|
| Seurat object | `seu_` | `seu_d09`, `seu_endo`, `seu_merged` |
| DESeqDataSet | `dds_` | `dds_sixbp1` |
| DESeqResults | `res_` | `res_sixbp1_vs_ctrl` |
| CellChat object | `cc_` | `cc_d09`, `cc_d12` |
| clusterProfiler result | `enrich_` | `enrich_go_up`, `enrich_kegg_down` |
| GSEA result | `gsea_` | `gsea_hallmark` |

## 9. Code Quality Checklist

```
[ ] Packages at top via library()
[ ] set.seed() once at top
[ ] All paths relative
[ ] Functions documented (Roxygen)
[ ] Figures: 170mm width, 300 DPI, PDF via cairo_pdf
[ ] RDS: every computed object saved
[ ] Comments explain WHY not WHAT
[ ] Object naming follows Section 8 conventions
```
