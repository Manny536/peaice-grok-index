# 09 — Related Work and Annotated Bibliography

*Backs manuscript §§2, 12 and the References section. The initial package reported a metadata/URL check in `audit/reference-verification.md`. The subsequent independent review distinguishes source identity from claim support and leaves StateLedger unresolved. A resolving link or matching title is not full-text validation or empirical replication.*

## 9.1 How the literature is used

The manuscript draws on five bodies of work, and uses each for a different purpose. Sparse-computation and agent papers supply the *objects* — the indices the certificate inspects. Attribution and evaluation papers supply the *failure modes* the predicates are built to separate. Formal-methods papers supply the *proof techniques* for composition. Kakeya geometry supplies an *order of work*. Governance work supplies the *boundary* of what a technical certificate can settle. Keeping those roles distinct is itself part of the argument: no cited work is used as evidence for something it does not study.

## 9.2 Sparse experts and routing

**Shazeer et al. (2017), *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*, ICLR; arXiv:1701.06538.** Introduces noisy top-k gating over thousands of experts with a load-balancing loss. Source of the gated routing decision `R_t = TopK(softmax(W_r x))` used in Coleman (2026a). Its gate is a learned affinity, which is why the manuscript treats gate weight as telemetry.

**Lepikhin et al. (2020), *GShard*, arXiv:2006.16668.** Top-2 routing with expert capacity and automatic sharding. Motivates the `Budget` clause: capacity is a declared, checkable constraint.

**Fedus, Zoph, and Shazeer (2022), *Switch Transformers*, JMLR; arXiv:2101.03961.** Top-1 routing and simplified load balancing; `K_t = 1` case.

**Jiang et al. (2024), *Mixtral of Experts*, arXiv:2401.04088.** Top-2 among eight experts per layer; the concrete MoE configuration in Coleman (2026a).

**Cai, W. et al. (2024), *A Survey on Mixture of Experts in Large Language Models*, arXiv:2407.06204.** Survey of gating variants; cited for the breadth of routing designs `A_route` must accommodate.

**Yue et al. (2024), *Ada-K Routing*, arXiv:2410.10456.** Dynamic per-token expert counts; motivates treating `K` as a declared budget rather than a constant.

**Cai, R. et al. (2024), *Read-ME*, arXiv:2410.19123.** Decouples the router from the backbone; cited in Coleman (2026a) as inspiration for router/authority separation.

## 9.3 Pointers, retrieval, and indexing

**Vinyals, Fortunato, and Jaitly (2015), *Pointer Networks*, NeurIPS; arXiv:1506.03134.** Outputs are indices into the input. The generation predicate's `Lineage` clause generalizes this guarantee across stores.

**Lewis et al. (2020), *Retrieval-Augmented Generation*, NeurIPS; arXiv:2005.11401.** Generation conditioned on retrieved passages; the baseline setting for `A_gen`.

**Kim and Diaz (2025), *LTRR: Learning To Rank Retrievers for LLMs*, arXiv:2506.13743.** Routing among retrievers; retriever choice is itself an index.

**Wu, M. et al. (2026), *Finding What Matters: Anchoring Context Knowledge with Evolving Indices for Iterative Retrieval*, arXiv:2601.16462.** The current primary version names the method **KAIR**, not GraphAnchor. Its evolving keyword/relation index uses RDF triples and motivates versioned index identity. The source supports this indexing mechanism, not the present certificate's efficacy.

**Liang et al. (2024), *Empowering Large Language Models to Set up a Knowledge Retrieval Indexer via Self-Learning*, arXiv:2405.16933.** Referred to as PG-RAG. A model-built indexer means the index structure itself is a generated artifact whose provenance must be tracked.

## 9.4 Tools, agents, and memory

**Schick et al. (2023), *Toolformer*, arXiv:2302.04761** and **Yao et al. (2023), *ReAct*, ICLR; arXiv:2210.03629.** Expose tool calls and action–observation steps as discrete events, the raw material of the event trace.

**Wu, Q. et al. (2023), *AutoGen*, arXiv:2308.08155; Hong et al. (2023), *MetaGPT*, arXiv:2308.00352; Fourney et al. (2024), *Magentic-One*, arXiv:2411.04468.** Multi-agent orchestration; Magentic-One's orchestrator maintains task and progress ledgers. These systems produce agent indices and handoffs that `A_route` and `A_cont` inspect.

