# Restored and Expanded Bibliography: Auditable Record (2026-11-17)

## Why the bibliography shrank
The author-supplied original 45-page PDF, `Frontier_of_CS___Diagnostics_and_Infrastructure_for_Multi_Agent_Systems__Copy_-2.pdf`, has **135** numbered references ([1]–[135]). The retained historical repository bibliography `FCS LaTeX Template(1)/references.bib` has **140** BibTeX records (not necessarily the identical 135-item snapshot). The reconstructed V5 root `main.tex` instead used an **inline `thebibliography` of 66** entries. Since that file did not include the original .bib, the shrinkage was a reconstruction regression, **not** an evidence-based 135→66 literature exclusion.

## Revision
- Preserved the V5 root manuscript's **66** existing entries and their citation keys.
- Recovered and integrated **147** distinct additional references from (i) the historical author's .bib, (ii) publicly accessible thematic multi-agent literature bibliographies, and (iii) a small set of publisher/author primary records for serving mechanisms.
- **Current total = 213 unique bibliography keys**; every one has at least one `\cite` in the main text or the explicitly marked literature coverage appendix. No undefined `\cite` keys.
- New sources are in `bibliography_restored_2026.tex`. The categorized and individually cited crosswalk is `literature_coverage_2026.tex`, included by root `main.tex`.
- Eliminated five duplicated primary-paper records identified through arXiv identifier comparison (four overlapping with the original V5 list, one between the historical and public supplemental lists). Title- and source-based deduplication was performed as well.
- Excluded 17 candidate records whose subject matter was too peripheral to the runtime diagnostics and serving review; excluded nine more that did not expose an immediate DOI/arXiv/official source locator in the available bibliography metadata. This was not a declaration that such work is invalid.
- The source PDF remains the authority for original V5 empirical results. No numerical experiment was invented or changed by the bibliography restoration.

## How this supports (and does not overstate) evidence rigor
**Two scopes must remain separate.**
1. The **core 60 table entries** (48 non-benchmark methods/systems/standards + 12 evaluation benchmarks) are the focus of the original V5 evidence-tier taxonomy, controlled comparisons, DRICE analysis and author-reported ablations.
2. The **213-item bibliography** includes broader contextual source coverage: foundational agent frameworks and interaction environments, agent benchmarks, safety/security, operational observability, cache systems and relevant technical specifications.

An entry in the 213-item bibliography **does not imply** that its full text was independently audited or that it should be promoted to T1. The appended source map is explicitly bibliographic/contextual; it is not evidence of a completed 213-paper primary-text audit. Several rows are preprints or official documentation rather than peer-reviewed research articles; publication type and original landing pages still require final author-side verification.

This revision fixes a real breadth and citation-regression defect and adds source provenance. It does **not**, on its own, establish a scientific-evidence score of 8/10, nor can it replace the missing case-level predictions, cache event logs or complete reproduction code.

## Editorial and Overleaf checks
- Root `main.tex` is the current Neurocomputing source; use XeLaTeX.
- In Overleaf, GitHub integration pull of the updated `main` branch is required; the GitHub push is not an automatic Overleaf sync.
- The root references are retained as `\bibitem{v5ref...}` and `\bibitem{v5supp...}`; `bibliography_restored_2026.tex` is input **inside** the same `thebibliography` environment. This avoids duplicate bibliography environments or broken numeric cross-references.
- CI validates all thirteen tables, moved Figure C.1 / original Figure 1 and figures 3–4, and counts all 213 uniquely keyed and cited references.

## Source classes
The 147 supplementary records include: diagnostics/tracing/attribution (16), evaluation/reliability (21), agent systems/collaboration (72), safety/security/governance (23), and LLM serving/cache infrastructure (15). Counts represent thematic bibliographic roles, not exclusive methodology or evidence tiers.

## Important next scientific audit
Before calling the full evidence claims journal-ready, verify the specific sections/tables supporting each T1 numerical result; resolve four T2 entries with fine-grained manuscript descriptions; reproduce the McNemar analysis from 220 case-level predictions and the cache experiment from access/eviction event logs. These gaps cannot be closed by increasing reference count alone.
