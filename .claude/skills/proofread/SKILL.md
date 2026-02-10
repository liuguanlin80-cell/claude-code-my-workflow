---
name: proofread
description: Run the proofreading protocol on thesis content or R scripts. Checks grammar, typos, consistency, and academic quality. Produces a report without editing files.
disable-model-invocation: true
argument-hint: "[filename, chapter number, or 'all']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Task"]
---

# Proofread Thesis Content

Run the mandatory proofreading protocol. This produces a report of all issues found WITHOUT editing any source files.

## Steps

1. **Identify content to review:**
   - If `$ARGUMENTS` is a specific filename: review that file only
   - If `$ARGUMENTS` is a chapter number (e.g., "3.1"): review outputs for that chapter
   - If `$ARGUMENTS` is "all": review all content in `thesis/`, `analysis/`, and `quality_reports/`

2. **For each item, launch the proofreader agent** that checks for:

   **GRAMMAR:** Subject-verb agreement, articles, prepositions (English); 语法 (Chinese)
   **TYPOS:** Misspellings, search-and-replace artifacts, duplicated words
   **PARAGRAPH LENGTH:** Paragraphs exceeding 300 words
   **CONSISTENCY:** Terminology (knowledge-base-template.md), citation format (GB/T 7714-2015), Epi vs EPI
   **ACADEMIC QUALITY:** Informal language, missing words, awkward constructions
   **CHINESE PUNCTUATION:** Full-width in Chinese, half-width in English

3. **Produce a detailed report** listing every finding with:
   - Location (chapter/section or line number)
   - Current text (what's wrong)
   - Proposed fix (what it should be)
   - Category and severity

4. **Save each report** to `quality_reports/reviews/`

5. **IMPORTANT: Do NOT edit any source files.**
   Only produce the report. Fixes are applied separately after user review.

6. **Present summary** to the user:
   - Total issues found
   - Breakdown by category
   - Most critical issues highlighted
