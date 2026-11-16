# V5 PDF → Overleaf source content audit (2026-11-15)

**The final working manuscript is root `main.tex`.** Do NOT set `v5_experimental_reconciliation.tex` (staging file) or `FCS LaTeX Template(1)/template.tex` (historical manuscript) as Overleaf Main document.

## Compiler repaired
The root `latexmkrc` config forces XeLaTeX even when the build runner requests `latexmk -pdf`. This addresses the Overleaf screenshot's fatal `fontspec requires XeTeX or LuaTeX` error. Set Overleaf Menu > Compiler > XeLaTeX as well and select "Recompile from scratch" to clear old BibTeX aux warnings.

## Baseline and integrity
The sole authoritative reference is the uploaded 56-page V5 PDF, SHA-256:
`e9fb0297c5e8c0f472214eb5672ae7543bf51f093c6544c7d005b807c82f149c`.

With the latest source fixes, local XeLaTeX output has 64 pages because of differences in paragraph flow, tables, fonts, and figure float positions. It is **not** visually identical to the source PDF.

**Changes made after the content audit:**
- Restored p.33, §6.2: all three events `N_i(T)`, `D_i(T)`, `R_i(T)`; full Eq.(1) `L_i(T)=N_i(T)∧D_i(T)∧¬R_i(T)`; and the difference between lost data and recoverable compute cost.
- Restored missing school/department names in all author affiliations.
- Restored Figure 1–3 descriptions and detailed Table 6–10 caption definitions, including denominators for the cache simulation metrics and warm-up.
- Preserved the original Table 11 source-reported 95% CI **as unverified evidence**, while identifying the correct exact two-sided McNemar test and correcting the reversed discordant pair directions. The original PDF labels the exact-test p values `mid-p`, which is inconsistent with their values.
- Kept **all 13 editable tables**, 60 core census entries, original 52 bibliography items, supplemental metadata, 4 figure assets and the complete DRICE discussion.

## What the audit actually establishes
A normalized textual check examined **320 original PDF text blocks** across all 56 pages, comparing to the compiled manuscript. **273/320 blocks** match at >=95% fuzzy similarity. The remaining **47** include table captions, table rows, figure labels, author metadata, and deliberately changed interpretations. The multiset word-token overlap is about **94.37%**, not a proof of complete word-for-word identity.

Individual comparison rows are in [PDF_TO_TEX_TEXT_BLOCK_AUDIT_2026-11-15.csv](./PDF_TO_TEX_TEXT_BLOCK_AUDIT_2026-11-15.csv).

Intentional scientific corrections that cannot be counted as verbatim identity:
1. Figure 4 and Table 3: benchmark *native* step/agent cause labels are separated from final task success and safety evaluation; tau-bench's final goal-state scoring is not native step root-cause ground truth.
2. Table 11: discordant pairs and exact/mid-p method labeling are corrected. The unverified source CI is explicitly retained and identified.

## Important limits
**Do not claim 100% literal preservation or 8/10 independently validated evidence rigor** from these checks alone. The provided PDF lacks raw 220-case predictions, cache hit/eviction event logs, runnable full evaluation scripts, and full original-papers evidence matrix. Content equivalence and primary scientific verification are different tests.

**GitHub push does not itself pull into Overleaf.** Use Overleaf GitHub integration to pull the updated `main` branch, set root `main.tex` as Main document, then recompile with XeLaTeX.
