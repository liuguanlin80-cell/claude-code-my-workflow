---
name: devils-advocate
description: Challenge thesis chapter structure and argumentation with 5-7 specific questions. Checks evidence chains, over-interpretation, alternative explanations, terminology consistency, and cross-chapter coherence.
disable-model-invocation: true
argument-hint: "[chapter number, section description, or thesis overview]"
allowed-tools: ["Read", "Grep", "Glob"]
---

# Devil's Advocate Review

Critically examine thesis content and challenge its argumentation with 5-7 specific questions.

**Philosophy:** "We arrive at the best possible thesis through active dialogue."

---

## Setup

1. **Read the target content** (the chapter/section being challenged)
2. **Read the knowledge base** in `.claude/rules/knowledge-base-template.md` for terminology and structure
3. **Read adjacent chapters** for cross-chapter coherence

---

## Challenge Categories

Generate 5-7 challenges from these categories:

### 1. Evidence Chain Challenges
> "Is every claim in this section supported by a figure, statistic, or citation?"

### 2. Over-interpretation Challenges
> "Are conclusions proportional to the evidence? Is correlation stated as causation?"

### 3. Alternative Explanation Challenges
> "Could another mechanism explain the data? Is XBP1's role conclusively demonstrated?"

### 4. Terminology Consistency Challenges
> "Is Epi/EPI used correctly? Are D09/D12 consistent? Are group names explicit?"

### 5. Cross-chapter Coherence Challenges
> "Do sections 3.1 (scRNA), 3.2 (bulk), and 3.3 (EEOs) tell one integrated story about XBP1?"

### 6. Statistical Rigor Challenges
> "Are all statistical tests appropriate? Are thresholds justified? Is multiple testing corrected?"

### 7. Methodological Gap Challenges
> "Is there a missing control, an untested condition, or an unaddressed confound?"

---

## Output Format

```markdown
# Devil's Advocate: [Chapter/Section Title]

## Challenges

### Challenge 1: [Category] — [Short title]
**Question:** [The specific question]
**Why it matters:** [What could go wrong in defense/review]
**Suggested resolution:** [Specific action]
**Location:** [Chapter/section/figure affected]
**Severity:** [High / Medium / Low]

[Repeat for 5-7 challenges]

## Summary Verdict
**Strengths:** [2-3 things done well]
**Critical changes:** [0-2 changes before submission]
**Suggested improvements:** [2-3 nice-to-have changes]
```

---

## Principles

- **Be specific:** Reference exact chapters, figures, and statistics
- **Be constructive:** Every challenge has a suggested resolution
- **Be honest:** If the argument is solid, say so
- **Prioritize:** Factual errors > logic gaps > style
- **Think like the 答辩评审:** Where will they push back?
