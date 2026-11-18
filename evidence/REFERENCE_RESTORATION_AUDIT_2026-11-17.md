# Reference integrity and in-text integration audit (2026-11-18)

## Root cause and current resolved state
The historical 45-page manuscript contained 135 numbered references, and the older source bibliography retained 140 BibTeX records. A PDF-only reconstruction of the later V5 paper incorrectly reduced the active main manuscript bibliography to 66 cited entries. Previous bulk restoration produced 213 entries but placed many references only in a standalone Appendix D catalog. This gave the **appearance** of citation coverage without adequate grounding in the paper's main argument.

The revised `main.tex` now has **205 distinct cited reference keys**: 52 original V5 papers + 14 V5 supplementary primary-source locators + 139 retained contextual sources. Eight more peripheral context records were excluded instead of retained merely to exceed 200 references.

**Appendix D / Extended Literature Coverage has been removed** from the compiled manuscript. The obsolete `literature_coverage_2026.tex` catalog was deleted. All 139 contextual citations are now within the body via:
- `related_literature/agent_foundations.tex`: foundation-model agent architectures and coordination
- `related_literature/collaboration.tex`: communication, reasoning history, long-running environments
- `related_literature/runtime_ops.tex`: durable workflows, operations, protocols and deployment sources
- `related_literature/failure_attribution.tex`: localization, repair and online detection
- `related_literature/observability.tex`: provenance and process mining
- `related_literature/benchmark_context.tex`: reliability, environments, native labels
- `related_literature/safety_context.tex`: threat models and controls
- `related_literature/serving_context.tex`: attention kernels, scheduling, KV/cache and adapter serving

These blocks are included in corresponding Background, Diagnostics, Safety, Benchmark and Serving Infrastructure subsections. The extended sources are used to delimit hypotheses and provide architectural/thematic context, **not** to claim independent full-text verification of every source.

## Figure readability
The paper's original Figure 2, a **4-row by 6-column** diagnostic taxonomy, and Figure 3, a **12-row by 10-column** benchmark capability matrix, were redrawn in native LaTeX. They preserve the original row/column order, all cell categories and color semantics. Their wider landscape pages permit readable 9.5–10.5 pt text rather than unreadable scaled raster labels. PDFs now use searchable figure text. Source files are `figures/diagnostic_taxonomy_readable.tex` and `figures/benchmark_capability_readable.tex`.

## Audit and limits
The updated CI checks 205 unique bibliography keys, 205 cited keys and that no citation is left undefined or uncited; it also verifies the original matrices' LaTeX source inclusion and removal of Appendix D. The scientific claims in the 60-item core census continue to require paper-level primary source audit; citations alone are not validation. The 220-case retention experiment's raw predictions and the cache access/eviction event logs are not present in the supplied PDFs. Do not infer a quality score >=8/10 or experimental reproducibility solely from reference count.

The final root Overleaf document remains `main.tex`; use XeLaTeX, GitHub `main`, and pull the changes using Overleaf GitHub integration.