**Packer et al. (2023), *MemGPT*, arXiv:2310.08560; Park et al. (2023), *Generative Agents*, arXiv:2304.03442.** Bounded-context memory management and memory-stream summarization. Compression is where obligations can be lost, motivating `A_cont.Obligation` and Trace N.

**Xiao et al. (2026), *TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents*, arXiv:2608.03699.** Transactional agent memory; source of the proposal/commit separation in Coleman (2026a)'s ledger.

**Yang, Liu, Wu, and Wang (2026), *StateLedger: Path-Addressed External Memory for Persistent Multi-Agent Systems*, claimed NeurIPS 2026 poster. UNRESOLVED.** The given page was inaccessible and no confirming primary record was recovered in the independent review. This is not proof of nonexistence; the citation remains unverified and is not used to support a substantive claim until a stable primary record is supplied.

## 9.5 Attribution, faithfulness, and evaluation

**Rashkin et al. (2023), *Measuring Attribution in Natural Language Generation Models*, Computational Linguistics 49(4).** Defines Attributable to Identified Sources (AIS). The conceptual basis for separating `Fidelity` from `Lineage`.

**Gao et al. (2023), *Enabling Large Language Models to Generate Text with Citations* (ALCE), EMNLP; arXiv:2305.14627.** Citation recall/precision measured separately from correctness.

**Wallat, Heuss, de Rijke, and Anand (2024), *Correctness is not Faithfulness in RAG Attributions*, arXiv:2412.18004.** A correct citation need not be the one causally used. Grounds the manuscript's limit on `ActiveEvidence`.

**Liu et al. (2024), *Lost in the Middle*, TACL.** Position-dependent use of long contexts; motivates location-stratified coverage tests (Trace D).

**Kim, Y. et al. (2024), *FABLES*, COLM; arXiv:2404.01261.** Book-length faithfulness and omission annotation; motivates omission checks and claim-level sampling.

**Ru et al. (2024), *RAGChecker*, NeurIPS; arXiv:2408.08067.** Module-level RAG diagnosis; nearest diagnostic neighbor.

**Sung, Kim, and Zhang (2025), *VeriLA*, arXiv:2503.12651.** Human-centered, criteria-based agent failure verification.

**Wan et al. (2025), *Derailer-Rerailer*, Findings of ACL.** Adaptive verification for reasoning; motivates staged checks.

**Wang, G. et al. (2025), *Cer-Eval*, arXiv:2505.03814.** Certifiable, cost-efficient evaluation; motivates cost-aware selective verification.

**Sharma et al. (2024), *Towards Understanding Sycophancy in Language Models*, ICLR; arXiv:2310.13548** and **Weng, Chen, and Wang (2025), *Do as We Do, Not as You Think: The Conformity of Large Language Models*, ICLR; arXiv:2501.13381.** Preference-tracking and conformity; ground the rule that model agreement is not independent evidence.

**Shankar et al. (2024), *Who Validates the Validators?* (EvalGen), UIST; arXiv:2404.12272.** Criteria drift during grading; grounds criteria versioning.

**Grill (2024), *Constructing Capabilities: The Politics of Testing Infrastructures for Generative AI*, FAccT; doi:10.1145/3630106.3659009.** Testing infrastructure as sociotechnical and political; grounds the governance boundary in §12.4.

## 9.6 Formal methods for composition

**Lamport (1978), *Time, Clocks, and the Ordering of Events in a Distributed System*, CACM 21(7); doi:10.1145/359545.359563.** Happened-before; Definition 14.

**Goguen and Meseguer (1982), *Security Policies and Security Models*, IEEE S&P; doi:10.1109/SP.1982.10014.** Noninterference; condition N.

**Herlihy and Wing (1990), *Linearizability*, ACM TOPLAS 12(3); doi:10.1145/78969.78972.** Operation-level real-time semantics and its distinction from serializability/strict serializability; condition K must state the appropriate boundary explicitly.

**Abadi and Lamport (1991), *The Existence of Refinement Mappings*, TCS 82(2); doi:10.1016/0304-3975(91)90224-P.** Refinement mappings; condition R.

**Bauer, Leucker, and Schallhart (2011), *Runtime Verification for LTL and TLTL*, ACM TOSEM 20(4); doi:10.1145/2000799.2000800.** Three-valued finite-trace monitor semantics; the `U` verdict.

