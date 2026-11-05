# 03 — Scale Refinement and Composition: Induction on Declared Scales

*Backs manuscript §§1.2, 2.2, 5.1–5.9, 6.2, 6.8–6.9, 6.11, Traces A and K.*

## 3.1 What "induction on scales" borrows and what it does not

In three-dimensional Kakeya geometry, Wang and Zahl (2025) prove that Kakeya sets in `ℝ³` have full Minkowski and Hausdorff dimension, and Guth, Wang, and Zahl (2026) give a streamlined proof. Coleman (2026b, §2.4) reads their architecture as an order of work: control the sticky configuration, then the non-sticky sparse two-scale case, then factor via slabs and planks, then account for the residual, and only then state the general result. That order is the part this paper borrows.

What it does not borrow is any inequality. The geometric arguments establish asymptotic volume and dimension bounds stated with `≲`-type inequalities and losses that are acceptable in the limit. An audit needs a threshold comparison at a finite scale. §1.2 of the manuscript says the analogy "changes how we organize an audit; it does not supply the audit's semantic predicates or prove their validity." The Kakeyalogic seat packet makes the same point: boolean, traceable induction on scales is not a consequence of Wang–Zahl or Guth–Wang–Zahl. Everything proved in this deep dive is proved from finite combinatorics and the stated hypotheses.

## 3.2 The obligation universe

At each scale `k` the manuscript requires an independently specified finite obligation universe `Q_k` (§5.1). An obligation can be local — one activation, one retrieval, one commit — or a *cross-operation invariant* such as a shared budget or a correction frontier. Cross-operation obligations are the entire reason composition is nontrivial; deep dive 03.7 shows what fails without them.

For each obligation `q` the paper uses two predicates, authorization `A_q` and compliance `C_q`, because they answer different questions: "an authorized write can violate a schema; a well-formed retrieved instruction can be unauthorized." Keeping them separate prevents a single combined "ok" bit from hiding which question failed.

## 3.3 The four composition conditions

Proposition 2 lifts sound local certificates to sound global ones under four conditions. Each is necessary for the proof, and each corresponds to a recognizable systems failure when absent.

**R — Evidence-preserving refinement.** For each parent obligation `q` there is a child set `D_k(q)` with `(⋀_{r∈D_k(q)} (A_r ∧ C_r)) ⇒ (A_q ∧ C_q)`. This is a refinement mapping in the spirit of Abadi and Lamport (1991): it states how a coarse specification is implemented by finer steps. The manuscript's R is narrower than their existence theorem; it is a certificate-specific implication that must be witnessed. Renaming an index or matching a label does not supply it.

**C — Complete obligation coverage.** `D_k(q)` accounts for every operation, effect, and cross-operation premise relevant to `q`, and `Q_k` is closed under work generated during the trace — retries, callbacks, dynamically spawned tasks. Without C, the induction proves the parent from an incomplete set of premises.

**N — Noninterference.** Operations outside the certified set cannot alter state on which authorization, compliance, evidence, or refinement depends. This is the noninterference idea of Goguen and Meseguer (1982) applied to certificate premises: low-integrity content must not influence high-integrity decisions. Concretely, retrieved text cannot rewrite policy, routers cannot commit, generators cannot self-accept.

**K — Correction-aware concurrency and freshness.** Reads come from a stated snapshot with linearizable or serializable semantics (Herlihy and Wing, 1990); every causally preceding correction is included; versions are valid at effect boundaries; accepted corrections invalidate dependents before promotion; concurrent conflicts are resolved; replayed approvals do not create fresh authority.

## 3.4 The proof of Proposition 2, annotated

The manuscript's proof is induction over the finite scale index. The annotated version below shows exactly where each hypothesis is consumed.

- **Base.** Every `q ∈ Q_0` has sound `T` verdicts. Soundness converts them into `A_q = C_q = 1`.
- **Step.** Assume all obligations at scale `k−1` are true with certificates. Take `q ∈ Q_k`.
  - *C* ensures `D_k(q)` contains every relevant premise, so nothing outside the child set needs to be true for `q`.
  - *N* ensures nothing outside the certified set altered those premises after they were certified, and that composition conferred no authority the children lacked.
  - *K* ensures the child certificates refer to current, correction-closed snapshots, so they are still about the state the parent depends on.
  - The induction hypothesis makes every child predicate true.
  - *R* converts true children into a true parent.
  - The parent's certificate is the child certificates plus the refinement witness, so every global `T` has a finite path to base evidence.

Removing any hypothesis breaks a specific line. Without C, a missing child can be false. Without N, an uncertified operation can falsify a child after certification. Without K, a child certificate can refer to a superseded state. Without R, true children need not imply anything about the parent. This is why the paper describes the hypotheses as "substantial": they are exactly the places where real systems leak.

