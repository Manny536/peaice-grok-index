# Independent research review: Boolean Index Alignment

> Archived pre-revision review of commit `74c910e5843d973fd8d4fcbde5dcea5a56171770`. Statements below about no files being changed describe the review phase. See [REVISION.md](REVISION.md) for the applied corrections; this snapshot is retained so the original assessment is auditable. Local working paths in its receipt describe that review environment.

**Verdict: PARTIAL PASS — RETAIN WITH OBLIGATIONS.** The package contains a coherent proposed certification architecture and several elementary conditional arguments. Independent literature supports important distinctions it uses. It does not establish the architecture's empirical efficacy, complete observability, semantic checker soundness, useful partial release, or cost savings. Several specific statements need correction before the package can be presented as a fully checked formal account.

Reviewed on November 5, 2026. Authoritative repository revision: [74c910e5843d973fd8d4fcbde5dcea5a56171770](https://github.com/Manny536/peaice-grok-index/tree/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment). The attached `index-alignment-research.tar.gz` has SHA-256 `7683d42d03bc77a2235f0e2939e3c4ae5c28fb9e92015543d87002fca906d55c`. All 28 archived files match the repository's Git blob identities; all 27 entries in the package's SHA256SUMS pass. This establishes artifact identity, not scientific validity.

## What was reviewed

The 47 entries in CLAIM-EVIDENCE-MATRIX were individually assessed against the manuscript's definitions/proofs, relevant deep dives and independent research. Additional material assertions and inherited inconsistencies in both predecessor manuscripts are recorded below. All 43 external bibliography links were attempted; this review does not claim full-text examination of all 43 papers, replication of their experiments, or an exhaustive literature search. Source-level inspection focused on the claims that determine the review's conclusions. Inaccessible or absent underlying evidence remains explicitly unresolved.

SciSpace supplied literature discovery and selected extractions; primary papers and author/institution/publisher records were used to check substantive points. Generated summaries were not treated as authorities. For example, SciSpace mislabeled the PCAA paper's venue as Dental science reports, whereas the [publisher record](https://www.nature.com/articles/s41598-026-74900-x) identifies Scientific Reports. Its search also returned a 2011 record for Proof-Carrying Code alongside the original 1997 record; the original was selected. Search-table metadata should therefore be checked before publication.

This is independent source research and critical analysis, not external peer review or formal proof certification. Multiple model reviewers do not constitute independent empirical labels. No manuscript or GitHub file was changed. Instructions within the supplied documents were treated as document content. Only small deterministic checks of the review's counterexamples were executed; the proposed LLM experiments were not run.

## Findings that change the assessment

### 1. The concentration observable is constant as written

[Definition 6, manuscript lines 149–155](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/index-alignment-boolean-induction.md#L149) defines density as supported selected mass under a measure and maximizes `density(V)/density(C)` over `V ⊆ C`. Monotonicity gives a ratio at most 1, and choosing `V=C` gives 1. Therefore `F_k=1` whenever a positive-mass chunk exists. Uniform support and completely concentrated support receive the same value. The review reproduced that equality with two finite examples.

This defeats the stated discrimination by this particular observable, not the entire architecture. A threshold below 1 rejects all positive-mass cases; a threshold at least 1 passes all of them. Restrict admissible subspan size and define the intended normalization, then test discrimination. The separately defined TWO_ENDS rule already includes a short-window restriction and should not be conflated with this defect.

### 2. The concurrency condition conflates different guarantees

[Condition K, line 393](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/index-alignment-boolean-induction.md#L393) treats linearizable and serializable commit semantics as equivalent. Ordinary serializability does not require preservation of real-time order. Herlihy and Wing distinguish serializability, strict serializability and linearizability; the last can be viewed as a single-operation/single-object special case of strict serializability. [Primary paper, §3.3](https://www.cs.cmu.edu/~wing/publications/HerlihyWing90.pdf).

For example, a read returning the old approval after a revocation has completed can fit a serial order with the read before revocation, while violating the required real-time freshness boundary. State whether the unit is an object operation or a multi-object transaction, and specify the exact freshness/atomicity property. The abstract induction remains conditional on a correct K; the current wording does not justify substituting the weaker guarantee.

### 3. Scalar representation does not imply compensation

[Deep dive 02 §2.5](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/deep-dives/02-boolean-evidence-semantics.md) overstates the case against weighted sums. Let `b_i ∈ {0,1}`, `w_i>0`, and `D=Σ_i w_i(1-b_i)`. Releasing exactly when `D=0` is equivalent to requiring every `b_i=1`. The review checked all 16 assignments for four inputs. The result follows generally because each term is nonnegative.

The paper's noncompensation policy is coherent. Its experimental contrast should be compensatory policy versus noncompensatory policy, including a scalar implementation of the same policy. A weighted sum is differentiable only when the constituent functions and domain permit that claim.

### 4. Citation visibility cannot test all causal citation failures

[Mutation M06, line 1384](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/index-alignment-boolean-induction.md#L1384) expects an ActiveEvidence mismatch for a post-rationalized citation. A document can be visible, support an answer, and still not have influenced generation. Its visible lineage can pass. The manuscript itself acknowledges this in §12.1. Independent work directly distinguishes support from causal reliance. [Wallat et al.](https://scispace.com/papers/correctness-is-not-faithfulness-in-rag-attributions-79sflsthbd3i), [primary paper](https://arxiv.org/abs/2412.18004).

Narrow the fixture to a cited source absent from the activation trace, or specify a separate causal-intervention test. Its result would still be conditional on the intervention design, not direct access to complete neural causation.

### 5. Content receipts have narrower guarantees than some companion text claims

[Deep dive 01 §1.6](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/deep-dives/01-index-foundations.md#L48) says holders of the same digest almost certainly hold the same bytes. A digest can simply be copied; possessing it establishes no possession of the source. Given candidate byte strings, matching cryptographic digests provide an integrity check under the cryptographic assumptions.

A correctly answered unpredictable span challenge supplies evidence of an ability to return sampled content under a stated threat model. It does not prove prior reading, understanding, or causal reliance. The predecessor's statement that a hash alone proves intake also needs qualification. These corrections preserve the manuscript's stronger distinction between integrity and semantics.

### 6. Some algorithms and coverage statements need precise limits

- **Frontier:** Definition 26's set of minimal failures is sound. Its additional clause about failures incomparable with frontier members is ambiguous. For failures `a→c` and independent `b`, the minimal set is `{a,b}`. An 'incomparable with any member' reading also admits `c`; an 'incomparable with all members' reading adds nothing. Return exactly the minimal set. Proposition 4 itself is not refuted.
- **Round caps:** A finite cap bounds iterations, not a nonterminating repair call. Add termination assumptions and enforced timeouts to Appendix B.5.
- **Scale orientation:** Definition 5 increases the partition index toward finer chunks, while §5.3/Proposition 2 increase the obligation index toward parents. State the reverse mapping explicitly. This is a specification ambiguity rather than a counterexample to finite induction.
- **Trace coverage:** Fourteen hand-built traces do not establish that every distinction has an executed separating test. Make the separation inventory explicit and distinguish it from the 32 mutation designs.

## What the evidence does support

The conditional composition proof is an ordinary finite induction: sound base judgments and valid child-to-parent implications yield sound parent judgments while the premises remain valid. R already contains the semantic implication; citations to refinement theory do not establish R for an actual implementation. [Abadi–Lamport](https://scispace.com/papers/the-existence-of-refinement-mappings-4cae6c6ovw) supplies relevant background, with its own assumptions.

Strong Kleene aggregation preserves soundness of constituent verdicts. The review checked 64 sound assignments for three conjuncts; that finite check is supplementary, not a machine proof of the universal proposition. First-failure uniqueness, finite-DAG minimality, and affected-closure preservation are appropriately elementary or conditional. Their practical bottlenecks are complete obligations, reliable dependency information, semantic assessors and enforced authority boundaries.

Independent attribution, long-context and evaluation research supports separating source availability from support, testing position effects, and avoiding self-generated ground truth. Those studies motivate experiments; they do not validate INDEX-ALIGN-CERT. The manuscript correctly says its 14 traces and 32 mutations are designs, and its proposed real-transcript evaluation has not been performed.

The Kakeya sources establish geometric results within their mathematical settings. The manuscript's explicit prohibition on transferring those conclusions into an AI-alignment theorem should be retained. [Wang–Zahl](https://arxiv.org/abs/2502.17655) and [Guth–Wang–Zahl](https://arxiv.org/abs/2601.14411) do not validate this architecture or its thresholds.

## Additional and inherited claims

| Location / claim | Independent assessment | Required correction or evidence |
|---|---|---|
| 2026a §5A.4: routing entropy tending to zero yields a dense model | Incorrect in general. A fixed top-1 route has zero route entropy and still activates one expert. | Describe degenerate fixed routing/underused capacity; distinguish routing entropy from number of activated experts. |
| 2026a §5.8: expected pollution grows as Θ(tpq) | An informal hypothesis. The recurrence, exposure count, deletion/overwrite dynamics and dependence assumptions are unspecified. A bounded occupancy measure can saturate. | Define the random variable and process; derive the expression or present it only as a toy scenario. Joint proposer/policy failure probabilities cannot be multiplied without the needed dependence assumptions. |
| 2026a §§5.5/5.7: index echoing makes faithfulness checkable; membership equals faithfulness | Too strong. Echoing provides identifiers; it does not force their use or entailment. The continuation improves this distinction. | Correct or annotate the predecessor so the package does not retain contradictory claims. |
| 2026a §5A.2: capability isolation lifts recursively | A desired implementation invariant, not a consequence of assigning router names. | Establish complete mediation and effective privilege separation at every child boundary. |
| 2026a continuity-repair discussion: empirical repair systems as existence proofs | Improvement on examples does not prove a globally contractive operator or convergence to C*. | Keep contractivity as a mathematical conjecture requiring a metric, domain, fixed point and proof. |
| 2026b §2.2: KNS fan multiplicity / Δ_max asymptotics | Insufficiently specified for independent proof from this package alone. | Supply direction separation/coverage, tube length and domain, measure, normalization and the referenced lemma; no Kakeya citation substitutes for these. |
| 2026b prime-carrying route called LIVE·FORCED after other lanes closed | Rejection of named alternatives does not establish exhaustion of alternatives. | Use research-priority status unless an exhaustive classification and exclusion argument is supplied. |
| 2026b §9.2: two paired-turn Benevolence Drift cases and internal classification | The main manuscript says only Case 01 has a forced-binary follow-up in the supplied material. Changed responses do not identify latent classification or a care-proxy causal mechanism. | Separate visible transcript observations, interpretive hypothesis and causal claim; supply original evidence and controlled alternatives before promotion. |
| Main §11.10: 110 runs / 539 tests; neighboring 7/8 predictions; predecessor numerical receipts | Source-reported claims, not independently reproduced here. Test counts alone cannot establish targeted detection, effect or transfer. | Pin executable code, environment, raw output and independent expectation labels; retain failed predictions. |
| Main §13.4 / Appendix F: 26 snapshots, 177,064,129 bytes, 717 extracted texts | The local handoff inventory underlying these numbers is not in this research archive. | Mark as attributed handoff counts; supply manifest if these totals matter. Extraction remains distinct from reading. |
| Deep dive 01 §1.3: registry/permission confusion is the most common authorization bug | Comparative prevalence is unsupported by the cited examples. | Remove the superlative or provide a representative error study with denominator. |
| Deep dive 01 §1.1: indices/finite enumeration are necessary for any meaningful boolean claim | Too broad outside the declared finite checker. Boolean propositions exist independently of whether this representation observes or decides them. | Restrict to what this verifier can finitely inspect under its model. |
| Deep dive 02: weak Kleene is wrong; exactly three values are forced | Weak Kleene conjunction can be sound but less informative; richer or abstaining monitor interfaces are possible. | Explain the chosen diagnostic benefit without claiming logical uniqueness. |
| GraphAnchor naming | The cited current primary work calls its method KAIR. Its evolving keyword/relation/RDF index supports the indexing description, so the issue is the name, not a fabricated graph mechanism. | Use KAIR and pin the relevant version. [Primary §3.2](https://arxiv.org/html/2601.16462v2). |
| StateLedger, reference 23 | The given NeurIPS page was inaccessible and exact-title searches did not recover a confirming primary record in this review. This is not proof that the work does not exist. | Supply a stable primary record or mark the citation unresolved. |
| Personal/evaluator h<1; RH/Coleman and other cross-program status labels | Stipulations, open problems or imported program records; no independent empirical/privacy/theorem certification is supplied by the labels. | Preserve their declared scope. Do not convert program status into a mathematical result or measured score. |

## Missing related work and fair comparisons

The related-work section should compare against existing certificate and enforcement traditions, not only routing and attribution papers:

1. [Necula, Proof-Carrying Code (1997)](https://scispace.com/papers/proof-carrying-code-47tcuiaiuz): a small consumer checker validates supplied safety evidence against policy. Compare trusted bases and specification assumptions.
2. [Chaki et al., Assurance Cases for Proofs as Evidence (2009)](https://scispace.com/papers/assurance-cases-for-proofs-as-evidence-11zvavg03o): addresses the gap between proof, model and actual software. The [NASA record](https://ntrs.nasa.gov/citations/20150004720) includes Charles Weinstock as a fourth author.
3. [Saltzer–Schroeder (1975)](https://cgi.cse.unsw.edu.au/~cs9242/20/papers/Saltzer_Schroeder_75.pdf): relevant foundations for least privilege, fail-safe defaults, separation of privilege and complete mediation.
4. [Kadyrbek–Mansurova, PCAA (2026)](https://scispace.com/papers/proof-carrying-agent-actions-enable-verifiable-licensing-of-krfhxn4h0e9t): a closely related planner-independent action-certificate checker. The publisher reports a small certificate battery and microbenchmark, with guarantees relative to trusted tool contracts. Its matched stateful guardrail is an especially useful baseline; these results do not validate the present framework.
5. [Liu Yanglet et al., No Certificate, No Execution (2026)](https://scispace.com/papers/no-certificate-no-execution-certified-traces-as-a-foundation-lj747n8uytg2): a closely related trace-level proposal/certification/execution framework. Compare certificate scope, conformance and composition assumptions. Treat it as formal/proposal background, not field efficacy evidence.
6. [AgentDojo](https://scispace.com/papers/agentdojo-a-dynamic-environment-to-evaluate-attacks-and-4201ufpfov): an independently developed environment for testing agent attacks and defenses on useful tasks. Use held-out scenarios and report utility as well as security failures.

These overlaps require precise positioning. They do not by themselves negate a contribution from the particular four-predicate integration, correction protocol or partial-release interface. Originality and practical advantage remain questions to demonstrate.

## Bibliographic audit boundary

There are 45 entries: two same-author unpublished manuscripts and 43 external works. Thirty-six linked primary pages were accessible directly; six older works were identified through primary-paper copies or author/institutional records when DOI routes failed. Reference 23, StateLedger, remains unresolved in this review. Metadata identity is not full-content verification or claim support. Years may denote preprint versus publication, so version and venue should be explicit; the FOCS 2024 attribution for the open-addressing paper is confirmed by the [conference paper](https://ieee-focs.org/FOCS-2024-Papers/pdfs/FOCS2024-1oojWxXs5YAKfs3z3lBRMF/167400a594/167400a594.pdf), despite its later arXiv submission.

The original package's 43/43 verification record is a prior reported check. This review does not silently reuse it as current proof that every URL is accessible or that each citation supports each claim.

## Promotion conditions and next experiment

**Pass condition for a corrected formal package:** fix the concrete formula, concurrency, receipt and scalar statements; reconcile indexing and frontier semantics; restrict M06; make every claimed separation traceable to an explicit fixture; preserve the conditional/proposed labels.

**Pass condition for an efficacy claim:** release an executable verifier and independently labeled, preregistered evaluation of false global acceptance, missed violations, false blocks, correction races, useful partial output and total cost. Use clean controls, held-out faults, semantic assessor calibration and matched baselines. Record execution and effects separately. No useful numerical threshold can be supplied honestly without the intended workload and risk tradeoff.

**Failure condition:** an in-scope trace violates a declared invariant but receives CERTIFIED, or a claimed necessary mechanism fails to outperform an equivalent policy baseline under the preregistered metric. A failed implication falsifies that concrete R witness; it does not falsify the tautological theorem that assumes R.

**Kill criterion:** withdraw the corresponding certification claim upon a reproducible false acceptance under the stated assumptions. Abandon claims of a distinctive empirical advantage if matched comparisons show none. Do not rescue a failed test by changing thresholds after observing outcomes; start a new specification epoch.

**Smallest next action:** correct the specification, then implement one narrow externally checkable action family with current authority, one shared budget, one correction race and one independently releasable output. That experiment can test whether the proposed distinctions produce safe, useful behavior without assuming the desired result.

The following ledger records a disposition for each of the 47 listed claims. A design or conditional argument marked retainable is not promoted to empirical validation.


## All 47 claims: evidence ledger

### 1. Sparse-system failures are usefully analyzed as mismatches among typed discrete indices

**Disposition: PROPOSED; motivation supported.** MoE, RAG and tool-use papers establish discrete selections. Treating their failures as typed-index mismatches is a useful candidate abstraction, not an independently established exhaustive taxonomy.

**Owed:** Compare against non-index failure taxonomies on independently labeled real traces; report what the abstraction misses.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L7); manuscript §1.1, §3.1; deep dive 01 §1.1–1.2. External evidence: [Reference 3](https://arxiv.org/abs/1701.06538), [Reference 5](https://arxiv.org/abs/2101.03961), [Reference 6](https://arxiv.org/abs/2401.04088), [Reference 11](https://arxiv.org/abs/2005.11401), [Reference 15](https://arxiv.org/abs/2302.04761).

### 2. Registry liveness and policy permission are distinct predicates

**Disposition: SUPPORTED DISTINCTION; design-specific predicates.** Resource existence/liveness does not entail a principal's permission to use it. The registry and policy separation is coherent; enforcing it requires an authenticated permission boundary.

**Owed:** Test live-but-forbidden resources, stale epochs, principal substitution and all bypass routes.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L8); manuscript Def. 1–2, §4.2, Trace B; deep dive 01 §1.3; 04 §4.2. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf), [Additional source 1](https://cgi.cse.unsw.edu.au/~cs9242/20/papers/Saltzer_Schroeder_75.pdf).

### 3. Gate weight is telemetry, not permission or quality

**Disposition: SUPPORTED WITH SCOPE.** A learned routing weight is not an authorization certificate or a factuality guarantee. It can still correlate with task utility, so the narrower 'does not establish quality' wording is preferable to 'contains no quality information'.

**Owed:** Calibrate route quality independently; preserve permission as a separate check.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L9); manuscript Def. 2, §2.3; deep dive 01 §1.4; 04 §4.2. External evidence: [Reference 3](https://arxiv.org/abs/1701.06538), [Reference 4](https://arxiv.org/abs/2006.16668), [Reference 5](https://arxiv.org/abs/2101.03961), [Reference 7](https://arxiv.org/abs/2407.06204).

### 4. Citation lineage generalizes pointer discipline and is necessary but not sufficient for support

**Disposition: CONSTRUCTION; support distinction established.** Pointer Networks support input-index selection, not cross-store provenance soundness. Lineage is necessary under this declared contract, not for every possible truthful answer, and does not establish entailment.

**Owed:** Validate each cross-store mapping and compare lineage-only versus support-aware checks.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L10); manuscript Def. 3, §4.4; deep dive 01 §1.5; 04 §4.4. External evidence: [Reference 10](https://arxiv.org/abs/1506.03134), [Reference 27](https://aclanthology.org/2023.cl-4.2/), [Reference 28](https://arxiv.org/abs/2305.14627).

### 5. A hash binds bytes but does not show reading; independent challenged spans are required

**Disposition: CORRECTION NEEDED.** A digest binds candidate bytes under cryptographic assumptions; possession of a digest does not prove possession of those bytes. Deep dive 01 overstates this. Challenged spans supply sampled content evidence, not proof of historical reading, understanding or causal use; they are one possible mechanism, not universally necessary.

**Owed:** Correct deep dive 01 §1.6 and predecessor 2026b §7.5; define the challenge threat model and success/failure probabilities.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L11); manuscript Def. 4, §8.5; deep dive 01 §1.6; 06 §6.8. External evidence: [Reference 29](https://arxiv.org/abs/2412.18004), [Additional source 1](https://doi.org/10.1145/263699.263712).

### 6. Scales are declared audit levels, not model or training scales

**Disposition: DEFINITION; notation clarification needed.** Declared audit levels are explicitly distinct from parameter/training scale. Definition 5 increases k toward finer partitions, while §5.3 and Proposition 2 increase k toward parent obligations; an explicit reverse-index mapping is missing.

**Owed:** Define the correspondence between P_k and Q_k, and use distinct names for partition depth and induction level.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L12); manuscript Def. 5, §5 intro; deep dive 01 §1.7; 03 §3.1. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 7. Happened-before, not wall clocks, determines ORDER

**Disposition: SUPPORTED WITH CONTRACT SCOPE.** Happened-before gives causal partial order; unsynchronized wall-clock order alone cannot establish it. A chosen total display order must not create causal edges, and clock order does not authenticate an issuer.

**Owed:** Test clock skew, missing message edges, cycles and independent concurrent events.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L13); manuscript Def. 14; deep dive 01 §1.9; 05 §5.3. External evidence: [Reference 45](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).

### 8. Semantic A/C predicates are boolean under a fixed spec; monitor verdicts must be three-valued

**Disposition: QUALIFICATION NEEDED.** Boolean semantic predicates and inconclusive monitoring are coherent. Bauer et al. supports a three-valued monitoring design, not the universal claim that every sound monitor must have exactly three values. Abstention and richer evidence algebras are alternatives.

**Owed:** Replace 'must be three-valued' with the specific T/F/U design requirement adopted here.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L14); manuscript §4.1, §5.1; deep dive 02 §2.1–2.2. External evidence: [Reference 41](https://christian.schallhart.net/publications/2011--tosem--runtime-verification-for-ltl-and-tltl.pdf).

### 9. Strong Kleene aggregation of sound verdicts is sound (Prop. 1)

**Disposition: SCOPED FORMAL ARGUMENT HOLDS.** Strong Kleene conjunction preserves sound positive and negative verdicts given sound constituent verdicts. The proof does not validate the primitive checkers or make the aggregation complete. The review also checked 64 sound assignments for three conjuncts.

**Owed:** Specify checker assumptions; mechanize the general result if claiming machine-checked certification.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L15); manuscript §6.1; deep dive 02 §2.3. External evidence: [Reference 41](https://christian.schallhart.net/publications/2011--tosem--runtime-verification-for-ltl-and-tltl.pdf).

### 10. PASS-only release bit; UNKNOWN and NO_VERDICT kept distinct; no hidden defaults

**Disposition: DESIGN RULE.** PASS-only release is a conservative control choice. UNKNOWN and NO_VERDICT can share the inconclusive semantic value while retaining different diagnostic reasons. Neither reason is an observed violation.

**Owed:** Test each missing-evidence/contract path and preserve mixed reasons in the actual decision object.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L16); manuscript §4.1, App. A.1, B.1, Trace I; deep dive 02 §2.4. External evidence: [Reference 41](https://christian.schallhart.net/publications/2011--tosem--runtime-verification-for-ltl-and-tltl.pdf).

### 11. Release must be non-compensatory; the scalar deficit can be telemetry only

**Disposition: CORE RULE VALID; SCALAR EXCLUSION FALSE AS STATED.** Necessary release conditions may be conjunctive. However a nonnegative weighted deficit with positive weights and release iff its value is zero implements the same rule. Deep dive 02's blanket claim that scalar sums must compensate is false; differentiability also needs assumptions.

**Owed:** Compare compensatory versus noncompensatory decision policies, including an equivalent scalar baseline, rather than boolean versus scalar representations.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L17); manuscript §2.1, §4.9; deep dive 02 §2.5. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 12. Non-vacuity blocks release; empty denominators report n/a (Prop. 6)

**Disposition: SCOPED FORMAL ARGUMENT HOLDS.** If NONVACUOUS is required, PASS-only conjunction blocks release when it does not pass. Reporting an empty denominator as n/a is sound accounting. An independently established empty task must remain distinct from a missing log.

**Owed:** Test empty logs, genuinely empty tasks and missing obligation inventories.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L18); manuscript Def. 27, §6.6; deep dive 02 §2.7. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 13. Kakeya induction supplies an order of work, not an implication

**Disposition: STRUCTURAL ANALOGY ONLY; boundary supported.** The cited Kakeya works concern geometric dimension/volume results. They supply no LLM predicate, authority rule or empirical alignment guarantee. A useful audit schedule can be inspired by them without inheriting their theorems.

**Owed:** Retain explicit no-transfer wording and test any claimed advantage of the schedule independently.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L19); manuscript §1.2, §2.2, §2.6; deep dive 03 §3.1; 09 §9.7. External evidence: [Reference 24](https://arxiv.org/abs/2502.17655), [Reference 25](https://arxiv.org/abs/2601.14411), [Reference 26](https://arxiv.org/abs/2411.08871).

### 14. Sound local certificates lift across scales under R, C, N, K (Prop. 2)

**Disposition: CONDITIONAL PROOF; CONCURRENCY SPEC NEEDS REPAIR.** The induction follows if the local verdicts are sound and R already establishes each child-to-parent semantic implication. C/N/K preserve the premises; citations do not discharge them. Condition K incorrectly treats serializability as equivalent to linearizability.

**Owed:** State operation/transaction boundaries and the required real-time property; implement and independently check R/C/N/K witnesses.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L20); manuscript §5.4–5.7, §6.2; deep dive 03 §3.3–3.4. External evidence: [Reference 40](https://lamport.azurewebsites.net/pubs/abadi-existence.pdf), [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf), [Reference 44](https://www.cs.cmu.edu/~wing/publications/HerlihyWing90.pdf).

### 15. Local passes do not compose without cross-operation obligations

**Disposition: VALID COUNTEREXAMPLE.** Two locally allowed expenditures of 60 violate a shared parent cap of 100. Local acceptance alone cannot establish this global invariant. This establishes a failure possibility, not the proposed checker's detection rate.

**Owed:** Test concurrent reservations and omitted cross-operation obligations with known global labels.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L21); manuscript §6.11, Trace K; deep dive 03 §3.7. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 16. Certificates are defeasible when any premise changes (Prop. 9)

**Disposition: SCOPED FORMAL ARGUMENT HOLDS.** A proof relying on an invalidated premise no longer justifies its old conclusion. This withdraws that proof path; it does not imply the proposition is false or that no alternative valid proof exists.

**Owed:** Track premise identities and alternative certificate paths explicitly.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L22); manuscript §6.9; deep dive 03 §3.5; 05 §5.10. External evidence: [Reference 40](https://lamport.azurewebsites.net/pubs/abadi-existence.pdf).

### 17. Required constraints are retained on a finite DAG under stated hypotheses (Prop. 8)

**Disposition: CONDITIONAL STRUCTURAL RESULT.** Finite-DAG retention follows from base coverage, edge preservation and admission of all new governing records. Complete mediation and absence of hidden execution channels are substantial assumptions; the result does not establish semantic sufficiency or deployed enforcement.

**Owed:** Independently exercise every execution boundary and retain effect evidence, including bypass attempts.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L23); manuscript §6.8; deep dive 03 §3.8. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf).

### 18. Stable-custody nesting uses per-registry acknowledgments, not global version comparison

**Disposition: PROPOSED DESIGN.** Per-registry acknowledgments avoid comparing unrelated version counters. They still require authenticated registry identity, current policy semantics and verified supersession. No external paper validates this exact acknowledgment construction.

**Owed:** Test independent registries, counter reset/reuse, missing ancestors and concurrent supersessions.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L24); manuscript §5.2; deep dive 03 §3.6. External evidence: [Reference 45](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).

### 19. A_route, A_ledger, A_gen, A_cont operationalize the four 2026a consistency relations

**Disposition: DEFINITIONAL CROSSWALK; empirical coverage OPEN.** The four predicate families implement the author's chosen routing, ledger, generation and continuity relations. Agreement with the predecessor is internal consistency, not independent evidence that these predicates capture all relevant failures.

**Owed:** Obtain external specification review and report false acceptance on failures outside the four-family taxonomy.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L25); manuscript §4.2–4.5, App. E; deep dive 04 §4.1–4.5. External evidence: [Reference 3](https://arxiv.org/abs/1701.06538), [Reference 11](https://arxiv.org/abs/2005.11401), [Reference 15](https://arxiv.org/abs/2302.04761), [Reference 20](https://arxiv.org/abs/2310.08560).

### 20. Order is not authority; append-only is not isolation

**Disposition: SUPPORTED DISTINCTION.** An ordered or append-only log can preserve an unauthorized write perfectly. Ordering and durability do not establish access control or noninterference.

**Owed:** Test authority-table modification through retrieved content and shared process state.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L26); manuscript §4.3, §5.6, Trace L; deep dive 04 §4.3; 06 §6.3. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf), [Reference 45](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).

### 21. Coverage is not fidelity

**Disposition: SUPPORTED DISTINCTION.** Retrieving or accounting for all required sources does not entail that a generated claim follows from them. Attribution evaluation treats support as a separate question.

**Owed:** Use complete-source but unsupported-conclusion controls with independent labels.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L27); manuscript §4.4, Trace C; deep dive 04 §4.4. External evidence: [Reference 27](https://aclanthology.org/2023.cl-4.2/), [Reference 28](https://arxiv.org/abs/2305.14627).

### 22. Exposed lineage is not proof of causal reliance

**Disposition: SUPPORTED; MUTATION M06 CONTRADICTS THE LIMIT.** Visible activation and a supporting citation do not prove causal reliance. M06 cannot reliably detect post-rationalized citations using ActiveEvidence alone when the cited document was visible but unused.

**Owed:** Narrow M06 to absent activation, or add a specified causal-intervention protocol with its own limitations.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L28); manuscript §12.1; deep dive 04 §4.4. External evidence: [Reference 29](https://arxiv.org/abs/2412.18004).

### 23. Continuity is preserved obligations across compression and handoff

**Disposition: PROPOSED OPERATIONALIZATION.** Memory and agent studies motivate durable context. They do not prove that arbitrary compression/handoff preserves every required obligation. The manuscript's predicate is a contract-relative definition, not a measured continuity guarantee.

**Owed:** Measure obligation loss across compression, resume and handoff using independently enumerated requirements.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L29); manuscript §4.5, Trace N; deep dive 04 §4.5. External evidence: [Reference 20](https://arxiv.org/abs/2310.08560), [Reference 21](https://arxiv.org/abs/2304.03442), [Reference 22](https://arxiv.org/abs/2608.03699).

### 24. Authority requires S·H·U from channels content cannot supply; Act=0 ⇏ Stop

**Disposition: STIPULATED AUTHORITY POLICY.** S·H·U is a conjunction of selected authority conditions, not an independently established universal authority law. Denying one privileged action can permit other output only when that output has its own authorization and dependencies.

**Owed:** Define and authenticate S/H/U inputs; test ambiguous intent, delegated authority and emission-specific permissions.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L30); manuscript Def. 9; deep dive 06 §6.3. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf), [Additional source 1](https://www.nature.com/articles/s41598-026-74900-x).

### 25. Signed is not fresh; stale approvals yield U or F, never T

**Disposition: SUPPORTED WITH FRESHNESS POLICY.** A valid signature can authenticate a historically valid approval while current authorization has changed. The U/F outcome depends on the specified revocation/effect-boundary policy; vector clocks alone do not decide it.

**Owed:** Test revocation races, effect-time revalidation and replay using corrected concurrency semantics.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L31); manuscript §6.11, Trace E; deep dive 05 §5.4. External evidence: [Reference 44](https://www.cs.cmu.edu/~wing/publications/HerlihyWing90.pdf), [Reference 45](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).

### 26. Correction invalidation is reachability over the dependency graph; whole closure is rechecked

**Disposition: CONSTRUCTION; graph completeness assumed.** Reachability computes affected nodes in a supplied dependency graph. It cannot discover missing dependencies, shared caches or unlogged side effects, and cannot retract already emitted copies.

**Owed:** Compare closure against an independently constructed dependency oracle and inject missing edges.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L32); manuscript §5.8, §8.1, App. B.4; deep dive 05 §5.6. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf).

