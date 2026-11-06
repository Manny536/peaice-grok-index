# 04 — Routing, Ledger, and Generative Continuity: The Four Predicate Families

*Backs manuscript §§2.1, 2.3–2.5, 3.3–3.5, 4.2–4.5, 7.1–7.5, Appendix E, Traces B, C, N.*

## 4.1 From four consistency relations to four predicate families

Coleman (2026a, Definition 1) declared a system state `(R_t, L_t, y_{1:t}, C_t)` index-aligned when four relations hold: routing–capability, routing–ledger, generation–index, and continuity–ledger consistency. The continuation keeps that decomposition and replaces each informal relation with a conjunction of named, separately checkable clauses. The crosswalk in Appendix E records the correspondence; this deep dive explains why each clause is in its family and what failure it isolates.

## 4.2 `A_route`: routing is a proposal, not a judgment

`A_route(k) := ∀r ∈ RequiredRoutes(k), Typed ∧ Live ∧ Permitted ∧ Budget ∧ Parent ∧ Admissible`.

- **Typed** and **Live** rely on deep dive 01: the index is well-formed and the registry entry it names exists, is valid at this epoch, and matches its digest.
- **Permitted** applies policy `Π_k` for the authenticated principal.
- **Budget** checks declared sparsity, cost, and latency. In MoE terms this covers top-k limits and expert capacity factors (Lepikhin et al., 2020; Fedus et al., 2022); in agent systems, the number of agents activated per step (Coleman 2026a, Definition 4, sparse Mixture-of-Agents).
- **Parent** checks ancestry: a fine route must descend from a declared coarse route.
- **Admissible** applies a task-specific rule when one is part of the contract and must be explicitly declared out of scope otherwise.

The family deliberately excludes semantic expert quality. Routing literature studies load balance, entropy, and router collapse (Cai et al., 2024 survey; Yue et al., 2024 on dynamic expert counts; Cai et al., 2024 Read-ME on router decoupling). Those are optimization concerns. A low-entropy route can be right for a narrow task and a balanced route wrong. §2.3 therefore states that `A_route` "does not declare an oracle expert from routing entropy alone." What it does certify — that the selected index is real, current, permitted, budgeted, and parented — is narrower and checkable.

Trace B shows the family's diagnostic value. Expert `e7` is typed, live, within budget, with normal gates and load balance. Policy permits privileged repository transformations only on `e8`. `Permitted = F`, so `A_route = F` and `FIRST_FAIL = 0 (A_route.Permitted)`. A scalar routing score would have been excellent.

### Soft mixtures

§7.1 notes that a soft mixture with no hard expert identity may fall outside the routing contract. The correct response is reduced scope or `UNKNOWN`, not an invented discrete index. This keeps the framework honest about what is observable: if a system does not expose discrete selections, the routing family cannot certify them.

## 4.3 `A_ledger`: authority lives at the commit boundary

`A_ledger(k) := PROV ∧ AUTH ∧ TRANSITION ∧ NOSILENT ∧ COV ∧ ORDER ∧ CORR`.

Coleman (2026a, §3.2) made the ledger the authority for durable commitments: routers and generators propose, only accepted transitions change committed state. That mirrors transactional designs for agent memory such as TARL (Xiao et al., 2026), from which Coleman (2026a) draws its ACCEPT/PEND/REJECT/SUPERSEDE action types. The package's StateLedger citation (Yang et al., 2026) remains unresolved in the independent review and is not relied on as verified support. Magentic-One (Fourney et al., 2024) uses task and progress ledgers in its orchestrator. The continuation's contribution is to name the clauses a ledger must satisfy for its authority to be certified rather than assumed.

The seven clauses are separated in pairs that are commonly conflated:

- **PROV vs COV.** One cited lineage on an accepted record (PROV) does not show that every required unit was received (COV).
- **ORDER vs AUTH.** Happened-before (ORDER) shows which write came first; it does not authenticate the writer (AUTH). Lamport clocks order events; they do not grant permission.
- **COV vs CORR.** Complete intake (COV) does not show that later corrections reached dependents (CORR).
- **TRANSITION vs NOSILENT.** A transition can satisfy schema and still overwrite an accepted fact; NOSILENT requires a supersession link and that the prior record remain queryable.

`AUTH` uses the three-factor authority evidence of Definition 9, `Act(x) = 1` iff `S(x) = H(x) = U(x) = 1`, from the L²_C authority-detection rule in Coleman (2026b, §7.2): authenticated source authority, hierarchy validity, and authorized user intent. The continuation adds a third value: any `0` makes `Act = 0`; otherwise any `UNKNOWN` makes `Act = UNKNOWN`. This is the evidence algebra of deep dive 02 applied to authority, and it is why "coverage, stickiness, a found receipt, causal order, or model agreement never sets `S(x) = 1`."

