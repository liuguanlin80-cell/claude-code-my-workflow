---
paths:
  - "analysis/**/*.R"
  - "thesis/**"
  - "figures/**"
  - "tables/**"
---

# Quality Gates & Scoring Rubrics

## Thresholds

- **80/100 = Commit** -- good enough to save
- **90/100 = PR** -- ready for review
- **95/100 = Excellence** -- aspirational

## Thesis Prose (Word output)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Factual error in results (number/conclusion wrong) | -100 |
| Critical | Citation fabricated (no real source) | -100 |
| Critical | Figure-text inconsistency (text says X, figure shows Y) | -20 |
| Major | Missing figure legend element (n/method/threshold) | -5 |
| Major | Terminology inconsistency (Epi vs EPI mix-up) | -3 |
| Major | Missing chapter location header in output | -3 |
| Minor | Awkward phrasing / non-academic register | -1 |
| Minor | Formatting inconsistency | -1 |

## R Scripts (.R)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Syntax errors | -100 |
| Critical | Domain-specific bugs (wrong assay, wrong contrast) | -30 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing set.seed() | -10 |
| Major | Missing figure generation | -5 |
| Major | Wrong figure dimensions (not 170mm/300DPI) | -5 |
| Minor | Long lines in non-mathematical code | -1 per line |

## Enforcement

- **Score < 80:** Block commit. List blocking issues.
- **Score < 90:** Allow commit, warn. List recommendations.
- User can override with justification.

## Quality Reports

Generated **only at merge time**. Use `templates/quality-report.md` for format.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md`.

## Tolerance Thresholds (Bioinformatics)

| Quantity | Tolerance | Rationale |
|----------|-----------|-----------|
| Cell counts (scRNA) | Exact | Integer, deterministic |
| DEG counts | Exact with fixed seed | Deterministic pipeline |
| padj values | < 1e-10 | Floating-point precision |
| log2FC values | < 0.001 | Numerical precision |
| UMAP coordinates | Visual similarity | Stochastic; set.seed required |
| RT-qPCR fold change | Report mean +/- SD | Biological variability |
