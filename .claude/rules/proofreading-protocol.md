---
paths:
  - "thesis/**"
  - "analysis/**/*.R"
  - "quality_reports/**"
---

# Proofreading Agent Protocol (MANDATORY)

**Every thesis output MUST be reviewed before any commit or PR.**

**CRITICAL RULE: The agent must NEVER apply changes directly. It proposes all changes for review first.**

## What the Agent Checks

1. **Grammar** -- subject-verb agreement, missing articles, wrong prepositions (English); 语法错误（Chinese）
2. **Typos** -- misspellings, search-and-replace corruption, duplicated words
3. **Paragraph length** -- flag paragraphs exceeding 300 words; suggest splitting for readability
4. **Consistency** -- terminology matches `knowledge-base-template.md`, GB/T 7714-2015 citation format, Epi vs EPI disambiguation
5. **Academic quality** -- informal abbreviations, missing words, awkward phrasing, academic register
6. **Chinese punctuation** -- full-width punctuation in Chinese text (，。；：""）, half-width in English text (,.;:"")

## Three-Phase Workflow

### Phase 1: Review & Propose (NO EDITS)

Each agent:
1. Reads the entire output
2. Produces a **report** with every proposed change:
   - Location (chapter/section or line number)
   - Current text
   - Proposed fix
   - Category (grammar / typo / consistency / academic / punctuation)
3. Saves report to `quality_reports/reviews/`
4. **Does NOT modify any source files**

### Phase 2: Review & Approve

The user reviews the proposed changes:
- Accepts all, accepts selectively, or requests modifications
- **Only after explicit approval** does the agent proceed

### Phase 3: Apply Fixes

Apply only approved changes:
- Use Edit tool; use `replace_all: true` for issues with multiple instances
- Verify each edit succeeded
- Report completion summary
