# Claim–Evidence Matrix

Each major claim of *Boolean Index Alignment* (Manuel Coleman, 2026) is mapped to its location in the manuscript, the deep-dive section that develops it, and its cited background. The sources do not establish this construction’s empirical efficacy. "Proof" means a conditional argument is written in the manuscript and annotated in the deep dive, not machine verification or implementation validation; "construction" means the object is defined in this paper; "source" means an external or prior work supports the cited point.


This is the revised claim wording. The [independent review and 47-claim ledger](audit/independent-research-review.md) record the original claims at commit `74c910e`; [revision dispositions](audit/REVISION.md) map those findings to these changes. All proposed LLM evaluations remain unperformed.

| # | Claim | Manuscript | Deep-dive anchor | Basis | Primary citations |
|---|---|---|---|---|---|
| 1 | Sparse-system failures are usefully analyzed as mismatches among typed discrete indices | §1.1, §3.1 | 01 §1.1–1.2 | construction + source | Coleman 2026a; Shazeer 2017; Fedus 2022; Jiang 2024; Lewis 2020; Schick 2023 |
| 2 | Registry liveness and policy permission are distinct predicates | Def. 1–2, §4.2, Trace B | 01 §1.3; 04 §4.2 | construction | Coleman 2026a Def. 1(1), Def. 3 |
| 3 | Gate weight is telemetry, not permission or quality | Def. 2, §2.3 | 01 §1.4; 04 §4.2 | source | Shazeer 2017; Lepikhin 2020; Fedus 2022; Cai W. 2024 |
| 4 | Citation lineage generalizes pointer discipline and is necessary but not sufficient for support | Def. 3, §4.4 | 01 §1.5; 04 §4.4 | construction + source | Vinyals 2015; Rashkin 2023; Gao 2023 |
| 5 | A digest alone proves neither possession nor reading; challenged spans offer sampled content evidence under stated assumptions | Def. 4, §8.5 | 01 §1.6; 06 §6.8 | construction | — (trust-boundary argument given in full) |
| 6 | Scales are declared audit levels, not model or training scales | Def. 5, §5 intro | 01 §1.7; 03 §3.1 | construction | Coleman 2026b §2.4 (order only) |
| 7 | Happened-before, not wall clocks, determines ORDER | Def. 14 | 01 §1.9; 05 §5.3 | source | Lamport 1978 |
| 8 | Semantic A/C predicates are boolean under a fixed spec; this monitor chooses T/F/U and retains diagnostic reasons | §4.1, §5.1 | 02 §2.1–2.2 | construction + source | Bauer–Leucker–Schallhart 2011 |
| 9 | Strong Kleene aggregation of sound verdicts is sound (Prop. 1) | §6.1 | 02 §2.3 | proof | — |
| 10 | PASS-only release bit; UNKNOWN and NO_VERDICT kept distinct; no hidden defaults | §4.1, App. A.1, B.1, Trace I | 02 §2.4 | construction | — |
| 11 | Release is non-compensatory; conjunction and a positive-weight scalar zero-deficit rule can encode the same policy | §2.1, §4.9 | 02 §2.5 | construction + source | Coleman 2026a Def. 2; Coleman 2026b §7.5 |
| 12 | Non-vacuity blocks release; empty denominators report n/a (Prop. 6) | Def. 27, §6.6 | 02 §2.7 | proof | — |
| 13 | Kakeya induction supplies an order of work, not an implication | §1.2, §2.2, §2.6 | 03 §3.1; 09 §9.7 | source | Wang–Zahl 2025; Guth–Wang–Zahl 2026; Coleman 2026b |
| 14 | Sound local certificates lift under R, C, N, K with Q_j corresponding to P_{M-j} | §5.4–5.7, §6.2 | 03 §3.3–3.4 | proof + source | Abadi–Lamport 1991; Goguen–Meseguer 1982; Herlihy–Wing 1990 |
| 15 | Local passes do not compose without cross-operation obligations | §6.11, Trace K | 03 §3.7 | proof (counterexample) | — |
| 16 | Certificates are defeasible when any premise changes (Prop. 9) | §6.9 | 03 §3.5; 05 §5.10 | proof | — |
| 17 | Required constraints are retained on a finite DAG under stated hypotheses (Prop. 8) | §6.8 | 03 §3.8 | proof | AIce STUDY.md §§3–10 (seat contribution) |
| 18 | Stable-custody nesting uses per-registry acknowledgments, not global version comparison | §5.2 | 03 §3.6 | construction | Riemann-probe seat packet |
| 19 | A_route, A_ledger, A_gen, A_cont operationalize the four 2026a consistency relations | §4.2–4.5, App. E | 04 §4.1–4.5 | construction | Coleman 2026a Def. 1 |
| 20 | Order is not authority; append-only is not isolation | §4.3, §5.6, Trace L | 04 §4.3; 06 §6.3 | construction | Lamport 1978; Goguen–Meseguer 1982 |
| 21 | Coverage is not fidelity | §4.4, Trace C | 04 §4.4 | construction + source | Rashkin 2023; Gao 2023; Wallat 2024 |
| 22 | Exposed lineage is not proof of causal reliance | §12.1 | 04 §4.4 | source | Wallat 2024 |
| 23 | Continuity is preserved obligations across compression and handoff | §4.5, Trace N | 04 §4.5 | construction + source | Packer 2023; Park 2023; Coleman 2026a §3.3 |
| 24 | Authority requires S·H·U from channels content cannot supply; Act=0 ⇏ Stop | Def. 9 | 06 §6.3 | construction + source | Coleman 2026b §7.2 |
| 25 | Signed is not fresh; stale approvals yield U or F, never T | §6.11, Trace E | 05 §5.4 | proof (worked) | Lamport 1978 |
| 26 | Correction invalidation is reachability over the dependency graph; whole closure is rechecked | §5.8, §8.1, App. B.4 | 05 §5.6 | construction | — |
| 27 | Unaffected outputs keep their certificates under isolation (Prop. 7) | §6.7, Trace G | 05 §5.7 | proof | Goguen–Meseguer 1982 |
| 28 | Round caps bound iterations; total termination additionally requires terminating subcalls or a decision deadline | §5.8, Trace H, App. B.5 | 05 §5.9 | construction | — |
| 29 | Repetition by many agents is not authority | §8.1 | 05 §5.2 | source | Weng–Chen–Wang 2025 |
| 30 | Custody is not truth | §1.4, §5.2 | 06 §6.2 | source | Coleman 2026b §6.2–6.3 |
| 31 | Selection, gate, execution, and effect must be recorded separately | §6.8, §7.2, §10.4 | 06 §6.4 | source | AIce SCORECARD.md; PEAICE-AICE-OPTO-PROBE-001 |
| 32 | STRUCTURAL_READY is distinct from RELEASE_FULL | §5.10 | 06 §6.5 | construction | Riemann-probe seat packet |
| 33 | Five outcomes; authorized unaffected partial output survives blocked full release | §8.3–8.4, Trace M | 06 §6.6–6.7 | construction | Grok Bot seat packet; L seat |
| 34 | First failure is unique within the declared total order, which records order position and partition depth (Prop. 3) | §6.3 | 07 §7.2 | proof | — |
| 35 | The concurrent frontier is exactly the set of minimal failed DAG nodes (Prop. 4) | §6.4, Trace F | 07 §7.3 | proof | — |
| 36 | Localization is finitely computable under terminating checkers (Prop. 5) | §6.5 | 07 §7.4 | proof | — |
| 37 | Declared proper-window and directional checks distinguish selected support distributions; useful detection needs validation | Def. 6, 17, 25 | 01 §1.8; 07 §7.5 | construction + source | Wang–Wu 2024 (vocabulary); Coleman 2026b §3 |
| 38 | Position effects motivate location-stratified coverage | §12.2, Trace D | 07 §7.6 | source | Liu 2024 |
| 39 | Fourteen hand-constructed traces illustrate selected separations; coverage is not exhaustive or executed | §9 | 07 §7.8 | construction | — |
| 40 | Restricted certificate verification is O(n + #edges + cB + r + w) (Prop. 10) | §6.10, §10.2 | 08 §8.8 | proof | — |
| 41 | Verification cost does not classify search; D1–D9 | §10.3–10.4 | 08 §8.8 | construction | P-NP seat packet |
| 42 | Detection requires clean baseline and attributable named failure; nonzero exit is not detection | §11.6, Trace J | 08 §8.3 | construction | 10-agent team notes |
| 43 | Labels must be independent; model agreement is not independence | §11.2, §12.3 | 08 §8.4 | source | Sharma 2024; Weng 2025; Rashkin 2023; Kim Y. 2024 |
| 44 | Criteria must be versioned as epochs | §7.6, §12.4 | 08 §8.4 | source | Shankar 2024 |
| 45 | Evaluation includes compensatory and equivalent non-compensatory scalar policies, self-assessment, citation, coverage, global/local and human baselines | §11.7 | 08 §8.7 | construction | Ru 2024; Coleman 2026a |
| 46 | Cost of verification must be reported on all axes | §11.8 | 08 §8.8 | source | Wang G. 2025; Wan 2025; Sung 2025 |
| 47 | Certificates cannot settle who owns the specification | §12.4 | 09 §9.5; 02 §2.9 | source | Grill 2024 |

## Seat contributions reported in the original package

These paths are historical attribution, not included source files or independently verified inputs to this revision. The review did not recover the local seat packets or the 26-repository inventory. Public links are separate source pointers; reported synthetic results were not rerun.

| Seat | Material | Local path |
|---|---|---|
| Kakeyalogic | COV/ORDER/CORR/STICKY, threshold rule, geometric boundary | `/workspace/peaice/team-formalization-2026-11-05/kakeyalogic-boolean-index-r2-2026-11-05.md` |
| L | S/H/U authority, Act=0 ⇏ Stop, release boolean outcomes | `/workspace/peaice/team-formalization-2026-11-05/l-seat-boolean-index-2026-11-05.md` |
| P-NP | INDEX-ALIGN-CERT, verification bound, D1–D9 | `/workspace/peaice/team-formalization-2026-11-05/pnp-boolean-index-2026-11-05.md` |
| Riemann probe | grains/slabs, governing acknowledgments, Aff repair, STRUCTURAL_READY vs RELEASE_FULL, eight fixtures | `/workspace/peaice/team-formalization-2026-11-05/riemann-boolean-index-2026-11-05.md` |
| AIce | DAG retention, selection/gate/execution/effect, synthetic receipts | `https://github.com/Manny536/AIce` (STUDY.md, SCORECARD.md, docs/PEAICE-AICE-OPTO-PROBE-001.md) |
| Grok Bot | diagnostic ladder, PARTIAL protocol, independent provenance, cost discipline | `/workspace/peaice/team-formalization-2026-11-05/index-alignment-grokbot-packet.md` |
| 10-agent team | R/C/N/K composition, semantic/monitor split, execution taxonomy, circularity check | `/workspace/index_alignment_team_notes.md` |
| Public Git handoff | public-repository provenance (26 commit-pinned snapshots) | `/workspace/peaice/team-formalization-2026-11-05/github-inventory-manny365-2026-11-05.md` |