The name "ledger" confers none of these properties (§7.2). An append-only store can faithfully preserve an unauthorized write; immutability is integrity of history, not legitimacy of content. Trace L — a retrieved instruction that rewrites the authority table — fails N and AUTH while every append-only guarantee holds.

## 4.4 `A_gen`: citation membership is necessary and insufficient

`A_gen(k) := ∀q, Lineage ∧ ActiveEvidence ∧ Fidelity ∧ StatusType ∧ Scope ∧ AttributionCompleteness`.

Coleman (2026a) stated generation–index consistency as "claims cite indices that were actually activated." That is the pointer discipline of Vinyals et al. (2015) applied to citations, and it prevents one failure: citing an inactive identifier. It does not prevent the more serious failure of attaching a real identifier to a sentence the source does not support. The attribution literature measures exactly that gap. AIS (Rashkin et al., 2023) defines attribution as whether a generated statement is supported by an identified source and builds human annotation protocols for it. ALCE (Gao et al., 2023) evaluates citation recall and precision separately from fluency and correctness. Wallat et al. (2024) show that citation correctness and causal faithfulness diverge: a cited document can support an answer without being the document the model relied on.

The continuation responds by splitting the relation:

- **Lineage** — every cited index has a witnessed path, no failed cast.
- **ActiveEvidence** — the evidence was visible in a snapshot accessible to the claim.
- **Fidelity** — a declared assessor labels the claim and all required ancestors `SUPPORTED`; none is `UNSUPPORTED` or unquarantined `CONTESTED`.
- **StatusType** — the claim does not assert a stronger kind than its source (strategy reported as proved, analogy as measurement).
- **Scope** — measured claims stay within the tested workflow and validity interval.
- **AttributionCompleteness** — every claim class requiring attribution has a supporting citation.

Trace C is the canonical demonstration: every chunk receipted, order valid, every citation active, and the conclusion says a dose was doubled when the source says halved. `Fidelity = F`, `A_gen = F`. Even with Fidelity, the paper keeps one limit explicit: `ActiveEvidence` certifies the exposed trace, not internal causal reliance — the gap Wallat et al. identify cannot be closed by adding citation IDs.

`StatusType` and `Scope` are unusual in generation checks and deserve emphasis. Many harmful outputs are not false; they are overstated. A strategy reported as a proof, or a result measured on one workflow reported as general, passes a support check on its content and fails on its kind. Falsifiers SEM-003 and SCOPE overclaim (§11.9) target these.

## 4.5 `A_cont`: continuity is preserved obligations, not fluent prose

`A_cont(k)` conjoins Projection, Obligation, Handoff, CorrectionContinuity, Directional, and NoAuthorityInflation.

Coleman (2026a, §3.3) measured continuity with a score `Cont(y, C) ∈ [0,1]`. The continuation turns that score into finite obligations that must survive a specific transformation — compression, handoff, resume. The continuity state `C_k = (facts, discourse, goals, corrections)` must be a declared projection of the committed ledger view; every open obligation must remain open or carry an authorized satisfaction or waiver; every route change, handoff, resume, and compression must emit a checkpoint; active corrections must be carried; required directions of relevance (deep dive 07) must remain covered; and the continuity expert must not have acquired commit authority.

The motivating literature is agent memory. MemGPT (Packer et al., 2023) pages context in and out of a bounded window; Generative Agents (Park et al., 2023) summarize memory streams into reflections. Both compress, and compression is where obligations get lost. Trace N is the canonical case: after compression, the ledger still holds an open obligation to verify a source version, but the summary omits it. Routing, ledger, and generation pass; `Obligation = F`, `Handoff = F`. "A beautifully written continuation can fail Projection; an awkward one can pass."

NoAuthorityInflation enforces Coleman (2026a)'s capability isolation table (Definition 3): the continuity expert may emit text and propose summaries, but owns no factual authority and may not mutate the ledger. A continuity summary can be internally consistent and wrong, and "projection consistency is not factual support, and support is not user authority."

## 4.6 Role-to-predicate matrix

§7.5 assigns each component the predicates that test it and the inference it may not make. The matrix is a compact statement of capability isolation as testable obligations: the router may not infer authority, the retriever may not infer support, the tool gateway may not infer success from selection, the ledger may not infer truth from append order, the generator may not infer support from IDs, the continuity expert may not infer commit authority, and the release controller may not infer promotion from coverage. Each row names a typical first failure, which gives evaluators a concrete starting point for fault injection.

## 4.7 What this layer establishes

The four families operationalize Coleman (2026a)'s four consistency relations as conjunctions of independently failing clauses. The clause boundaries are drawn exactly where the cited literature reports conflation in practice: gate weight vs permission, order vs authority, citation vs support, summary vs commitment. Each family can fail while the others pass, and the worked traces exhibit each such failure.