### 27. Unaffected outputs keep their certificates under isolation (Prop. 7)

**Disposition: CONDITIONAL PROOF HOLDS.** Unchanged inputs and absence of all modeled/unmodeled influence preserve a deterministic predicate. Partial-release safety therefore rests on complete dependencies and N, rather than disjoint graph labels alone.

**Owed:** Test hidden shared context, shared budgets and policy changes affecting apparently separate outputs.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L33); manuscript §6.7, Trace G; deep dive 05 §5.7. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf).

### 28. Round caps guarantee termination, not correctness

**Disposition: QUALIFICATION NEEDED.** A finite round cap bounds iterations. It guarantees total termination only if every repair, checker and I/O operation terminates or is interrupted by an enforced timeout. Appendix B.5 leaves repair and recheck abstract.

**Owed:** Add per-operation deadlines/cancellation and distinguish timeout from semantic failure.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L34); manuscript §5.8, Trace H, App. B.5; deep dive 05 §5.9. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 29. Repetition by many agents is not authority

**Disposition: SUPPORTED DISTINCTION.** Conformity experiments show that multi-model agreement can reflect social influence; agreement itself neither creates permission nor establishes independent evidence. This does not show that every ensemble is ineffective.

**Owed:** Measure error correlation and adjudicate against external labels rather than vote counts alone.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L35); manuscript §8.1; deep dive 05 §5.2. External evidence: [Reference 34](https://arxiv.org/abs/2310.13548), [Reference 35](https://arxiv.org/abs/2501.13381).

### 30. Custody is not truth

**Disposition: SUPPORTED CONCEPTUAL DISTINCTION.** Custody records can establish which artifact was retained under what conditions without proving the artifact's claims true. The predecessor's framework terminology is a design convention.

**Owed:** Keep integrity, source reliability, entailment and truth assessments separate.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L36); manuscript §1.4, §5.2; deep dive 06 §6.2. External evidence: [Reference 27](https://aclanthology.org/2023.cl-4.2/), [Additional source 1](https://ntrs.nasa.gov/citations/20150004720).

### 31. Selection, gate, execution, and effect must be recorded separately

**Disposition: SOUND MEASUREMENT DESIGN; imported results NOT replicated.** Selection, gate output, execution and observed effect are different events. The manuscript reports neighboring AIce synthetic figures but explicitly did not rerun them; those figures do not establish this package's efficacy.

**Owed:** Pin raw AIce inputs/outputs and independently reproduce the reported run before using it as validation.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L37); manuscript §6.8, §7.2, §10.4; deep dive 06 §6.4. External evidence: [Additional source 1](https://github.com/Manny536/AIce).

### 32. STRUCTURAL_READY is distinct from RELEASE_FULL

**Disposition: PROPOSED DESIGN.** Structural readiness can be kept distinct from semantic/authority release. The names are policy-defined states; they do not supply the external support or authority checks they require.

**Owed:** Test structurally complete records with invalid support, scope or permission.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L38); manuscript §5.10; deep dive 06 §6.5. External evidence: [Additional source 1](https://arxiv.org/abs/2605.24462).

### 33. Five outcomes; authorized unaffected partial output survives blocked full release

**Disposition: PROPOSED DESIGN; useful partial release OPEN.** Five outcomes are a coherent interface choice. Whether unaffected authorized output survives in practice depends on isolation, complete dependencies, correct labels and an enforced emission boundary.

**Owed:** Benchmark utility and false partial release under hidden dependencies and semantic UNKNOWN.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L39); manuscript §8.3–8.4, Trace M; deep dive 06 §6.6–6.7. External evidence: [Reference 43](https://www.cs.purdue.edu/homes/ninghui/readings/AccessControl/goguen_meseguer_82.pdf).

### 34. First failure is unique on a total order (Prop. 3)

**Disposition: SCOPED ELEMENTARY RESULT HOLDS.** A nonempty finite totally ordered failure set has a unique minimum; a fixed tie order identifies one reported conjunct. This is not a unique causal diagnosis or proof that the actual root cause was observed.

**Owed:** Evaluate whether the reported location predicts a useful repair site on labeled traces.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L40); manuscript §6.3; deep dive 07 §7.2. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 35. Concurrent failures form a frontier on a DAG (Prop. 4)