## 3.5 Proposition 9: certificates are defeasible

Because the parent certificate is built from child paths and hypotheses, it inherits their defeasibility. Proposition 9 states that if any certificate on the path is invalidated, or R, C, N, or K stops holding, the old parent `T` is no longer justified by Proposition 2. The proposition is careful: it does not say the parent becomes false, only that the old proof no longer supports it. This is the logical basis for treating policy updates, source version changes, and verifier upgrades as part of certificate identity (deep dive 05).

## 3.6 Sticky, non-sticky, and the band

The **sticky case** (§5.3) is the regime in which each fine item has one visible coarse parent, authority and correction scope are shared, all versions agree with the snapshot, and no unlisted channel affects the parent. In that regime the parent check depends only on its declared children and the certificate is small: parent identity, children, receipts, correction acknowledgments, refinement witness.

The manuscript defines a concrete stable-custody nesting from the Riemann-probe packet. For every applicable ancestor `a` of grain `g`, `ANCEST_OK_k` requires an acknowledgment `(a.id, c_id, c_ver)` naming the currently governing correction in `a`'s own registry. `NEST_OK_k` requires fresh parent edges and content hashes. The paper explicitly declines a global comparison `correction_version(parent) ≤ correction_version(child)` because counters from different registries are incomparable — a subtle point: version numbers are only ordered within the registry that issues them.

The **non-sticky band** is the set of grains, claims, and transitions for which nesting fails. The geometric reading in Coleman (2026b) is that coarse tubes can overlap heavily while fine tubes inside them are sparse; the systems reading is that ancestry, authority, or correction scope diverge across children. The discipline imported is *factor only the band*: repair the region that left the sticky regime rather than restarting the whole trace or averaging its failure into global telemetry. Deep dive 05 gives the affected-closure algorithm that does this.

## 3.7 The shared-budget counterexample

§6.11 and Trace K give the canonical demonstration that local passes do not compose. A parent permits total spend 100. Two children each spend 60 and each is individually authorized up to 60. Locally, both `(A, C) = (T, T)`. Globally, `60 + 60 = 120 > 100`, so parent compliance is false.

The example identifies precisely which hypothesis failed. R and C omitted a cross-operation obligation — the shared cap. No number of additional local checks repairs this, because the violation is a property of the pair, not of either element. The repair is structural: add the shared-cap invariant to `D(parent)`, partition the budget in advance, or use an atomic reservation in the ledger so that the second reservation observes remaining capacity 40 and is rejected. The manuscript records detection and rejection separately, anticipating the selection/gate/execution distinction of deep dive 06.

This counterexample generalizes. Any global property that is not the conjunction of local properties — capacity, uniqueness, mutual exclusion, global ordering, aggregate privacy budgets — requires an explicit cross-operation obligation. The obligation universe must be designed with that in mind.

## 3.8 Retention on a finite DAG (Proposition 8)

AIce's contribution adds a complementary result. For each node `v` of a finite refinement DAG, let `Required(v)` be the governing evidence and transitions needed for its action and `C(v)` the admitted carried set. Under base coverage, edge preservation, admission of newly governing patches before action, valid scoped fresh supersession, an enforced gate on every execution, and no unmodeled execution channel, topological induction gives `Required(v) ⊆ C(v)`.

The result is about retention, not semantic sufficiency: it shows required constraints are carried, not that they are the right constraints. AIce's sources also show why the enforced-gate hypothesis is load-bearing. The shipped simulator was advisory — it could execute a selection the gate had rejected — and a local enforcing wrapper that blocked correctly also produced a false stop on legitimate work (E2). Custody and enforcement are different properties, and both need evidence.

## 3.9 The capped schedule and why a loop is not a proof

§5.9 gives the general schedule: for each scale, establish `Q_k` and versions; if sticky, verify locally with refinement witnesses; otherwise factor the band and repair the affected closure under R/C/N/K; recheck; record residuals; return `STRUCTURAL_READY` only if every level passes. The manuscript is careful that "a finite loop is not by itself an induction proof." The loop is how the proof's premises are gathered; Proposition 2 is what turns gathered premises into a conclusion. `max_rounds` bounds work; it does not certify correctness. Residuals — items no admissible carrier explains, the analogue of Grain Zero in Coleman (2026b) — remain visible in the certificate rather than disappearing.

## 3.10 What this layer establishes

Composition across scales is proved valid under four explicit conditions that correspond to well-understood formal traditions: refinement mapping, closed-world coverage, noninterference, and linearizable freshness. The counterexamples show that each is needed in practice. The sticky/non-sticky distinction then gives an efficient operating discipline: cheap certificates where ancestry is clean, targeted repair where it is not, and visible residuals where neither applies.
