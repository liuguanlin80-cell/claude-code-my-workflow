---
paths:
  - "thesis/**"
  - "analysis/**/*.R"
  - "figures/**"
  - "tables/**"
---

# Task Completion Verification Protocol

**At the end of EVERY task, Claude MUST verify the output works correctly.** This is non-negotiable.

## For R Scripts:
1. Run `Rscript analysis/filename.R`
2. Verify output files (PDF, PNG, RDS) were created with non-zero size
3. Spot-check results for reasonable magnitude
4. If `set.seed()` is used, re-run and confirm identical outputs
5. Verify figure dimensions match style guide (170mm width, 300 DPI)

## For Figures:
1. Verify file exists in `figures/` with correct naming convention (`fig_章节_序号_描述.pdf`)
2. Verify dimensions: 170mm width for single-column
3. Verify DPI: 300 for PNG
4. Verify text legibility (axis labels, legends not cut off)
5. Verify color palette matches project conventions

## For Thesis Prose (Word-pasteable output):
1. Verify output includes `[章节: X.X 标题]` location header
2. Verify all statistical values match script outputs
3. Verify terminology matches knowledge-base-template.md
4. Verify figure/table cross-references use correct numbering
5. Verify citation placeholders use `[AuthorYear]` format
6. Verify plain text format (no Markdown)

## For Bibliography:
1. Verify BibTeX entries have all required fields (author, title, journal, year, volume, pages)
2. Verify key naming follows `AuthorYear_keyword` convention
3. Verify no duplicate keys

## Common Pitfalls:
- **Chinese characters in PDF:** Use `cairo_pdf` device or `showtext` package
- **Figure dimensions:** Verify they match Word thesis margins (A4, ~170mm text width)
- **Assuming success:** Always verify output files exist AND contain correct content
- **Stale RDS files:** If analysis parameters changed, re-run from scratch

## Verification Checklist:
```
[ ] Output file created successfully
[ ] No errors during execution
[ ] Results are scientifically reasonable
[ ] Figures display correctly with correct dimensions
[ ] Terminology is consistent with knowledge base
[ ] Reported results to user
```
