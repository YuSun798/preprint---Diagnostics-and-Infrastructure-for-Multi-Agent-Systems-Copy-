# Evidence audit and remaining submission checks (Neurocomputing revision)

Revision freeze: 2026-11-07. Original manuscript was curated iteratively. Search strings, exclusions and retrieval dates were not logged; no systematic/PRISMA claim is made.

## Evidence-tier limitations
- Original Tier 1a/1b classification: FAMAS, TrajAudit, Agent Traces, TraceElephant, ScaleSim, G-Safeguard, ShieldAgent, and AgenTracer (eight papers across nine table entries including RootSE). Prior author-reported full-text reviews were not all independently reaudited in this edit.
- Tier 2 = abstract-level evidence. Serving-table workload assumptions and limitations are provisional mechanism-based hypotheses, not verified internal implementation statements.
- Tier 3 = standards, vendor material or documentation.

## Full-text priority list (outstanding before submission)
For every study record version/DOI, access date, supporting section/page/table, precise state object, workload, experimental baselines, overhead units, and whether a shared diagnostics-serving budget is explicitly defined. An abstract cannot prove nonexistence.

| Priority | Papers | Question / source-location task | Status |
|---|---|---|---|
| P0 | ScaleSim | Record exact state movement and persistence (original Tier 1a, recheck page) | Open |
| P0 | Continuum | TTL eviction vs persisted logs and exact restoration behavior | Open |
| P0 | KVFlow, KVCOMM | Cache alignment, divergent prefixes, portability | Open |
| P0 | TokenCake, TOPAS | Agent workload assumptions and quantitative baseline locations | Open |
| P0 | Parrot, InferCept, Preble | DAG scheduling, interruptions, existing app-aware mechanisms | Open |
| P0 | Mooncake, SGLang, vLLM | Cache/storage tiers and log retention vs recomputation | Open |
| P1 | DroidSpeak, TokenDance, ForkKV | Exact vs approximate cross-model/cross-agent reuse | Open |
| P1 | Autellix, INFRAMIND, KAIROS | Scheduling and power signals, diagnostic integration | Open |
| P1 | CHIEF, MASPrism | Verify mechanism/cost numbers from body (names and abstracts checked) | Open |
| P1 | Who&When, MultiAgentBench, Agent-SafetyBench, AgentHarm | Benchmark scale, trace fidelity, splits | Open |
| P1 | Adjacent surveys | Confirm scope, relationships and added dimensions | Open |

## Reviewer response map
1. Retention: conditional loss equation, state-object matrix, distinction between latency and unrecoverable evidence, vector Figure 5.
2. Literature: cutoff and scope disclosure; audit added, but P0 full-text validation is not done.
3. Taxonomy: CHIEF corrected; MASPrism no longer RL-trained; orthogonal attributes instead of exclusive methods.
4. Comparison: replay/tokens/parameter size separated; 21-system assumptions/limits matrix; explicit unknowns.
5. Multi-agent specificity: causal edges, future agent activation, prefix compatibility, exact versus cross-model KV.
6. Scope/novelty: bounded diagnostic-serving interface, nonbinary survey comparison, falsifiable contribution.
7. Validation: instrumented harness, stage A/B, B0-B4 baselines, false alarms, lead time, task success/recovery, no future-label leakage.
8. Presentation: elsarticle, vector Figures 1–3/5–6, corrected Figure 6 naming.

## Do not claim without verification
- Serving KV eviction inherently destroys diagnostic logs.
- No existing system anywhere shares diagnostic-serving retention budget.
- Proposed policies have been experimentally validated: there are NO new experiments in this revision.
- All infrastructure papers were full-text reviewed.
- Manuscript has compiled successfully or been submitted before actual verification.

## Author-side release checklist
- [ ] Full-text audits with page/table citations for all P0 papers.
- [ ] Fill NR cells only from checked primary sources.
- [ ] Validate BibTeX keys, venue details and authorship.
- [ ] Compile pdflatex/BibTeX in Overleaf and visually inspect tables/figures.
- [ ] Confirm journal review-article eligibility, highlights, affiliations, author contributions and disclosures.
- [ ] Package the submission source files per latest Neurocomputing Editorial Manager guidance.
