---
name: validate-bib
description: Validate bibliography entries for completeness and GB/T 7714-2015 compliance. Check for missing fields, duplicate keys, and formatting issues.
disable-model-invocation: true
allowed-tools: ["Read", "Grep", "Glob"]
---

# Validate Bibliography

Validate all BibTeX entries for completeness, consistency, and GB/T 7714-2015 compliance.

## Steps

1. **Read the bibliography file** (`Bibliography_base.bib`) and extract all citation keys

2. **Check entry quality** for each bib entry:
   - Required fields present: author, title, year, journal/booktitle
   - Recommended fields: volume, number, pages, doi
   - Author field properly formatted (FAMILY NAME in caps, given name initials)
   - Year is reasonable (not future, not ancient)
   - No malformed characters or encoding issues
   - Key follows `AuthorYear_keyword` convention

3. **Check GB/T 7714-2015 compliance:**
   - Article type codes present: [J], [M], [D], [C], [P], [DB/OL]
   - Author format: up to 3 listed, 3+ use "et al" / "等"
   - DOI included when available

4. **Cross-reference with thesis content** (if available):
   - Scan `analysis/**/*.R` for citation comments
   - Check that tool citations exist (Seurat, CellChat, DESeq2, clusterProfiler, etc.)

5. **Report findings:**
   - List of entries with missing required fields (CRITICAL)
   - List of entries with missing recommended fields (MINOR)
   - List of duplicate or near-duplicate keys
   - List of formatting issues
   - List of recommended tool citations to add

## Bibliography location:
```
Bibliography_base.bib  (repo root)
```
