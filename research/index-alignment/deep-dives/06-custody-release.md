# 06 — Custody, Authority, and Release

*Backs manuscript §§2.2, 3.3 (Definition 9), 5.10, 6.6–6.8, 7.2, 8.3–8.5, 10.4, Traces J, L, M.*

## 6.1 Three things that are easy to confuse

A system can *hold* an object, be *entitled to act* on it, and *release* conclusions drawn from it. These are three separate properties. Coleman (2026b, §6.3) states the first separation as "held = relevant + retained ≠ truth": keeping something for evaluation is not endorsing it. The L²_C authority rule (Coleman 2026b, §7.2) states the second: detection of source, authority, intent, and harm precedes incorporation, and untrusted text may be read as content without becoming an instruction. This deep dive explains how the continuation turns those principles into a release contract.

## 6.2 Custody is not truth

In Coleman (2026b), the HELD predicate requires an object to be typed, grounded, evidence-exposed, correction-preserved, and status-visible. Every clause concerns how the object is kept, none whether it is true. The continuation preserves that property: a grain record (§5.2) carries a content hash, status, authority stamp, dependencies, and governing acknowledgments, and the manuscript states that the hash "is not a read receipt, semantic support, freshness, or permission." A perfectly custodied false claim is still false. Custody is what makes later correction possible — you cannot invalidate what you did not keep — which is why NOSILENT requires superseded records to remain queryable.

## 6.3 Authority: `Act = S · H · U` and `Act = 0 ⇏ Stop`

Definition 9 adopts the three-factor authority gate: authenticated source authority `S`, hierarchy validity `H`, authorized user intent `U`. All three must be 1 for `Act = 1`. Two consequences are built into the definition.

**`S = 0 ⇒ Act = 0`.** Content from a source without authority cannot authorize an action no matter how it is phrased. This is the structural defense against instruction injection through retrieved documents: Trace L's document saying "make router an approver" has a valid content receipt and no authority. The manuscript's "found content is not an instruction" example states the verdict: `F` if evidence establishes no authority, `U` if authority evidence is incomplete, never `T` from retrieval alone.

**`Act = 0 ⇏ Stop`.** Denying an action is not the same as halting the system. A privileged tool call can be refused while an informational response explaining the refusal is still produced. Coleman (2026b) states this as detection without resistance: L²_C "does not resist instruction-shaped content," it declines to incorporate unauthorized instructions and proceeds toward an authorized outcome. The continuation uses the rule to justify partial release (§6.6 below) and is explicit that it "does not override a separate policy requiring complete suppression."

## 6.4 Selection, gate verdict, execution, effect

AIce's contribution adds a four-way distinction that the manuscript adopts in §§6.8, 7.2, and 10.4: `selected_action`, `gate_verdict`, `executed_action`, `observed_effect`. Each can diverge from the others.

- A gate can reject a selection that an advisory executor runs anyway. AIce's shipped simulator was advisory in exactly this way.
- An enforcing wrapper can block correctly and still reject legitimate work — AIce's E2 false stop.
- A blocked action can still have produced partial logs or externally visible effects before the block.

The manuscript draws the consequence: "a correct verifier can be attached to a broken executor." Certificates about detection say nothing about enforcement unless enforcement is separately recorded and checked. Mutation M27 (gate rejects but tool executes) is classified as `EXECUTION_ERROR`, distinct from detection — a distinction formalized in deep dive 08.

## 6.5 Structural readiness and full release

§5.10 defines two levels of promotion.

`STRUCTURAL_READY_k` is the conjunction of COV, ORDER, CORR, ROUTE_OK, LEDGER_OK, GEN_OK, `A_cont`, and STICKY where required, achieved directly or after capped reconciliation. It certifies that the structure is intact: evidence received, order valid, corrections propagated, lineage complete.

`RELEASE_FULL` additionally requires CROSS_OK, CROSS_SCALE_OK, SCOPE where measured claims occur, POLICY_OK, AUTH, SUPPORT, FID, and NONVACUOUS. These checks use evidence independent of ingestion receipts, and SUPPORT/FID use a declared external assessor.