**Disposition: PROPOSITION VALID; FRONTIER RETURN RULE AMBIGUOUS.** Finite nonempty failure sets in a DAG have minimal elements. Definition 26's extra incomparable-members clause is redundant if it means all members and can include nonminimal failures if it means any member.

**Owed:** Return exactly Min(F); test a→c plus independent b, whose minimal frontier is {a,b}.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L41); manuscript §6.4, Trace F; deep dive 07 §7.3. External evidence: [Reference 45](https://lamport.azurewebsites.net/pubs/time-clocks.pdf).

### 36. Localization is finitely computable under terminating checkers (Prop. 5)

**Disposition: SCOPED COMPUTABILITY RESULT HOLDS.** Finite enumeration plus terminating predicate checks and graph traversal terminates. It says nothing about general semantic discovery, repair search, or practical latency.

**Owed:** State termination assumptions for every primitive and report timed-out/incomplete checks separately.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L42); manuscript §6.5; deep dive 07 §7.4. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 37. Two-ends and directional checks detect concentration that totals miss

**Disposition: PARTIAL; ONE CONCENTRATION FORMULA IS DEGENERATE.** Explicit window/direction coverage can expose distributions hidden by totals. However F_k in Definition 6 maximizes submass/full mass while allowing V=C, so F_k=1 for every positive-mass chunk. It cannot discriminate concentration as stated.

