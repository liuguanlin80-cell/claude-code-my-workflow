# Project Memory

Corrections and learned facts that persist across sessions.
When a mistake is corrected, append a `[LEARN:category]` entry below.

---

<!-- Append new entries below. Most recent at bottom. -->

[LEARN:terminology] Epi = 子宫内膜上皮细胞 (endometrial epithelium); EPI = 胚胎上胚层 (epiblast). NEVER mix these up. Context: single-cell analysis has both cell types.

[LEARN:platform] This project runs on Windows. Use Python hooks (.py), not shell scripts (.sh). Use `Rscript` for R execution, `python` (not python3) for Python.

[LEARN:output] The thesis is in Word format (thesis/论文_word版.docx). All prose output must be plain text with `[章节: X.X 标题]` location headers, formatted for direct paste into Word. No Markdown formatting in thesis outputs.

[LEARN:statistics] Default differential expression thresholds: padj < 0.05 (BH correction), |log2FC| > 1. Always report both padj AND log2FC together.

[LEARN:figures] Figure dimensions for thesis: 170mm width, 300 DPI, PDF primary format via cairo_pdf. Naming: figures/fig_章节_序号_描述.pdf

[LEARN:citation] Citation format: GB/T 7714-2015 (Chinese national standard). Sequential numbered [1], [2,3], [4-7]. In Claude outputs use [AuthorYear] placeholders.

[LEARN:timepoints] Pregnancy timepoints: D09 (early implantation), D12 (maternal recognition of pregnancy / enhanced interaction). Always write D09/D12, never 9d/12d.

[LEARN:models] Three experimental systems: (1) scRNA-seq of D09/D12 conceptus + endometrium, (2) si-XBP1 in primary EECs + bulk RNA-seq, (3) EEOs + STF083010/E2/P4 + RT-qPCR/IF.

[LEARN:colorpalette] Project palette: D09=#F39C12(暖橙), D12=#8E44AD(紫), up=#27AE60(绿), down=#C0392B(红), ns=#95A5A6(灰). Cell types use Seurat::DiscretePalette(n,"polychrome").
