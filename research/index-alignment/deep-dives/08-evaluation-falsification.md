# 08 — Evaluation, Falsification, and Cost

*Backs manuscript §§6.10, 10.1–10.4, 11.1–11.10, Appendix D, Trace J.*

## 8.1 What a falsifiable certificate design looks like

A certification scheme is scientifically useful only if it can be shown to be wrong. The manuscript states its falsifiers as fixtures: inputs for which a wrong design passes and the correct design does not. A fixture falsifies a *named design or implementation conformance condition*. That scoping is precise rather than defensive — a fixture about coverage and fidelity tests whether the release rule conflates them; it cannot test a theorem in geometry or number theory, because those are not inputs to the checker.

## 8.2 The eight core fixtures

From the Riemann-probe packet, §11.9 lists eight fixtures, each targeting one separation:

1. **COV-pass/FID-fail** — all chunks receipted, conclusion unsupported. A design that releases on coverage alone passes it.
2. **Route substitution** — registered but unauthorized tool or expert. A design that ignores `Π` passes.
3. **Stale correction handoff** — child uses pre-correction view. A design that does not invalidate `Aff` passes.
4. **SEM-003 status inflation** — strategy labeled proved. A design without `StatusType` passes.
5. **SCOPE overclaim** — measured claim generalized. A design without tested-workflow scope passes.
6. **PROV-002 hash-only reread** — hash presented as reading. A design without independent content-bound verification passes.
7. **ACT conflation** — covered but unauthorized instruction. A design in which coverage grants `Act` passes.
8. **Index echo** — cited identifier absent from visible activations. A design without generation–index lineage passes.

Appendix D extends these to thirty-two mutations (M01–M32) spanning registry rollback, wrong quoted spans, post-rationalized citations, omitted callbacks, replayed nonces, cross-registry acknowledgments, authority pollution, router self-commit, generator self-certification, empty universes, missing thresholds and assessors, compression-dropped goals, gate bypass, harness crashes, correction storms, hidden caches, and silent rubric edits. Each row states the clean expectation, the fault expectation, and what non-detection would warn about.

## 8.3 Detection requires a baseline and an attributable failure

The most consequential methodological rule in the evaluation section is that "a nonzero exit status alone never counts as detection" (§11.6). It comes from a concrete hazard reported by the 10-agent team's review of an open-addressing probe: same-author mutation scripts that count any nonzero exit as a "killed" mutant. An import error, an unrelated assertion, or a timeout then counts as successful detection, inflating the kill rate with infrastructure failures.

The manuscript's taxonomy separates five outcomes:

- **CLEAN_PASS** — the unmodified baseline passes named checks under the same configuration. Without it, no comparison is valid.
- **DETECTED** — the variant runs far enough to evaluate the intended property and a predeclared named check fails for the intended reason.
- **UNDETECTED** — a valid run completes without relevant detection.
- **HARNESS_ERROR** — the intended check could not be evaluated: import failure, malformed harness, unrelated exception, timeout.
- **EXECUTION_ERROR** — enforcement or environment fails even though detection is valid.

Trace J demonstrates all of them on one configuration. The team notes used `HARNESS_ERROR` and earlier text used `EXECUTION_ERROR` for overlapping cases; the manuscript harmonizes them by putting them on different axes — evaluation infrastructure versus enforcement — so a single run can be `DETECTED` on the detection axis and `EXECUTION_ERROR` on the execution axis.

## 8.4 Labels must be independent of the monitor

§11.2 requires that ground truth come from independently constructed specifications, hand-audited synthetic traces, or injected faults with known mechanisms: "the monitor's own output cannot supply its labels." This is the evaluation analogue of the independent-verifier rule. Three bodies of work motivate the specific protocol.

**Human annotation discipline.** AIS (Rashkin et al., 2023) and FABLES (Kim et al., 2024) build attribution and faithfulness labels through structured human annotation, and FABLES specifically annotates omissions in long summaries. The manuscript adopts claim-level sampling and omission checks from that discipline.

**Independence of judges.** Sycophancy research (Sharma et al., 2024) shows models adjusting answers toward perceived user preferences, and BenchForm (Weng, Chen, and Wang, 2025) shows conformity to group answers. The protocol therefore collects human ratings independently before discussion and treats agreement between model assessors as non-independent evidence: separate answers from models with shared training data and rubrics are correlated.

**Criteria drift.** EvalGen (Shankar et al., 2024) found that users refine their evaluation criteria while grading outputs. The protocol does not deny drift; it versions it. Exploratory rubric development creates a new specification epoch; confirmatory runs use a frozen manifest (§7.6, §11.8).

## 8.5 Six research questions