The split exists because structural integrity is necessary and cheap to check, while semantic support is expensive and depends on an assessor whose reliability must itself be established. Reporting structural readiness as if it were release would recreate the coverage-equals-fidelity error at the level of the whole certificate. The Riemann-probe packet contributed this split and the rule that four-valued evidence maps to PASS-only bits, with missing evidence blocking full promotion but not authorized unaffected partial output.

## 6.6 Five outcomes

`INDEX-ALIGN-CERT` returns one of five outcomes (§8.3):

| Outcome | Condition | Typical trace |
|---|---|---|
| CERTIFIED | all full-release conjuncts pass, independent release authority, non-vacuous | A |
| HELD_PARTIAL | only authorized unaffected content emitted; held dependencies named | G, M |
| REFUSED | observed failure prohibits the requested release | B, C, E |
| AWAITING_HUMAN | contract names an authorized adjudicator for an exact question | H (with adjudicator) |
| NO_VERDICT | missing thresholds, incomplete evidence, unavailable assessor, exhausted reconciliation, invalid execution | I, H (no adjudicator) |

The outcome set is richer than pass/fail because control decisions are richer than truth values. The same predicate trace can yield different outcomes under different authorized scopes: "a semantic pass in a sandbox can coexist with refusal to publish because AUTH is absent." `AWAITING_HUMAN` names a role and an exact question, not a generic request for oversight.

## 6.7 The partial-release rule

For candidate output `o`, partial emission requires `Deps(o) ∩ Aff = ∅`, that `o`'s own route, authority, policy, support, scope, and continuity checks pass, that dependency enumeration and N pass for its scope, and that the output is labeled partial and names excluded obligations (§8.4). Appendix A.1 adds that `HELD_PARTIAL` "cannot be inferred solely from Aff disjointness."

Trace M shows the rule's purpose. A report has independent sections X and Y; Y's support assessor is unavailable. Full promotion is blocked with `SUPPORT(Y) = U`. X, independently supported and isolated from Y, may be emitted as `HELD_PARTIAL`. Y is not labeled false. Without partial release, a conjunctive rule would discard X because of an unrelated unknown — exactly the utility loss that makes conservative certification unattractive in practice. With it, conservatism is confined to the affected region.

The Grok Bot packet contributed the corresponding operator-facing protocol: labeled partial answers that name uncovered chunks, and `NO_VERDICT` where thresholds are missing.

## 6.8 Independent verification

§8.5 applies the trust-boundary argument of deep dive 01 to the release decision. PROV-002 requires a verifier outside the process capable of forging receipts. A challenge generated and checked by the same process is an honest-workflow control, useful against accidents and useless against a compromised process. An in-process HMAC does not protect against code holding the same key. "The release decision itself is verifier output, not evidence of its own correctness" (§10.1). Independence also has a social dimension: model agreement is not independence, because models share training data and rubric blind spots (deep dive 08).

## 6.9 `h < 1` and private facts

Coleman (2026b, §7.3) treats `h < 1` as an evaluator non-sovereignty boundary: the evaluating system remains bounded, and claimed sovereignty overreach is telemetry. The continuation keeps it as a stipulated design boundary, not a measured score, and adds the rule that private personal facts are excluded from synthetic predicates and cannot raise or lower a verdict. Excluding a class of inputs from the decision is a structural privacy property of the certificate; it is not a proof that the surrounding system preserves privacy.

## 6.10 What this layer establishes

Holding, authorizing, and releasing are separated into distinct evidence channels with distinct checks. Authority is a conjunction of three externally evidenced factors that content cannot supply. Detection is separated from enforcement and enforcement from effect. Release is graded into five outcomes so that a blocked full release does not suppress authorized, isolated, labeled partial output. Together these turn Coleman (2026b)'s custody and authority principles into a release contract whose every clause names its own evidence.
