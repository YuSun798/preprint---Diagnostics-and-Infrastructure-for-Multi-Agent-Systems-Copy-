# V5 evidence audit: verified mappings, unresolved claims and acceptance gates
Date: 2026-11-12. Status: editorial working audit, NOT 60 independent full-text verifications.

The original V5 56-page PDF is preserved page by page as extracted text in V5_SOURCE_SNAPSHOT/. Formatting/figures require comparison with the user-supplied PDF.

## Terms
- Primary paper mapped: method can be linked to its original paper. Does not imply verification of all claims.
- Public primary landing page checked: title, author list, venue and abstract, NOT source-level numerical verification.
- Full-text claim verified: exact source section, table, metric, setup and numbers independently checked.
- Reproduced: raw per-instance predictions or event logs and code rerun; not possible from PDF aggregate tables alone.

## Corpus and missing bibliography items
The 60 V5 rows = 12 localization + 6 observability + 8 safety + 22 infrastructure + 12 benchmarks. Exactly 14 distinct source entries do not have a dedicated reference in V5's 52-entry bibliography:
LangSmith, TokenDance, Leyline, LRAgent, PolyKV, ConServe, MultiAgentBench, GuardianAgentBench, ReliabilityBench, Agent-SafetyBench, AgentHarm, TAMAS, ASB, OSGuard.
The same primary paper contains both TrajAudit and RootSE, so row count and reference count need not match.
Draft publisher/arXiv metadata for 14 missing entries now lives in v5_primary_sources.bib; these **are not a declaration of full-text verification**.
Appendix A still says "approximately 82 distinct systems plus 12 benchmarks"; this is inconsistent with 48 nonbenchmark core entries + around 22 additional textual entries + 12 benchmarks. Correct to approximately 82 combined entries before deduplication, and distinguish systems from standards and surveys.

## T2 inconsistency
StepFinder, FALAT, DoVer, VerifyMAS are all labeled T2 in V5 Table 2 but pp.14–17 give fine-grained training, replay and experimental metrics, sometimes citing specific original tables. Section 3.3 (p.8) defines T2 as abstract-only; p.17 also incorrectly calls DoVer a T1 replay system.
Action: independently read full primary texts and record section/table evidence for each claim before upgrading the tier. Otherwise remove unsupported quantitative detail and keep T2. Do not infer a tier from a plausible citation.

## Benchmark-native label audit
- TraceElephant (ACL 2026): native agent blame and decisive-step annotation, 220 failed traces: https://aclanthology.org/2026.acl-long.912/
- RootSE (TrajAudit): native earliest-error-step labels, 102 coding instances: https://arxiv.org/abs/2605.26563
- Who&When: agent and step labels: V5 bibliography reference [48]; verify exact splits.
- tau-bench: final DB state and pass^k outcome, NOT native step root-cause labels: https://arxiv.org/abs/2406.12045
- MultiAgentBench: collaboration milestones and task outcome; step blame not verified: https://aclanthology.org/2025.acl-long.421/
- GuardianAgentBench: tool-use safety and guardrails, not step blame: https://arxiv.org/abs/2607.20982
- ReliabilityBench: pass^k, perturbations and fault tolerance, not native step blame: https://arxiv.org/abs/2601.06112
- Agent-SafetyBench: risk/failure modes, not native root cause step: https://arxiv.org/abs/2412.14470
- AgentHarm: harmful task refusal/completion, not root-cause step: https://proceedings.iclr.cc/paper_files/paper/2025/hash/c493d23af93118975cdbc32cbe7323f5-Abstract-Conference.html
- TAMAS: adversarial MAS robustness, not step blame: https://aclanthology.org/2026.acl-long.1442/
- ASB: agent attacks and defenses, not step blame: https://proceedings.iclr.cc/paper_files/paper/2025/hash/5750f91d8fb9d5c02bd8ad2c3b44456b-Abstract-Conference.html
- OSGuard: local unsafe-action classification and end-to-end safety, not causal root-cause labels: https://arxiv.org/abs/2606.15034
Action: revise benchmark Table/Figure with separate task success, native agent attribution, native step attribution, safety labels, and serving telemetry columns. Explicitly mark annotations newly inferred by researchers as NOT benchmark-native.

## Statistical and simulation blockers
V5 p.42: C1=101/220; C2=117/220; C3=119/220. Under the paper's definitions, C1→C2 b=22,c=6 (not b=6,c=22); C2→C3 b=28,c=26. Two-sided exact McNemar p values: .0037191659 and .8919231511. Two-sided mid-p: .0023157001 and .7877061897. The table reports exact-test values but incorrectly labels the method mid-p. Report raw 2x2 confusion tables, method and independently computed paired CI.

V5 p.35: LRU 2688 evictions with 100% hit rate, Diag-Aware 2658 evictions with 88.4% hit and 100/100 diagnostic blocks retained. These could use distinct event streams, but the denominator and event semantics must be proved by event-level logs: access/hit/miss, insertion, eviction, key, diagnostic class, and state at retention snapshot. This CPU toy simulation must not be described as a real GPU serving validation.

## 8/10 quality gate (objective criteria, score never guaranteed)
1. Source locator or justified exclusion for 60/60 core entries.
2. Every key numerical claim mapped to primary section/table/page.
3. Four T2 entries either upgraded via actual full-text evidence or quantitatively downgraded.
4. Twelve benchmark capabilities supported by native-label definitions.
5. Statistical values regenerated from per-instance outputs; cache percentages regenerated from event logs.
6. Accessible version-locked scripts and dataset instructions for Tables 7–11; V5 p.50 still uses a future URL placeholder.
7. Native V5 LaTeX source and updated artwork, complete compilation and PDF-vs-source validation.
No assertion of 8/10 until all gates are checked; current package is a substantial source and evidence upgrade, not final validated submission.
