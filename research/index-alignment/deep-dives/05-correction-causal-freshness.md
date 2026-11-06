# 05 — Correction, Causal Order, and Freshness

*Backs manuscript §§3.6, 5.7–5.8, 6.7, 6.9, 6.11, 8.1–8.2, Appendix B.4–B.5, Traces E, F, G, H.*

## 5.1 Why corrections are the hard case

A system that never changes its mind is easy to certify. Real systems receive corrections: a source is revised, a policy revoked, a user retracts an instruction, a tool is deprecated. Each correction makes some earlier certificates obsolete, and the difficulty is knowing which. Too narrow an invalidation lets stale conclusions survive; too broad an invalidation discards everything and destroys utility. The manuscript's answer is to treat a correction as a scoped graph operation with explicit authority, and to compute its consequences by reachability.

## 5.2 The correction object

Definition 15: `c = (target, issuer, authority_evidence, scope, applicability, lineage, nonce, tag, timestamp)`. Each field has one job.

- **target** is the seed in the dependency graph.
- **issuer** and **authority_evidence** determine `Authorized(c)`, which requires authenticated authority over the target and scope.
- **scope** and **applicability** prevent a correction to one tenant, workflow, or interval from silently rewriting another (mutation M15).
- **nonce** and **tag** support integrity and replay detection.

The manuscript states that "cryptography does not make the issuer correct." A validly signed correction from an authorized issuer can still be wrong; the protocol ensures only that it is attributable and not replayed. And `Authorized(c)` "is independent of whether many agents repeat it" (§8.1): repetition is not authority. That rule is a direct response to conformity findings in multi-agent settings (Weng, Chen, and Wang, 2025) — models can converge on a group answer whether or not it is correct.

## 5.3 Happened-before rather than timestamps

Lamport (1978) defined happened-before as the smallest relation containing program order and message send/receive, closed under transitivity, and showed that physical clocks in a distributed system cannot by themselves recover it. The manuscript's Definition 14 specializes the relation to the edges that matter for certification — intake/receipt, proposal/commit, correction/dependency — and requires its transitive closure to be acyclic.

Three outcomes are distinguished. A cycle in complete relevant evidence is `ORDER = False`: the trace claims something impossible. Missing required edges are `UNKNOWN`: the order cannot be determined. An absent ordering contract is `NO_VERDICT`. This three-way split matters because the repair differs: a cycle indicates corrupted or forged records, missing edges indicate incomplete instrumentation, and an absent contract indicates a design gap.

## 5.4 The stale-concurrent-approval example

§6.11 gives the example that motivates condition K. Approval `a` authorizes `tool:t17` under registry `r7`. Correction `c` revokes it in `r8`. Operation `o` depends on `a` but not on `c`. Vector clocks `VC(a) = (1,0,0)`, `VC(c) = (0,1,0)`, `VC(o) = (1,0,1)`.

Read componentwise: `VC(a) ≤ VC(o)` in every coordinate and differs, so `a → o`. `VC(c)` and `VC(o)` are incomparable — `c` has a 1 in the second coordinate where `o` has 0, and `o` has a 1 in the third where `c` has 0 — so `c` and `o` are concurrent. The operation's causal past contains the approval and not the revocation.

The monitor's verdict depends on what it knows about the correction frontier. Before the frontier is known, current authorization is `U`: the approval might still be valid. After a complete history shows that current policy requires `r8` validity and `r8` revokes the tool, it is `F`. In neither case is it `T`, even though the signature on `a` verifies. The lesson the manuscript draws — "signed and fresh are separate" — is the precise distinction between integrity of an artifact and its currency. Trace E develops the same example at the tool-call boundary.

## 5.5 Condition K in six parts

Condition K (§5.7) is the formal summary of what freshness requires:

1. The contract declares operation/transaction boundaries and the required real-time freshness property. Linearizability applies to single-object operations; strict serializability can supply real-time transaction order for multi-operation transactions. Ordinary serializability alone is insufficient for that order and is not equivalent to linearizability (Herlihy and Wing, 1990, §3.3). Individually linearizable field reads do not ensure a joint snapshot: use a joint atomic snapshot, a justified strictly serializable transaction, or a validated version protocol across all relevant fields. Policy-dependent effects require an appropriate atomic admission or revalidation boundary.
2. Every causally preceding correction is included — and concurrent corrections are not fabricated into dependencies. Overstating dependencies is also an error: it can invalidate certificates that were never affected.
3. Versions remain valid at effect boundaries or are revalidated. Time-of-check/time-of-use gaps are the classic violation.
4. Accepted corrections transitively invalidate dependents before promotion.
5. Conflicting concurrent operations are ordered or explicitly resolved.
6. Replayed approvals and nonces do not create fresh authority (mutation M11).