**Owed:** Restrict window size and normalize the intended density; test uniform versus concentrated support. Treat threshold usefulness as empirical, not imported geometry.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L43); manuscript Def. 17, 25; deep dive 07 §7.5. External evidence: [Reference 26](https://arxiv.org/abs/2411.08871).

### 38. Position effects motivate location-stratified coverage

**Disposition: SUPPORTED MOTIVATION; generality LIMITED.** Lost in the Middle documents positional effects in its evaluated models/tasks. It motivates location-stratified testing, not a universal middle-loss law or validation of this paper's windows.

**Owed:** Re-estimate positional effects for the actual models, context sizes, tasks and prompt formats used.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L44); manuscript §12.2, Trace D; deep dive 07 §7.6. External evidence: [Reference 30](https://aclanthology.org/2024.tacl-1.9/), [Reference 31](https://arxiv.org/abs/2404.01261).

### 39. The fourteen traces jointly exhibit every separation the framework draws

**Disposition: EXHAUSTIVE COVERAGE NOT ESTABLISHED.** The fourteen written traces illustrate many distinctions, but an exhaustive independently checked separation-to-trace map is absent. Status inflation, vacuity and independence receive mutation designs; a written fixture is not a successful test execution.

**Owed:** Define the finite list of claimed separations, map each to a minimal pair, and execute the suite.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L45); manuscript §9; deep dive 07 §7.8. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 40. Restricted certificate verification is O(n + #edges + cB + r + w) (Prop. 10)

**Disposition: RESTRICTED BOUND PLAUSIBLE; assumptions essential.** The stated O(n+|E|+cB+r+w) follows from bounded primitives, a shared traversal, bounded window checks and at most one support call per claim. Real hashing/input lengths, signatures, sorting and repeated traversals must be charged when not constant.

**Owed:** Implement the restricted witness format and instrument total work versus input bytes and graph structure.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L46); manuscript §6.10, §10.2; deep dive 08 §8.8. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 41. Verification cost does not classify search; D1–D9

