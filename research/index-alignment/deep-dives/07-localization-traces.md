# 07 — Failure Localization and the Worked Traces

*Backs manuscript §§4.7–4.8, 6.3–6.5, 7.4, 9.1–9.15, 12.2, Definitions 17, 24–26.*

## 7.1 Why localization is the practical payoff

A scalar alignment score can tell an operator that something went wrong. It cannot say where. The boolean trace `𝔅(T) = (b_0, …, b_M)`, with sub-conjunct outcomes and witness references, can. Coleman (2026a) motivated the index abstraction partly through debuggability: separating roles makes failures attributable. The continuation makes that attribution a computable function of the trace.

## 7.2 FIRST_FAIL and FIRST_NONPASS

Definition 24: `FIRST_FAIL(T) := min{k : A(k) = False}`. Proposition 3: on a finite total scale order, if the failed set is nonempty, the minimum exists and is unique; with a declared sub-conjunct order, the reported failing predicate is unique too. The proof is the well-ordering of finite totally ordered sets.

The manuscript reports a second location, `FIRST_NONPASS`, the least scale with an `UNKNOWN` or `NO_VERDICT` outcome preceded only by passes. The two are reported separately because they mean different things. If scale 2 is `UNKNOWN` and scale 4 is `FAIL`, the observed failure is at 4, but the earliest point where certification became impossible is 2, and the real defect may be there. Overwriting either location with the other would lose information.

The manuscript also limits the claim: `FIRST_FAIL` is "the earliest known failed declared lift, not a metaphysical origin." Several defects can produce the same failed predicate, and the true cause may lie outside the instrumented trace. Trace N makes this concrete: the omission surfaces at the handoff scale even if the compressor that caused it is upstream and unrepresented.

## 7.3 Concurrent failures need a frontier, not a minimum

When the scale structure is a DAG with causal order `≺` rather than a total order, two failures can be incomparable. Choosing one as "first" would encode an arbitrary scheduling artifact as a diagnosis. Definition 26 defines `Frontier(F) = {x ∈ F : no y ∈ F has y ≺ x}`, the set of minimal failures. Proposition 4: in a finite acyclic order, every nonempty `F` has at least one minimal element, and every failure has a minimal failed ancestor. The proof is descent along strict predecessors: acyclicity forbids repetition, finiteness forces termination.

Trace F returns `Frontier(F) = {B.A_ledger.CORR, C.A_cont.Obligation}`. A display may list B first, but the certificate preserves their incomparability. If order edges are missing, the result is `UNKNOWN_ORDER`, consistent with the evidence semantics of deep dive 02.

## 7.4 Computability (Proposition 5)

If each checker terminates on its finite slice, reachability is over a finite graph, and thresholds are present, the trace, frontier, and affected closure are computable in finite time. The proposition is deliberately weak: it is a termination guarantee, not a cost bound, and it excludes semantic discovery. Its practical point is the converse — when a checker does not terminate (an LLM assessor times out), that is an execution status, not a semantic failure. Deep dive 08 develops the execution taxonomy.

## 7.5 Two-ends support and directional coverage

Two predicates detect a failure that counting receipts misses: concentration.

`TWO_ENDS(q)` (Definition 25) requires that no admissible window shorter than `ε|S|` contain more than a `θ_2E` share of a claim's declared support. A claim that is "supported by" a 300-page source but draws all its support from one paragraph may be correct, but it has not engaged the source as a whole; where the contract requires distributed evidence, that should be visible. The vocabulary is borrowed from the two-ends condition in the restriction literature (Wang and Wu, 2024), where it excludes configurations whose mass concentrates in a short piece of a tube; here it is a caller-parameterized audit check, not a theorem.

Directional coverage (Definition 17) requires that each declared direction of relevance — evidence class, obligation, tenant partition — retain a distinguishable lineage at each scale. It is the systems analog of the light-rule posture in Coleman (2026b, §3), contributed through the L seat: every required direction through the custody center remains represented. The manuscript bounds it twice: directions must be declared (no claim to capture all semantic directions), and coverage overlap does not imply authority. High coverage in one class cannot repair an omitted class.

## 7.6 The position-effect motivation

Liu et al. (2024) showed that language models' use of long contexts depends on where relevant information sits, with degraded performance when it is in the middle. That result motivates Trace D, in which beginning and end chunks have challenged quotations and the middle has only a file hash. The manuscript's verdict is `COV_middle = U`, not `F`: the certificate reports missing evidence rather than asserting that the model omitted the middle. The position-effect literature motivates stratifying evaluations by location; it does not license assuming every model fails there.

## 7.7 The diagnostic ladder

The Grok Bot packet contributed a ladder `chunk → section → source → cross-source → handoff`, adopted in §7.4 as a preregistered schedule per task. Each rung has its own obligation universe and transfer witness; passing a rung does not substitute for a missing later rung; skipped rungs must be justified as inapplicable. The ladder is the concrete instance of the declared scale tree for document-grounded tasks, and it makes the first failed lift interpretable: a failure at "section" means within-source aggregation failed, a failure at "cross-source" means synthesis across sources failed, and so on.

## 7.8 The fourteen traces as a coverage argument

The worked traces in §9 are hand-constructed. Their role is to show that every clause the paper introduces can fail independently, that every outcome is reachable, and that the evidence algebra yields the intended verdict in each case. Read as a set, they cover:

| Separation demonstrated | Trace |
|---|---|
| Clean conditional lift with independent denominator | A |
| Registered ≠ permitted | B |
| Coverage ≠ fidelity | C |
| Missing evidence ≠ observed failure | D |
| Signed ≠ fresh | E |
| Concurrent failures → frontier | F |
| Scoped invalidation and partial release | G |
| Termination bound ≠ correctness | H |
| Missing threshold → NO_VERDICT | I |
| Detection ≠ process exit | J |
| Local passes need cross-operation obligations | K |
| Immutable history ≠ isolation | L |
| Partial release under unrelated unknown | M |
| Fluent continuation ≠ preserved commitments | N |

Every predicate family fails in at least one trace (route in B, ledger in E/F/L, generation in C, continuity in N); every non-certified outcome appears (REFUSED in B/C/E, HELD_PARTIAL in G/M, NO_VERDICT in H/I, AWAITING_HUMAN in H with an adjudicator); every composition condition is broken somewhere (C in K, N in L, K in E). The traces are the paper's constructive argument that its distinctions are not redundant: for each pair of conditions it separates, there is a trace where one holds and the other fails.

## 7.9 Trace A as the positive control

A localization scheme is only meaningful if it also certifies clean cases. Trace A fixes policy, registry, authority, snapshot, and `min_coverage = 1.0`; an independent manifest lists exactly five obligations; every scale-0 predicate passes on explicit evidence; the scale-1 lift has R/C/N/K witnesses. `STRUCTURAL_READY = T`, and with the full-release checks the certificate is `CERTIFIED`. Trace I then reuses Trace A's records with `min_coverage` omitted and obtains `NO_VERDICT` — a minimal pair isolating the effect of a missing contract.

## 7.10 What this layer establishes

Localization is exact where order is total (unique first failure), honest where order is partial (a frontier set), and bounded in its claims (earliest known failed lift, not root cause). Concentration and direction checks catch failures that totals hide. The worked traces jointly exhibit every separation the framework draws.