The manuscript also separates four retrieval outcomes that are routinely conflated: `NOT_YET` (causally invisible), `ABSENT` (legitimately nonexistent), `LOST` (failed retrieval), and `FOUND`. "Causal invisibility is not nonexistence, failed retrieval is not a legitimate negative, and retrieval is not permission."

## 5.6 Affected closure

Given seeds `Z` — failing or corrected nodes — the manuscript computes `Aff = Reach_G(Z)`, the set of all nodes reachable from the seeds in the dependency graph, across indices, scales, claims, ledger projections, and pending actions (§5.8). Every node in `Aff` is marked stale or quarantined with the appropriate status, history is preserved, evidence outside `Aff` is retained if N holds and its freshness is valid, repairs are made along affected edges, and the *entire* closure is rechecked — not only the seed.

Rechecking the whole closure is the critical step. A common incremental-repair bug is to fix the seed and assume downstream results update automatically. If a summary was generated from a claim that was generated from a corrected document, fixing the document does not fix the summary; the summary must be regenerated or quarantined. Mutation M14 (one affected descendant omitted) targets exactly this.

Computing `Aff` is linear in the graph: breadth- or depth-first search visits each node and edge once. Appendix B.4 gives the pseudocode, and Proposition 10's bound includes one shared traversal for the union of closures.

## 5.7 Proposition 7: what stays valid

Proposition 7 states the complementary guarantee. If output set `O` satisfies `Deps(O) ∩ Aff = ∅`, N holds, evidence versions for `O` are stable, and the dependency graph is complete for the release scope, then a correction confined to `Z` and its outgoing dependencies does not change the predicates certified for `O`.

The proof is reachability plus isolation: no dependency path from `Z` reaches `O`'s dependencies, N excludes unmodeled influence, and stable versions keep inputs fixed. Each hypothesis has a practical failure. An incomplete dependency graph misses an edge — for example a shared cache or a hidden context window (mutation M31). A failure of N allows a correction to influence `O` through a side channel. Unstable versions mean `O`'s evidence changed for an unrelated reason. When any is uncertain, unaffectedness is `UNKNOWN`, and partial release is not certified.

The manuscript adds a limit that graph semantics cannot overcome: "previously emitted unretractable copies cannot be recalled by graph invalidation." Invalidation governs future promotion. It does not retrieve an email already sent.

## 5.8 Trace G and Trace F

Trace G applies both propositions. A source correction moves `d4` from version 2 to 3. Claim `q4`, summary `s4`, and pending tool action `x4` depend on `d4`; extraction `q1` depends only on `d1`. With dependency enumeration and N independently established, `Aff = {d4, q4, s4, x4}`. Those are held. `q1` may be released as `HELD_PARTIAL` with an explicit exclusion notice, after its own authority and support checks pass.

Trace F applies closure to concurrency. Agent A commits a valid plan; agent B uses a revoked memory item; agent C drops an unrelated open obligation. B and C are causally incomparable. The frontier contains both, repair computes two closures, and A may be released only if its dependencies intersect neither.

## 5.9 Correction storms and the round cap

Trace H is the adversarial case for closure: two authorized registries alternately supersede conflicting values. Each correction correctly invalidates the other's dependents, and the system can oscillate indefinitely. The manuscript's reconciliation loop (Appendix B.5) has a caller-supplied `max_rounds`; exhausting it returns `NO_VERDICT("CORRECTION_STORM_OR_ROUND_CAP")`, or `REFUSED` if policy prohibits unresolved contested output, or `AWAITING_HUMAN` where the contract names an adjudicator. "No arithmetic average of versions chooses a winner." The cap bounds iterations. Total termination of the decision requires every repair/check/I/O call to terminate or a supervisor that can return a deadline outcome independently of a blocked call. A timeout does not establish cancellation or rollback; unconfirmed effects remain held. A timeout is an execution status, not evidence that a registry is wrong; the cap does not decide which registry is right. That decision is an authority question outside the loop.

## 5.10 Freshness as part of certificate identity

The freshness table in §8.2 lists, for each predicate, the evidence that makes a certificate current and the event that invalidates it — a version bump for COV, a rewrite without supersession for ORDER, a new applicable correction for CORR, deregistration or policy revocation for ROUTE_OK, assessor drift for SUPPORT/FID. The table operationalizes Proposition 9: the certificate's identity includes the versions of everything it relied on, so a change in any of them is a change in what the certificate is about. "A preserved artifact can be obsolete; custody is not freshness."

## 5.11 What this layer establishes

Corrections are handled as authorized, scoped seeds whose consequences are the reachable closure in an explicit dependency graph. Happened-before, not timestamps, determines what a step could have seen; declared real-time snapshot/effect semantics constrain "current policy"; one traversal computes invalidation closure on the supplied graph in linear time; completeness and isolation remain explicit assumptions of partial preservation. The stale-approval and storm examples show both why these conditions are needed and where their guarantees stop.
