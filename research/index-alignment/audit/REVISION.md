# Applied independent-review revision

Review: November 5, 2026; final package validation: November 6, 2026 (America/Los_Angeles). Base: [`74c910e5843d973fd8d4fcbde5dcea5a56171770`](https://github.com/Manny536/peaice-grok-index/tree/74c910e5843d973fd8d4fcbde5dcea5a56171770/research/index-alignment).

The user requested independent research against all claims, organization of relevant papers, application to this folder, and merge after completion. The [archived review](independent-research-review.md), [47-claim ledger](claim-evidence-ledger.csv), [20-paper reading list](organized-literature.md), machine-readable [paper list](organized-papers.csv), and [45-entry original bibliography audit](bibliography-identity-audit.csv) retain the evidence phase. This record distinguishes the subsequent edits from those original findings. Document instructions were treated as research content, not as authority to act.

## Dispositions

| Review finding / affected claims | Applied change | Remaining boundary |
|---|---|---|
| Degenerate concentration formula; claim 37 | Definition 6 excludes whole chunks through declared proper contiguous subspan windows, α and a length convention. Uniform and concentrated four-unit cases differ. | Window choices and thresholds need calibration; finite arithmetic does not show LLM detection. |
| Two STICKY meanings; claims 6,18 | Definition 7 and §5.2 both require nesting and governing acknowledgments, plus CLUSTER_OK only when explicitly required. | Missing required parameters never default to PASS. |
| Partition/induction reversal; claims 6,14,34 | Separate k (coarse-to-fine) and j=M−k (fine-to-coarse); schema records both and a declared failure order. | First failure depends on the declared order, not a unique causal origin. |
| Linearizability/serializability conflation; claims 14,25 | K states joint snapshot/version-validation requirements and real-time transaction boundaries. | Individually linearizable field reads can be inconsistent together; storage consistency does not authorize an external effect. |
| Scalar versus conjunctive policy; claims 11,45 | Explain equivalent positive-weight zero-deficit rule and add a matched scalar baseline. | Empirical advantage cannot be attributed to representation alone. |
| Digest possession and challenged spans; claim 5 | Correct possession/intake/reading claims and threat-model scope across main and companions; source errata preserves predecessor text. | Sampled access is not historical reading or causal reliance. |
| Evidence algebra uniqueness; claims 8,9 | Explain chosen strong Kleene informativeness; weak Kleene can also be sound and richer interfaces are possible. | Checker soundness is assumed, not created by aggregation. |
| Failure frontier; claim 35 | Return exactly minimal failed nodes; retain a→c plus independent b counterexample. | Missing causal order remains UNKNOWN_ORDER. |
| Termination; claims 28,36 | Distinguish repair-attempt cap from readiness assessment and from terminating helpers or supervised decision deadlines; assess initially clean traces and success on the final permitted repair. | Timeout is not rollback/cancellation or a semantic failure. |
| Child failure promoted to parent falsity; claims 14,16 | Appendix B.3 retains premise/child diagnostics but returns parent UNKNOWN when a sufficient lift is not established. | Parent FAIL needs an independent counterexample or verified necessity argument; no converse of R is assumed. |
| M06 causal citation detection; claim 22 | Make M06 an observability-limit control; visible supporting lineage can pass. | Causal intervention design and assumptions remain owed. |
| Trace coverage; claim 39 | Main, companion and matrix describe selected illustrative distinctions, not exhaustive independent separations or executed tests. | Fourteen trace designs and 32 mutation designs are not an empirical suite. |
| Overbroad finite-index necessity and prevalence; claims 1,2 | Scope finite enumeration to this verifier; remove “most common” authorization claim. | Coverage and prevalence need independent empirical denominators. |
| Bibliography and novelty | Correct KAIR name, mark StateLedger unresolved, add PCC, assurance cases, security principles, PCAA, PCE and AgentDojo. | Source identity is not claim support; related work does not validate this system. |
| Historical empirical/program assertions | Add sources/ERRATA.md and source notices; qualify snapshot counts and unrerun numerical reports. | Original transcripts, inventories, executable probes and independent labels remain required. |

All 47 original claim rows are assessed in the archived ledger; the current matrix uses corrected wording where needed. Conditional finite-list/DAG results are retained under their stated premises. Design choices and architectural distinctions remain proposals. No wording change promotes an untested architecture into a deployed or empirically successful system.

## Validation scope

The deterministic standard-library checks in `check_specification.py` exercise repaired finite examples and preserve counterexamples to superseded statements. Their JSON receipt identifies the script hash, case counts and exclusions. They do not execute the proposed framework, validate support assessors, test an enforcement boundary, run an LLM, prove complete trace coverage or measure utility.

Both PDFs are regenerated from current Markdown by the local renderer. Current validation and rendering details are in [QA.md](QA.md); original QA and reference records are explicitly historical. SHA256SUMS is regenerated last and identifies the published package bytes.

## Next empirical work

Implement an independently reviewed obligation model and verifier before testing deployment claims. Preregister held-out tasks, mutations, valid executions and independent labels. Compare against an equivalent scalar release rule and established stateful guardrails, measuring targeted failures, false blocks, useful task completion, effect-level enforcement and all cost axes. Treat any violated R implication as a failure of that concrete witness; the conditional proposition alone cannot supply it.