**Disposition: CORRECT NON-CLAIM.** Efficient verification of supplied restricted evidence does not classify route discovery, natural-language support or general Index Alignment as P, NP or NP-hard. No such reduction is provided.

**Owed:** Retain the explicit complexity boundary; specify encodings and computational models before stronger claims.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L47); manuscript §10.3–10.4; deep dive 08 §8.8. Basis: direct inspection of the stated construction, proof or counterexample; no external study is claimed to validate it.

### 42. Detection requires clean baseline and attributable named failure; nonzero exit is not detection

**Disposition: SOUND EVALUATION REQUIREMENT.** A harness crash or arbitrary nonzero exit is not evidence that the intended fault was detected. An evaluable clean control and attributable named failure distinguish diagnostic performance from infrastructure failure.

**Owed:** Require structured outcome reasons, fixed clean baselines and predeclared exclusions in the executable harness.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L48); manuscript §11.6, Trace J; deep dive 08 §8.3. External evidence: [Reference 33](https://arxiv.org/abs/2503.12651), [Additional source 1](https://arxiv.org/abs/2406.13352).

### 43. Labels must be independent; model agreement is not independence

**Disposition: SUPPORTED REQUIREMENT; independence must be operationalized.** Sycophancy, conformity and summarization-evaluation failures motivate external labels. Separate model names or agent roles do not establish independent errors or epistemic independence.

**Owed:** Blind raters, use independent specifications, disclose shared data/models, and estimate correlated errors.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L49); manuscript §11.2, §12.3; deep dive 08 §8.4. External evidence: [Reference 27](https://aclanthology.org/2023.cl-4.2/), [Reference 31](https://arxiv.org/abs/2404.01261), [Reference 34](https://arxiv.org/abs/2310.13548), [Reference 35](https://arxiv.org/abs/2501.13381).

### 44. Criteria must be versioned as epochs

**Disposition: SUPPORTED MOTIVATION; epoch design PROPOSED.** EvalGen studies evolving criteria. Versioned epochs are a reasonable engineering response, not a result that EvalGen proves necessary or sufficient for reliable certification.

**Owed:** Freeze confirmatory criteria, record migrations and retest certificates when applicable criteria change.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L50); manuscript §7.6, §12.4; deep dive 08 §8.4. External evidence: [Reference 38](https://arxiv.org/abs/2404.12272).

### 45. Evaluation compares against scalar, self-assessment, citation-only, coverage-only, global-judge, local-only, human baselines

**Disposition: PROPOSED COMPARISON PLAN.** The baseline list is appropriate research planning, not comparative evidence. Include a scalar encoding of exactly the same noncompensatory policy to avoid attributing policy differences to representation.

**Owed:** Pre-register matched model/context/tool/time budgets and paired comparisons, including partial-release and refuse-all controls.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L51); manuscript §11.7; deep dive 08 §8.7. External evidence: [Reference 32](https://arxiv.org/abs/2408.08067).

### 46. Cost of verification must be reported on all axes

**Disposition: SUPPORTED REPORTING PRACTICE; no savings demonstrated.** Selective verification and human-centered evaluation motivate explicit cost accounting. They do not establish that this framework saves tokens, latency, energy or review effort.

**Owed:** Measure all stated cost/utility axes, including repair and false blocks, with uncertainty and workload scope.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L52); manuscript §11.8; deep dive 08 §8.8. External evidence: [Reference 33](https://arxiv.org/abs/2503.12651), [Reference 36](https://arxiv.org/abs/2505.03814), [Reference 37](https://aclanthology.org/2025.findings-acl.18/).

### 47. Certificates cannot settle who owns the specification

**Disposition: SUPPORTED LIMIT; governance remains external.** A certificate establishes conformance to a chosen specification under assumptions; it cannot itself establish the legitimacy, ownership or adequacy of that specification. Governance scholarship motivates this boundary.

**Owed:** Identify authorized specification owners, appeal mechanisms and revision authority outside the certifier.

[Package claim](https://github.com/Manny536/peaice-grok-index/blob/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment/CLAIM-EVIDENCE-MATRIX.md#L53); manuscript §12.4; deep dive 09 §9.5; 02 §2.9. External evidence: [Reference 39](https://facctconference.org/static/papers24/facct24-124.pdf).

## Reproducibility receipt

The companion bundle contains the 47-row ledger, organized paper guide, bibliography identity audit, counterexample script/results, and file-identity receipts. The counterexample script checks only the stated finite examples and does not implement or test INDEX-ALIGN-CERT.
