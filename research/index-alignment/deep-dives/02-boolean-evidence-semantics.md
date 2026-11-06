# 02 — Boolean Evidence Semantics: Why Alignment Can Be Boolean Without Pretending to Know

*Backs manuscript §§1.1, 4.1, 4.6–4.9, 5.1, 6.1, 6.6, Appendix A.1 and B.1–B.2.*

## 2.1 The central claim, stated exactly

The manuscript's thesis is that alignment, in a specific declared sense, "can be treated as a boolean kind of problem." The precise content is a separation of two layers:

1. **Semantic layer.** For an obligation `q`, a fixed history `H_q`, a policy snapshot `Π(q)`, and a specification `Spec_k`, the authorization predicate `A_q` and the compliance predicate `C_q` each take a value in `{0,1}`. Once the specification and history are fixed, either the history satisfies the specification or it does not. This is ordinary bivalence of a well-defined proposition.
2. **Evidence layer.** A monitor observing partial evidence returns a verdict `V ∈ {T, F, U}`, refined operationally into `PASS`, `FAIL`, `UNKNOWN`, and `NO_VERDICT`. The monitor may not know the semantic value.

The release decision is then a third object: a bit `b(P) = 1` iff `Ev(P) = PASS`. That bit is boolean by design. The thesis is not that knowledge is always available; it is that the *question* is boolean and the *control* is boolean, while the *evidence state* is honestly three-valued. Deep confusion about "boolean alignment" usually comes from collapsing those three layers.

## 2.2 Why this monitor retains an inconclusive outcome

Suppose a monitor were required to answer only true or false. Given incomplete evidence about obligation `q`, it must either answer `T` — and be unsound whenever the missing evidence would have shown a violation — or answer `F` — and be unsound whenever the missing evidence would have shown compliance. The manuscript's "Unknown is not true" counterexample (§6.11) makes this concrete: three required operations, two observed and passing. Reporting "2/2 passed" silently changes the denominator. Reporting `F` asserts a violation nobody observed. Within the chosen total-response interface, `U` is the sound response when neither truth value is justified. An abstaining interface or a richer evidence algebra could also preserve soundness; exactly three values are not universally forced.

This is the same structure runtime verification faces. Bauer, Leucker, and Schallhart (2011) define three-valued LTL semantics for finite trace prefixes precisely because a finite observation of an unfinished execution may neither satisfy nor violate a property; an inconclusive outcome preserves soundness in their monitor design. The index-alignment monitor adopts this design for its own evidence conditions and is in the same position with respect to missing receipts, unavailable assessors, and incomplete causal histories.

## 2.3 Strong Kleene conjunction and Proposition 1

The manuscript aggregates verdicts with strong Kleene conjunction: `F` dominates, `T` is the identity, and otherwise the result is `U`. Proposition 1 proves that if each local verdict is sound (`V_q = T ⇒ P_q = 1`, `V_q = F ⇒ P_q = 0`), the aggregate is sound for the conjunction.

The proof is short, but each case does work:

- **Aggregate `T`.** Strong Kleene yields `T` only if every input is `T`. Soundness gives every `P_q = 1`, so the conjunction is 1.
- **Aggregate `F`.** Some input is `F`, so some `P_q = 0`, so the conjunction is 0 — *regardless of unknowns elsewhere*. This is why an observed failure can be reported even when other evidence is missing; Trace C relies on it.
- **Aggregate `U`.** No input is `F` and some is `U`. The semantic conjunction might be 0 or 1. The monitor correctly asserts neither.

Two consequences matter. First, soundness is *inherited*, not *created*: "it does not make an unsound checker sound." A support model that labels contradictions as support breaks the guarantee at its source, which is why deep dive 08 insists on independent labels. Second, strong Kleene conjunction retains a decisive observed `F` even alongside `U`. Weak Kleene conjunction can remain sound but is less informative in that case because it returns `U`. A different rule that relabels unknown evidence as observed falsehood can be unsound: an aggregate `F` would no longer imply an actual violation. Mapping unknown to a release bit of zero is instead an allowed control choice when the evidence reason remains visible.

## 2.4 PASS, FAIL, UNKNOWN, NO_VERDICT: four reasons, one release rule

At the diagnostic layer the manuscript keeps four statuses:

| Status | Meaning | Required witness (Appendix A.1) |
|---|---|---|
| PASS | required evidence present, fresh, satisfies contract | positive evidence |
| FAIL | present evidence violates contract | identified counterexample |
| UNKNOWN | evidence missing, incomplete, stale, or assessor unavailable | insufficiency reason |
| NO_VERDICT | thresholds or assessor contracts not supplied, or reconciliation exhausted | name of missing contract |

`UNKNOWN` and `NO_VERDICT` both map to `U` semantically, but they demand different repairs. `UNKNOWN` asks the operator to collect evidence; `NO_VERDICT` asks the contract owner to decide something — a threshold, a coverage floor, a round cap. Merging them would send work to the wrong person. Trace I (missing `min_coverage`) exists to show that a contract gap must never be repaired by quietly assuming a default: if a system picks `min_coverage = 0.9` on its own, it has made a policy decision it had no authority to make.