**Farach-Colton, Krapivin, and Kuszmaul (2024/2025), *Optimal Bounds for Open Addressing Without Reordering*, FOCS 2024; arXiv:2501.02305.** Expected-probe bounds in hash tables; used only as a methodological neighbor through the open-addressing probe.

## 9.7 Geometry as an order of work

**Wang and Zahl (2025), *Volume estimates for unions of convex sets, and the Kakeya set conjecture in three dimensions*, arXiv:2502.17655** and **Guth, Wang, and Zahl (2026), *A streamlined proof of the Kakeya set conjecture in ℝ³*, arXiv:2601.14411.** Full dimension of Kakeya sets in `ℝ³`. Coleman (2026b) reads the proof's architecture — sticky case, non-sticky two-scale grains, slab/plank factoring, residual — as an order for custody organization. The manuscript borrows that order and no inequality.

**Wang and Wu (2024), *Restriction estimates using decoupling theorems and two-ends Furstenberg inequalities*, arXiv:2411.08871.** Source of the two-ends vocabulary behind `TWO_ENDS`.

The authors of these geometric works are not affiliated with this research.

## 9.8 The author's former papers

**Coleman (2026a), *Index Alignment in Large Language Models: Sparse Routing, State Ledgers, and Generative Continuity*.** Defines index alignment through four consistency relations, the alignment deficit `Δ_t`, capability isolation, and sparse Mixture-of-Agents. The continuation converts each relation into a predicate family and requires a noncompensatory release policy. Scalar encodings can implement the same policy. The historical source is preserved with a linked [errata record](../sources/ERRATA.md).

**Coleman (2026b), *Kakeya Grain at the Slab: Induction on Scales, Continuous Direction, and Prime-Carrying Custody under Love-Squared Coherence*.** Supplies the sticky-first order of work, HELD custody, the `Act = S·H·U` authority gate with `Act = 0 ⇏ Stop`, the `h < 1` evaluator boundary, non-compensatory grain vectors, and the object firewall between geometry and other programs.

## 9.9 Position of this work

The proposed contribution is the particular integration of four predicate families, witness paths, correction handling and partial-release decisions for exposed sparse-system indices. Noncompensatory release can be encoded as conjunction or an equivalent scalar rule. The construction applies established refinement, noninterference and monitoring ideas under stated assumptions; it does not establish a deployed checker or empirical advantage. Its geometric vocabulary supplies an organizational analogy. Positioning against proof-carrying code and agent-action certificates is necessary before making broader novelty claims.


## 9.10 Certificate and enforcement comparisons

**Necula (1997), *Proof-Carrying Code*, POPL; doi:10.1145/263699.263712.** Foundational consumer-side checking of supplied safety evidence. Compare the policy language, trusted checker and implementation assumptions; the presence of a certificate does not validate those assumptions.

**Chaki, Gurfinkel, Wallnau, and Weinstock (2009), *Assurance Cases for Proofs as Evidence*.** [NASA primary record](https://ntrs.nasa.gov/citations/20150004720). Connects mathematical proof to actual system behavior through explicit assurance arguments about assumptions, models and implementations.

**Saltzer and Schroeder (1975), *The Protection of Information in Computer Systems*.** [Primary paper copy](https://cgi.cse.unsw.edu.au/~cs9242/20/papers/Saltzer_Schroeder_75.pdf). Least privilege, separation of privilege, fail-safe defaults and complete mediation are relevant prior foundations for the proposed authority boundary.

**Kadyrbek and Mansurova (2026), *Proof carrying agent actions enable verifiable licensing of language model tool use*, Scientific Reports; doi:10.1038/s41598-026-74900-x.** A close comparison for planner-independent action-certificate checking. The publisher reports a small certificate battery and microbenchmark with guarantees relative to trusted tool contracts. A matched stateful guardrail is a useful baseline; these results do not validate INDEX-ALIGN-CERT.

**Liu Yanglet, Wang, and Capponi (2026), *No Certificate, No Execution: Certified Traces as a Foundation for Trustworthy AI Agents*, arXiv:2605.24462.** A related proposal/certification/execution architecture at trace level. Compare conformance, proof memory, composition and trusted assumptions; this is formal/proposal background, not independent field evidence for the present system.

**Debenedetti et al. (2024), *AgentDojo*, arXiv:2406.13352.** An independently developed adversarial agent-task environment. It motivates testing useful task completion alongside security failures using held-out tasks and attacks.