The manuscript frames six questions, each paired with a measurable outcome: sound booleanization (inter-rater and oracle agreement under fixed specs), localization (does first failure predict the repair site better than scalar telemetry?), composition (do R/C/N/K witnesses prevent false global acceptance?), partial release (is useful unaffected output retained without contaminated promotion?), cost and utility (latency, tokens, dollars, human minutes, false blocks, missed coverage), and drift (how often do criteria, registries, sources, and assessors change enough to invalidate certificates?). They are posed as questions; their answers are what the protocol is designed to measure.

## 8.6 Metrics that do not hide unknowns

Detection metrics are standard — TPR, FPR, precision on valid evaluable episodes, with `n/a` for empty denominators — with one modification: `U` is reported separately and is never encoded as detection or non-detection. Where policy holds on `U`, the protocol measures that control choice by its false-block and missed-violation consequences "without changing the epistemic label."

Trace-level metrics include global-violation recall, R/C/N/K failure recall by category, false global acceptance, false-block rate, detection latency, correction propagation completeness, stale-approval acceptance, and lineage completeness. The manuscript names the two degenerate designs these metrics must expose: a certificate that refuses everything has zero false acceptance and no utility; one that accepts everything has high completion and no safety value.

Evidence metrics include `EvidenceCoverage` with a vacuity flag, unknown rate by reason, threshold-supplied rate, content-bound vs hash-only coverage, fresh-snapshot coverage, asynchronous side-effect coverage, refinement-witness coverage, and correction-frontier completeness.

## 8.7 Baselines and ablations

The protocol compares the certificate against seven baselines: scalar weighted deficit (Coleman 2026a's `Δ_t`), raw model self-assessment, citation-membership only, receipt-coverage only, a global end-of-trace judge, per-call local checks without composition conditions, and human review alone. Capability, context, tool access, token budget, and human time are matched. Ablations remove typed lineage, content-bound receipts, noninterference checks, correction closure, cross-scale receipts, independent assessors, non-vacuity, and partial-release logic, one at a time and jointly — joint ablations matter because C interacts with N and K with correction propagation.

RAGChecker (Ru et al., 2024) is the closest existing diagnostic framework: it separates retriever and generator metrics to locate defects. The index-alignment protocol shares that modular aim and differs by making each relation a non-compensatory release conjunct with a witness path.

## 8.8 Cost of verification

Proposition 10 bounds verification of a supplied restricted certificate at `O(n + |E| + cB + r + w)`: one pass over records, one shared graph traversal, at most one support-oracle call of cost `B` per claim, plus receipts and windows. The proof charges each item once; the restrictions are stated so that repeated per-claim or per-seed traversals, if an implementation needs them, are charged separately rather than hidden.

The bound is about verification, and §10.4 separates four costs that are often conflated: search (finding routes, evidence, repairs), verification (checking the witness), enforcement (blocking execution), and observed effect (what happened). Cheap verification does not imply cheap search. The P-NP seat's non-claims D1–D9 make the boundary explicit: no reduction is given in either direction, no hardness or membership claim is made for general index alignment, and polynomial verification of a supplied witness does not classify the search problem.

Cer-Eval (Wang et al., 2025) and Derailer-Rerailer (Wan et al., 2025) motivate selective, staged verification to reduce cost; VeriLA (Sung, Kim, and Zhang, 2025) motivates explicit, human-centered agent failure criteria. The protocol adopts the cost-reporting discipline and requires that any selection policy itself be evaluated for missed violations. The Grok Bot packet's rule that verification spending should be incurred where it can change the answer is the operational form.

## 8.9 Existing construction evidence

§11.10 reports what neighboring artifacts already show. AIce's opto probe at revision `e623a10` reports 110 synthetic runs with zero mismatches against frozen expectations and 539 tests, with documented limitations including handoff RPL = 0, live `L_N = .75` versus compressed 1, order-unaware replay, and in-process registry forgery. The open-addressing probe reports 7 of 8 confirmatory predictions held, with P3 failed. These are source-reported numbers for neighboring constructions; their methodological value — failed predictions kept visible, exploratory sweeps separated from confirmatory ones — carries over directly. The `thinkingmachines.txt` transcript documents Benevolence Drift Case 01, an evasive first response that became an explicit "Yes" after a forced binary prompt; Case 02 has no forced-binary follow-up in the supplied material.

## 8.10 What this layer establishes

The evaluation design specifies how to break the construction: fixtures for each separation, a mutation inventory, independent labels, an execution taxonomy that cannot count crashes as detections, metrics that keep unknowns visible, baselines that include the scalar deficit the paper replaces, ablations, and a cost model that separates verification from search and enforcement. Each element is traceable to a specific hazard reported in the cited literature or in the team's own probes.