The reference pseudocode in Appendix B.1 orders the checks deliberately: undeclared obligation → missing thresholds → execution failure → counterexample → positive witness → otherwise `UNKNOWN`. The final fall-through is the important line. Absence of a counterexample does not produce `PASS`; only a positive witness does.

## 2.5 Non-compensation

Coleman (2026a, Definition 2) defined the alignment deficit `Δ_t = λ_1 d_route + λ_2 d_led + λ_3 d_gen + λ_4 (1 − Cont)`. Weighted scores can summarize defects and support optimization; differentiability requires differentiable constituent functions on an appropriate domain. Whether release compensates for a failed required condition depends on the score ranges, weights and release threshold, not on scalar representation alone. For example, if `b_i∈{0,1}`, `w_i>0` and `D=Σ_i w_i(1-b_i)`, releasing exactly when `D=0` is equivalent to conjunction. No term can compensate for a positive deficit because every term is nonnegative.

The manuscript requires a noncompensatory release rule, expressed as conjunction; an equivalent scalar encoding is permitted. §4.9 states the formal property: replacing any required `True` by `False` makes `A(k)` false regardless of other values. A boolean rule that is true exactly when every required input is true is, by definition, conjunction; any rule that can return true while some required input is false is compensatory. The same discipline appears in Coleman (2026b) for SAVER and SIUS grain vectors ("no weighted average compensates a failed grain"), and the manuscript adopts it as the operational meaning of "boolean alignment": named necessary conditions.

Non-compensation is a design choice with costs. A conjunctive release rule may block outputs that a compensatory weighted rule would pass; an equivalent zero-deficit scalar rule makes the same decisions as conjunction. The partial-release machinery (deep dive 06) exists to recover utility without reintroducing compensation: rather than averaging a failure away, it isolates the failure and releases what does not depend on it.

## 2.6 Composite definitions: A(k), ALIGNED_k, ALIGNED(T)

The manuscript defines three related conjunctions and keeps them distinct:

- `A(k) := A_route(k) ∧ A_ledger(k) ∧ A_gen(k) ∧ A_cont(k)` — full per-scale alignment.
- `ALIGNED_k := COV_k ∧ ORDER_k ∧ CORR_k (∧ STICKY_k)` — a narrower coverage/order/correction diagnostic contributed by the Kakeyalogic seat packet.
- `ALIGNED(T) := ∀k, A(k)` — global alignment across scales.

`ALIGNED_k` is not an alias of `A(k)`. A trace can have complete coverage, valid order, and closed corrections and still fail `Fidelity` (Trace C). Naming the narrow diagnostic separately prevents a coverage dashboard from being read as an alignment certificate. Likewise `ALIGNED(T)` is not `CERTIFIED`: certification adds release authority and non-vacuity.

## 2.7 Non-vacuity and the empty denominator

Any universally quantified predicate over an empty set is true. A checker that finds no required routes, no claims, and no obligations will therefore "pass" vacuously. Definition 27 lists the vacuous cases — empty required set, unknown denominator, empty route or claim sets despite required work, skipped checks reported as passes — and Proposition 6 shows that if `NONVACUOUS` is a required conjunct, a non-PASS value forces the release bit to zero.

The companion rule `EvidenceCoverage = |Q_sound|/|Q_req|`, with `n/a` when `Q_req = ∅`, closes the reporting loophole. Reporting 100% coverage on an empty universe is the denominator version of the same error. The manuscript's insistence that the obligation universe be *independently* established (§5.5) — by a specification manifest rather than by counting observed records — follows: the denominator cannot come from the same evidence it is meant to audit. The 10-agent-team notes flagged exactly this circularity in an early version of Trace A ("all five obligations present" includes itself); the manuscript now states that the fifth obligation's completeness comes from the manifest.

## 2.8 SKIPPED is not PASS

§4.7 adds a fifth operational marker: when an earlier failure makes a later check unsafe to run, the later check is `SKIPPED`. This prevents a common reporting artifact in which tests that never ran appear green. It also preserves the rest of the evidence: a certificate reports the first failure *and* all later observed failures, so an early failure does not hide independent later defects.

## 2.9 Boolean predicates are only as good as their specifications

The boolean framing makes one limitation sharper rather than softer. A semantic predicate is boolean only relative to a fixed specification. If the specification is wrong, a correct certificate certifies the wrong thing. §12.6 lists "semantic booleanization error" — forcing a graded or contested judgment into PASS/FAIL — as a failure mode, with the defense of retaining `CONTESTED` and `UNKNOWN` labels and booleanizing only the release control. Deep dive 09 connects this to Grill (2024) on the politics of testing infrastructure: who writes the specification is a governance question the certificate cannot answer.

## 2.10 What this layer establishes

Booleanity in this paper is achieved by three moves: fix the specification so the semantic question has a truth value; report monitor knowledge in three values so that soundness is preserved under incomplete evidence; and project to a PASS-only bit at the control boundary so that release is conservative without mislabeling unknowns as failures. Proposition 1 shows these moves compose soundly; Proposition 6 shows non-vacuity can be enforced by the same conjunction. The rest of the paper builds on this algebra.
