# Index Alignment in Large Language Models: Sparse Routing, State Ledgers, and Generative Continuity

> Historical source text. Read with the [source errata and inherited-claim limits](ERRATA.md). This notice does not convert the source’s proposals, numerical reports or program labels into independently validated results.

**Authors:** Manuel Coleman$^{1}$ \\
$^{1}$AgreeYa Solutions (Computacenter), Folsom, CA, USA \\
Correspondence: manuel.coleman@lovelabslca.com

**Status:** Research draft (arXiv-style). Sections marked *Proposal* introduce framing and architectures that synthesize prior work rather than claiming completed empirical validation.

---

## Abstract

Large language models (LLMs) increasingly operate as *conditionally computed* systems: Mixture-of-Experts (MoE) layers activate sparse parameter subsets per token; multi-agent frameworks activate sparse agent subsets per subtask; retrieval-augmented generation (RAG) activates sparse document subsets per query. Across these regimes, correct behavior depends less on any single activated module than on whether the *indices* that name modules, memory entries, tools, and discourse commitments remain aligned with the evolving computational state. We call this requirement **index alignment**.

This paper develops a research framework for index alignment in LLMs. We formalize indices as typed pointers into expert banks, agent teams, external memory, and tool registries; define alignment as consistency between routed indices, ledgered state, and generated continuations; and propose a role taxonomy that separates (i) **non-authoritative routers**, which propose sparse activations without owning world state, (ii) **state ledgers**, which provide append-oriented, provenance-bearing records of accepted commitments, and (iii) **generative continuity experts**, which specialize in maintaining coherence across long horizons. We situate the proposal in established literature on sparsely gated MoE (Shazeer et al., 2017; Lepikhin et al., 2020; Fedus et al., 2022; Jiang et al., 2024), pointer networks (Vinyals et al., 2015), tool-using LMs (Schick et al., 2023), multi-agent orchestration (Wu et al., 2023; Fourney et al., 2024), and persistent agent memory (Packer et al., 2023; recent ledger-style memory systems). Framing that goes beyond prior empirical results is marked as **proposal**. We outline evaluation protocols for routing fidelity, ledger consistency, continuity retention, and end-to-end sparse Mixture-of-Agents (MoA) performance under capability isolation.

**Keywords:** index alignment, Mixture-of-Experts, sparse activation, multi-agent systems, sparse Mixture-of-Agents, non-authoritative routers, state ledgers, generative continuity experts, retrieval-augmented generation, tool use, agent orchestration, capability isolation

---


## 1. Introduction

### 1.1 Motivation

Scaling laws for dense transformers establish that quality improves with parameter count and data, but dense activation makes every parameter participate in every forward pass (Kaplan et al., 2020; Hoffmann et al., 2022). Conditional computation reframes scale: capacity can grow while per-example FLOPs stay roughly constant if only a sparse subset of modules is activated (Bengio et al., 2013; Shazeer et al., 2017). In contemporary LLMs this idea appears at several layers of the stack:

1. **Parameter sparsity.** Mixture-of-Experts (MoE) layers route each token to a small set of feed-forward experts (Lepikhin et al., 2020; Fedus et al., 2022; Jiang et al., 2024; Cai et al., 2024).
2. **Retrieval sparsity.** RAG systems retrieve a sparse set of passages or index nodes conditioned on a query (Lewis et al., 2020; Gao et al., 2024; LTRR, 2025; GraphAnchor, 2026).
3. **Tool sparsity.** Tool-augmented LMs decide *whether* and *which* APIs to invoke (Schick et al., 2023; Yao et al., 2023).
4. **Agent sparsity.** Multi-agent systems activate specialized agents under an orchestrator rather than running every agent on every step (Wu et al., 2023; Hong et al., 2023; Fourney et al., 2024).

What these regimes share is an **index**—a discrete pointer naming which expert, document, tool, agent, or memory path participates next. Failures often look like generation errors when they are actually *index* errors: a router selecting the wrong expert, an orchestrator calling the wrong agent, a retriever returning an off-topic chunk, or a memory write that silently overwrites a still-valid commitment. We argue that treating these phenomena uniformly under **index alignment** clarifies both theory and system design.

### 1.2 Thesis

**Thesis (Index Alignment).** In sparse activation models and multi-agent LLM systems, reliability is governed by the consistency of discrete indices that bind (a) routing decisions, (b) durable state, and (c) generative continuations. Routers should be *non-authoritative*—they propose activations but do not unilaterally rewrite world state. Durable commitments should live in *state ledgers* with provenance. Long-horizon coherence should be supported by *generative continuity experts* whose specialization is maintaining narrative, plan, and constraint continuity rather than owning factual authority.

This thesis is partly descriptive of existing practice (MoE routers already do not "own" parameters; Magentic-One-style orchestrators already maintain structured ledgers; MemGPT-style systems already page memory by reference) and partly **proposal** (unifying these as index alignment; requiring capability isolation between router, ledger, and continuity roles; defining sparse Mixture-of-Agents as an indexed sparse activation pattern over agents).

### 1.3 Contributions

This draft contributes:

1. **A formal definition of index alignment** for LLMs spanning MoE, RAG, tools, and agents (Section 3).
2. **A role taxonomy** separating non-authoritative routers, state ledgers, and generative continuity experts, with capability isolation as a design principle (Section 4).
3. **A method sketch** for sparse Mixture-of-Agents (MoA) with typed indices, ledger commits, and continuity scoring (Section 5).
4. **An evaluation design** measuring routing fidelity, ledger consistency, continuity retention, and end-to-end task success (Section 6).
5. **A literature-grounded discussion** relating index alignment to MoE routing, pointer networks, agent orchestration, and memory systems, clearly labeling speculative extensions (Sections 2, 7–8).

### 1.4 Scope and non-claims

We do **not** claim a new trained frontier model, nor completed large-scale experiments in this draft. Empirical numbers cited from prior work are attributed; metrics proposed for future evaluation are labeled as such. We deliberately avoid proprietary framework branding and focus on transferable systems vocabulary used in the open literature.

---


## 1.5 Worked Motivating Scenarios

### Scenario A: MoE misrouting under distribution shift

A production sparse decoder (Mixtral-style top-2 among 8 experts) serves both code and natural language. Under a sudden shift to underrepresented dialectal text, the router concentrates mass on a small expert subset—classic load imbalance. Surface symptoms include degraded fluency; root cause is an **index distribution failure**. Load-balancing auxiliaries (Shazeer et al., 2017; Fedus et al., 2022) and adaptive $K$ (Ada-K) are index-health interventions. If operators only finetune the decoder head, they treat a routing problem as a generation problem.

### Scenario B: RAG with unaligned citations

A RAG pipeline retrieves passages $\{d_{i_1},\ldots,d_{i_k}\}$ but the generator cites a plausible DOI never retrieved. Faithfulness metrics catch this post hoc; **generation–index consistency** would catch it as soon as citation IDs leave the activated set $R_t$. GraphAnchor-style evolving indices and LTRR-style retriever routing show the field moving toward treating retrieval choices as controllable indices rather than opaque context blobs.

### Scenario C: Multi-agent memory pollution

Agent A writes `customer_tier = gold` from a stale CRM tool call. Agent B later refunds based on that scratchpad field. TARL-motivated ledgers would have marked the CRM fact with temporal scope and provenance, allowing `REVISE`/`REJECT` when a fresher source arrives. Without a ledger, index names collide (`customer_tier`) while meanings drift—an alignment failure between memory indices and world state.

### Scenario D: Continuity break across handoffs

An Orchestrator switches from `WebSurfer` to `Coder` mid-task. The coding agent does not see the constraint discovered online ("API rate limit 10 QPS"). Continuity-on-handoff activation would force a continuity expert to project constraints into $C_t$ and optionally commit them to the task ledger before the handoff completes. Magentic-One's structured ledgers already gesture at this; we elevate it to a named role.

### Scenario E: Tool registry drift

HuggingGPT-/Toolformer-style systems select tools by name. If a registry renames `calc` to `calculator` without updating policies, routers emit dangling indices. Capability policy $\Pi$ and live registration checks (Definition 1.1) are the alignment patch; retry logic alone is not.

These scenarios motivate a single vocabulary—**indices, routers, ledgers, continuity**—spanning layers that are usually siloed in papers and org charts.

---

## 2. Related Work

### 2.1 Sparse activation and Mixture-of-Experts

Shazeer et al. (2017) introduced the sparsely gated MoE layer: a trainable gating network produces a sparse combination of expert feed-forward networks per example, enabling large capacity at controlled compute (arXiv:1701.06538). GShard scaled MoE Transformers for multilingual translation with top-2 routing and automatic sharding (Lepikhin et al., 2020; arXiv:2006.16668). Switch Transformers simplified routing to top-1 and demonstrated trillion-parameter sparse models (Fedus et al., 2022; arXiv:2101.03961). Mixtral of Experts instantiated sparse MoE in a widely deployed decoder LLM, routing each token to two of eight experts per MoE layer (Jiang et al., 2024; arXiv:2401.04088).

Subsequent work studies *how* routing should work. Ada-K routing dynamically varies the number of activated experts per token (arXiv:2410.10456). Read-ME refactorizes dense LLMs into router-decoupled MoEs and argues for separating routing from the expert backbone for system-friendly scheduling (arXiv:2410.19123). Surveys catalog sparse, dense, and soft gating families (Cai et al., 2024; arXiv:2407.06204). Theoretical and empirical analyses show that *learned* routers confer benefits beyond fixed assignment (Dikkala et al., 2023).

**Connection to index alignment.** In MoE, the router emits expert *indices* (and gates). Misrouting is an index error: the activated parameter subset is wrong even if each expert is well-trained. Load-balancing losses (Shazeer et al., 2017; Fedus et al., 2022) are mechanisms that keep the index distribution healthy—an early form of index hygiene.

### 2.2 Pointers, indices, and retrieval

Pointer Networks use attention as a pointer into input positions rather than as a soft blend, producing outputs that are indices into a variable-length set (Vinyals et al., 2015; arXiv:1506.03134). This lineage is relevant whenever an LLM must *name* an element of a set: an expert, a passage, a tool, or a memory path.

RAG (Lewis et al., 2020) retrieves sparse evidence for generation. Recent work treats retrieval itself as indexed routing: LTRR learns to rank retrievers (including a no-retrieval option) for downstream RAG utility (arXiv:2506.13743); GraphAnchor maintains an evolving graph as an active knowledge *index* during iterative retrieval (arXiv:2601.16462); PG-RAG constructs hierarchical mental indices via self-learning (arXiv:2405.16933). Segment-ordering pointer heads improve paragraph-level coherence (arXiv:2406.04156).

**Connection.** Retrieval IDs, graph node IDs, and passage ranks are indices. Index alignment asks whether the indices that enter the generator match the discourse commitments the generator is about to make.

### 2.3 Tool use and ReAct-style control

Toolformer trains LMs to decide which APIs to call and how to incorporate results (Schick et al., 2023; arXiv:2302.04761). ReAct interleaves reasoning traces with actions and observations (Yao et al., 2023; arXiv:2210.03629). HuggingGPT uses an LLM as a controller that plans tasks and selects specialist models (Shen et al., 2023; arXiv:2303.17580). In all cases, the controller emits *names* (tool IDs, model IDs, argument schemas)—indices into an external capability registry.

### 2.4 Multi-agent systems and orchestration

AutoGen enables multi-agent conversation programming with LLM-, tool-, and human-backed agents (Wu et al., 2023; arXiv:2308.08155). MetaGPT encodes SOPs into multi-agent workflows for software engineering (Hong et al., 2023; arXiv:2308.00352). Magentic-One uses an Orchestrator that plans, tracks progress with structured ledgers, and directs specialized agents (browser, files, code, terminal) (Fourney et al., 2024; arXiv:2411.04468). LEGOMem studies modular procedural memory allocation across orchestrators and task agents (arXiv:2510.04851).

**Connection.** Orchestrators are routers over *agents*. Magentic-One's explicit ledgers are a concrete precursor to our state-ledger role. We generalize and separate authority: the orchestrator proposes; the ledger records accepted state; continuity specialists protect long-horizon coherence.

### 2.5 Memory, state, and ledgers for LLM agents

MemGPT treats the LLM context window as RAM with OS-like paging into external storage (Packer et al., 2023; arXiv:2310.08560). Generative Agents maintain memory streams with retrieval by recency, relevance, and importance (Park et al., 2023; arXiv:2304.03442). Recent work argues that multi-agent memory is a *governance* and consistency problem, not only a retrieval problem (Governed Shared Memory; arXiv:2606.24535). TARL maps memory updates to transactional actions over accepted/pending/rejected ledgers (arXiv:2608.03699). StateLedger proposes path-addressed external memory for persistent multi-agent systems (NeurIPS 2026 poster abstract). MAGE stores collaborative events in temporal hypergraphs for role-aware retrieval (arXiv:2608.29678).

**Connection.** Ledgers and path-addressed stores make indices first-class: a memory path *is* an index; alignment means reads and writes refer to the same durable locations under consistent validity rules.

### 2.6 Continuity in long-form generation

Long-form story and plan generation systems track item states, episode summaries, temporal fact validity, and hierarchical outlines to reduce contradictions (e.g., DOME, FactTrack, SCORE, STORYWRITER; 2024–2025 venues). These systems motivate a dedicated *continuity* specialization: not all experts should be generalists; some should be scored and routed for coherence maintenance.

### 2.7 Positioning

Prior work provides the ingredients—sparse routers, pointers, tools, orchestrators, ledgers, continuity trackers—but rarely treats **index alignment** as the cross-cutting correctness property, nor insists on **capability isolation** among router, ledger, and continuity roles. That synthesis, and the sparse Mixture-of-Agents formalization in Section 5, is the **proposal** of this draft.

---


### 2.8 Sparse activation beyond classical MoE

Not all sparse activation is MoE routing. Activation sparsity inside dense FFNs (many near-zero hidden units) has motivated refactorizations into experts (Read-ME) and fine-grained multi-layer expert partitions (Finedeep; DSMoE). From the index-alignment perspective, converting dense compute into indexed experts *increases* the number of discrete decisions that must stay consistent with logging and serving layers. Systems that refactor dense models into MoE therefore inherit an obligation to expose stable expert indices to downstream telemetry and to any agent wrapper that might treat expert choice as an auditable event.

Soft MoE and expert-merging approaches blur hard indices into continuous mixtures. They can improve trainability but weaken the pointer-like semantics that make generation–index consistency easy to check. We consider hard or top-$K$ indices the friendly setting for alignment auditing; soft mixtures remain valuable baselines when evaluating whether discreteness itself helps or hurts faithfulness.

### 2.9 Agent evaluation harnesses and side effects

Fourney et al. (2024) stress that agent actions have side effects, motivating contained evaluation (AutoGenBench). Side effects are precisely mutations of external indices: filesystems, browsers, tickets, emails. A ledger that only tracks conversational summaries is insufficient when the true world state lives in those external stores. Index alignment therefore pushes toward *hybrid ledgers*: pointers into external systems plus local validity metadata (what was true when we last looked), echoing StateLedger's path-addressed artifacts and governed shared memory's temporal supersession.


## 3. Problem Formulation and Formal Definitions

### 3.1 Notation

Let $x_{1:T}$ be a token sequence (prompt plus generation so far). Let $\mathcal{E} = \{E_1,\ldots,E_N\}$ be a bank of *modules*—MoE experts, agents, tools, retrievers, or continuity specialists—each identified by a discrete index $i \in \{1,\ldots,N\}$. Let $\mathcal{M}$ be an external memory address space with paths (indices) $p \in \mathcal{P}$. Let $\mathcal{T}$ be a tool registry with tool IDs $u \in \mathcal{U}$.

An **index** is a typed discrete reference drawn from one of these spaces:

$$
\iota \in \mathcal{I} \;=\; \mathcal{I}_{\mathrm{expert}} \;\cup\; \mathcal{I}_{\mathrm{agent}} \;\cup\; \mathcal{I}_{\mathrm{mem}} \;\cup\; \mathcal{I}_{\mathrm{tool}} \;\cup\; \mathcal{I}_{\mathrm{doc}}.
$$

A **routing decision** at step $t$ is a sparse set of indices with optional gates:

$$
R_t = \{( \iota_k, g_k )\}_{k=1}^{K_t}, \qquad g_k \ge 0,\; \sum_k g_k = 1 \text{ (when gates are used)}.
$$

For classical top-$K$ MoE (Shazeer et al., 2017; Fedus et al., 2022):

$$
h(x_t) = W_r x_t, \qquad
p_i(x_t) = \frac{e^{h(x_t)_i}}{\sum_j e^{h(x_t)_j}}, \qquad
R_t = \mathrm{TopK}(p(\cdot)).
$$

For Switch routing, $K_t=1$ (Fedus et al., 2022). For Mixtral-style layers, $K_t=2$ among $N=8$ experts (Jiang et al., 2024).

### 3.2 State ledgers

A **state ledger** $L$ is an append-oriented sequence of records

$$
L = (\ell_1,\ell_2,\ldots,\ell_m), \qquad
\ell_j = (\tau_j,\; a_j,\; \iota^{\mathrm{subj}}_j,\; v_j,\; \pi_j,\; s_j),
$$

where $\tau_j$ is a timestamp or logical clock, $a_j$ is an action type (e.g., `ACCEPT`, `PEND`, `REJECT`, `SUPERSEDE` as in TARL-style designs), $\iota^{\mathrm{subj}}_j$ is the indexed subject (memory path, claim ID, plan node), $v_j$ is a value or payload, $\pi_j$ is provenance (which agent/tool/document justified the write), and $s_j$ is a validity status.

**Authoritativeness.** The ledger is the authority for durable commitments. Routers and generators may *propose* records; only accepted ledger transitions change the committed state. This mirrors the separation between proposal and commit in transactional memory designs for agents (TARL; governed shared memory).

Define the **committed view** at time $t$:

$$
\mathrm{View}(L_t) = \{ (\iota, v) : \iota \text{ has an accepted, non-superseded record in } L_t \}.
$$

### 3.3 Generative continuity

Let $y_{1:t}$ be the generated continuation and $C_t$ a structured continuity state (entities, constraints, open goals, discourse commitments). A **continuity score** measures agreement between generation and continuity state:

$$
\mathrm{Cont}(y_{1:t}, C_t) \in [0,1].
$$

Operationalizations (**proposal** for unified metric; components exist in prior work) include: entity consistency checks, temporal validity of facts (FactTrack-style), contradiction detection against episode summaries (SCORE-style), and plan-progress consistency (Magentic-One-style task ledgers).

A **generative continuity expert** $E^{\mathrm{cont}}$ is a module (agent or MoE expert) whose training or prompting objective emphasizes maximizing $\mathrm{Cont}$ under sparse activation, rather than maximizing unconstrained next-token likelihood alone.

### 3.4 Index alignment (core definition)

**Definition 1 (Index Alignment).** A system state $(R_t, L_t, y_{1:t}, C_t)$ is *index-aligned* at step $t$ if:

1. **Routing–capability consistency.** Every $\iota \in R_t$ refers to a live, permitted module under a capability policy $\Pi$ (no dangling or unauthorized indices).
2. **Routing–ledger consistency.** If $R_t$ triggers a state-changing action, the resulting ledger proposal is consistent with $\mathrm{View}(L_t)$ under transition rules $\delta$ (no silent overwrite of accepted facts without `SUPERSEDE` provenance).
3. **Generation–index consistency.** Claims in $y_{t}$ that depend on retrieved documents, tools, or memory cite indices that were actually activated in $R_{\le t}$ (no hallucinated citations to inactive indices).
4. **Continuity–ledger consistency.** $C_t$ is a sound projection of $\mathrm{View}(L_t)$ plus open discourse structure; generative continuity experts may update $C_t$ but may not unilaterally mutate $L_t$.

**Definition 2 (Alignment deficit).** 

$$
\Delta_t = \lambda_1 d_{\mathrm{route}}(R_t,\Pi) + \lambda_2 d_{\mathrm{led}}(R_t,L_t) + \lambda_3 d_{\mathrm{gen}}(y_t,R_{\le t}) + \lambda_4 (1-\mathrm{Cont}(y_{1:t},C_t)),
$$

with task-specific distances $d_{(\cdot)}$. Index alignment optimization seeks policies that keep $\mathbb{E}[\sum_t \Delta_t]$ small without destroying task reward.

### 3.5 Capability isolation

**Definition 3 (Capability isolation).** Roles are capability-isolated if the following write permissions hold:

| Role | May propose $R_t$ | May append to $L$ | May emit $y$ tokens | Owns factual authority |
|------|-------------------|-------------------|---------------------|------------------------|
| Non-authoritative router | Yes | No (proposal only) | No / limited | No |
| State ledger (service) | No | Yes (under $\delta$) | No | Yes (for committed facts) |
| Generative continuity expert | Optional advisory | No (proposal only) | Yes (continuity-focused) | No |
| Domain / tool experts | Via router | Proposal only | Yes | No (unless ledger-accepted) |

Isolation is a **design principle** inspired by (a) router/backbone decoupling in Read-ME, (b) Orchestrator-vs-worker separation in Magentic-One, and (c) transactional memory updates in TARL. It is **proposal** as a hard architectural invariant for index-aligned systems.

### 3.6 Sparse Mixture-of-Agents

**Definition 4 (Sparse Mixture-of-Agents, MoA).** Let $\mathcal{A}=\{A_1,\ldots,A_M\}$ be agents. A sparse MoA activates at most $K \ll M$ agents per orchestration step:

$$
R_t^{\mathrm{agent}} = \mathrm{TopK}( \rho(q_t, L_t, C_t) ),
$$

where $\rho$ is a non-authoritative routing function over agent indices, conditioned on the current query/subgoal $q_t$, ledger view, and continuity state. Agent outputs are aggregated by an orchestrator policy $\alpha$:

$$
z_t = \alpha\big( \{ A_i(\cdot) : i \in R_t^{\mathrm{agent}} \}, L_t, C_t \big).
$$

This parallels token-level MoE but operates at the *agent* granularity. Dense multi-agent chat (all agents speak every turn) is the $K=M$ special case; sparse MoA is the conditional-computation analogue.

---


## 4. Architecture and Role Taxonomy

### 4.1 System overview (**proposal**)

We describe a reference architecture for index-aligned LLM systems. Components communicate by typed index messages; durable truth flows only through the ledger.

```
                    +----------------------+
   query / tokens ->| Non-authoritative    |-- R_t (sparse indices) -->
                    | Router(s)            |
                    +----------+-----------+
                               |
                               v
              +----------------+----------------+
              |     Activation Fabric           |
              |  MoE experts | Agents | Tools   |
              |  Retrievers  | Continuity exps  |
              +----------------+----------------+
                               |
            proposals (facts, tool results, drafts)
                               |
                               v
                    +----------------------+
                    | State Ledger Service |-- View(L_t) -->
                    | (accept/pend/reject) |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Generative Continuity|
                    | Expert(s) + Decoder  |--> y_t
                    +----------------------+
```

### 4.2 Role: Non-authoritative routers

**Responsibility.** Map context features to sparse index sets $R_t$ over experts, agents, tools, or retrievers.

**What they are not.** They are not sources of ground truth. A router that both selects modules *and* silently mutates long-term memory concentrates failure modes (routing collapse plus memory pollution).

**Instances in literature.**

- MoE gating networks (Shazeer et al., 2017; Fedus et al., 2022; Jiang et al., 2024).
- Pre-gating / decoupled routers (Read-ME; arXiv:2410.19123).
- Retriever routers / learning-to-rank retrievers (LTRR; arXiv:2506.13743).
- Orchestrators that select the next agent (AutoGen group chat; Magentic-One Orchestrator).
- Tool-selection heads (Toolformer; HuggingGPT controller).

**Design rules (**proposal**).**

1. Routers emit indices and optional confidence; they do not commit ledger writes.
2. Routers may read $\mathrm{View}(L_t)$ and $C_t$ (read-only).
3. Load balancing / diversity regularizers apply at all sparse levels (token experts *and* agents) to avoid index collapse.
4. Adaptive $K$ (Ada-K style) is encouraged when subtask difficulty varies.

### 4.3 Role: State ledgers

**Responsibility.** Provide the authoritative, provenance-bearing record of accepted, pending, and rejected commitments; support supersession with history preservation.

**Instances in literature.**

- Magentic-One's structured progress/task ledgers (Fourney et al., 2024).
- TARL accepted/pending/rejected ledgers (arXiv:2608.03699).
- StateLedger path-addressed memory (NeurIPS 2026 abstract).
- Governed shared memory policies for multi-agent fleets (arXiv:2606.24535).
- MemGPT archival/recall stores as addressable external memory (Packer et al., 2023).

**Design rules (**proposal**).**

1. Every write carries provenance $\pi$ (agent ID, tool ID, document ID, confidence).
2. Conflicts create `PEND` or `REJECT` entries rather than silent clobbering.
3. Readers see a consistency-specified snapshot (e.g., committed-only vs. committed+pending).
4. Indices into the ledger are stable paths (content-addressed or hierarchical), enabling alignment checks.

### 4.4 Role: Generative continuity experts

**Responsibility.** Maintain coherence of entities, plans, constraints, and discourse across long generations; propose repairs when $\mathrm{Cont}$ drops; emit continuations conditioned on $\mathrm{View}(L_t)$ and $C_t$.

**Instances / precursors.**

- Continuity/repair modules in long-form narrative systems (SCORE, FactTrack, DOME).
- Reflection and summarization loops in Generative Agents (Park et al., 2023).
- Orchestrator re-planning on error in Magentic-One.
- Segment-ordering / coherence-oriented pointer objectives (arXiv:2406.04156).

**Design rules (**proposal**).**

1. Continuity experts are *specialists* in the sparse MoA/MoE bank, not the sole generators.
2. They may propose ledger updates (e.g., "entity status changed") but commits go through ledger rules.
3. They should be activated when continuity risk is high (long context, multi-session tasks, multi-agent handoffs)—an Ada-K-like policy over continuity indices.

### 4.5 Supporting roles

**Domain experts / workers.** Code, browse, retrieve, translate—activated by routers; return results as proposals.

**Critics / validators.** Optional agents that score alignment deficits $\Delta_t$ before commit (related to MetaGPT-style verification SOPs).

**Human-in-the-loop.** May act as a privileged provenance source for ledger accepts under policy $\Pi$.

### 4.6 Capability isolation as safety and debuggability

Isolation improves:

- **Debuggability.** One can audit whether a failure was a bad index (router), a bad commit (ledger policy), or a bad continuation (generator/continuity).
- **Security.** Unauthorized agents cannot rewrite shared memory (governed shared memory failure mode: unauthorized leakage / provenance collapse).
- **Composability.** New experts/agents register indices without gaining ledger authority by default.

---


## 5. Method / Formalization

This section specifies a concrete **Index-Aligned Sparse Mixture-of-Agents (IA-MoA)** method sketch. Unless noted, components are **proposal** compositions of mechanisms already validated separately in cited work.

### 5.1 Typed index space

Each activatable resource registers a descriptor:

$$
\mathrm{Reg}(\iota) = (\mathrm{type}(\iota),\; \mathrm{cap}(\iota),\; \mathrm{schema}(\iota),\; \mathrm{sla}(\iota)),
$$

where $\mathrm{cap}$ lists permitted actions, $\mathrm{schema}$ describes I/O types, and $\mathrm{sla}$ captures latency/cost priors for routing. Registration is analogous to tool/API cards in Toolformer/HuggingGPT and to expert metadata in MoE serving stacks.

### 5.2 Non-authoritative routing objective

Let $q_t$ be the current subgoal embedding (from orchestrator state). Define a scoring network

$$
s(\iota; q_t, L_t, C_t) = f_\theta\big( q_t,\; e_\iota,\; \phi(\mathrm{View}(L_t)),\; \psi(C_t) \big),
$$

with $e_\iota$ a learned or frozen embedding of the registered resource. Sparse activation:

$$
R_t = \mathrm{TopKSoftmax}(s(\cdot)), \quad |R_t| \le K.
$$

**Training signal (**proposal**, combining known losses).**

$$
\mathcal{L}_{\mathrm{route}} = \mathcal{L}_{\mathrm{task}} + \beta_{\mathrm{lb}} \mathcal{L}_{\mathrm{load}} + \beta_{\mathrm{al}} \mathcal{L}_{\mathrm{align}} + \beta_{\mathrm{cost}} \mathcal{L}_{\mathrm{cost}}.
$$

- $\mathcal{L}_{\mathrm{task}}$: downstream task loss or RL reward (as in Ada-K's PPO-trained allocators; arXiv:2410.10456).
- $\mathcal{L}_{\mathrm{load}}$: MoE-style load balancing to prevent expert/agent collapse (Shazeer et al., 2017; Fedus et al., 2022).
- $\mathcal{L}_{\mathrm{align}}$: penalty for generation–index inconsistency (Section 3.4), e.g., citing inactive document IDs.
- $\mathcal{L}_{\mathrm{cost}}$: expected latency/tool cost.

**Non-authoritativeness constraint.** The routing module's parameters $\theta$ have *no write head* into $L$. Any memory side effect must be an explicit proposal message consumed by the ledger service.

### 5.3 Ledger transition system

Let proposals arrive as

$$
\tilde{\ell} = (\hat{a}, \iota^{\mathrm{subj}}, \hat{v}, \pi, \mathrm{conf}).
$$

A deterministic (or policy-gated) transition $\delta$ implements:

$$
L_{t+1} = \delta(L_t, \tilde{\ell}).
$$

Following TARL's spirit of multi-way updates rather than binary write/hold, we adopt action set

$$
\hat{a} \in \{\mathtt{ADD}, \mathtt{IGNORE}, \mathtt{REVISE}, \mathtt{REJECT}, \mathtt{DEFER}\}.
$$

**Consistency invariants (**proposal**).**

1. *Provenance:* $\pi \neq \varnothing$ for all accepted writes.
2. *No silent mutate:* `REVISE` creates a supersession link; old values remain queryable.
3. *Reader isolation:* agents read snapshots; concurrent proposals serialize under a logical clock.
4. *Scope:* capability policy $\Pi$ restricts which $\iota^{\mathrm{subj}}$ a given proposer may touch (governed shared memory).

### 5.4 Continuity expert activation

Define a risk estimator

$$
r_t = 1 - \widehat{\mathrm{Cont}}(y_{1:t}, C_t; L_t).
$$

Activate continuity experts when $r_t > \tau$ or on handoff events (agent switch, session resume, tool failure):

$$
R_t \leftarrow R_t \cup \mathrm{TopK}_{\mathrm{cont}}(s_{\mathrm{cont}}(\cdot)).
$$

Continuity experts produce: (i) a patched draft $y'$, (ii) optional ledger proposals (e.g., entity status), (iii) an updated $C_{t+1}$.

### 5.5 Aggregation and decoding

Given activated modules' outputs $\{z_{\iota}\}_{\iota \in R_t}$, the aggregator $\alpha$ may:

- **Gate-weighted merge** (MoE style): $z = \sum_{(\iota,g)\in R_t} g\, z_\iota$ when outputs share a vector space;
- **Structured fusion** (agent style): synthesize a natural-language or JSON plan from worker reports, as in Magentic-One / MetaGPT;
- **RAG fusion:** concatenate or compress retrieved passages under an index list that is *echoed* into the prompt to support generation–index consistency.

Decoding then conditions on $(z, \mathrm{View}(L_t), C_t)$. We encourage **index echoing**: the prompt includes the explicit list of activated indices so that citation faithfulness is checkable (related to attribution practices in RAG).

### 5.6 End-to-end algorithm (IA-MoA)

```
Input: user task u, registries Reg, empty ledger L, empty continuity C
Initialize orchestrator subgoal q <- u
for t = 1,2,... until halt:
    R <- NonAuthRouter(q, View(L), C; K)
    if ContinuityRisk(C, y) > tau:
        R <- R union ContinuityExperts(K_c)
    execute modules in R -> proposals P, drafts Y
    for ell_tilde in P:
        L <- delta(L, ell_tilde)   # ledger authority
    C <- UpdateContinuity(C, View(L), Y)
    y_t <- Decode(Y, View(L), C) with index echoing
    q <- OrchestratorReplan(q, View(L), C, y_t)
    if Done(View(L), q): halt
Return y, L, C
```

### 5.7 Special cases that recover prior systems

| Setting | IA-MoA reduction |
|---------|------------------|
| Token-level MoE LLM | $\mathcal{I}=\mathcal{I}_{\mathrm{expert}}$, no agents; ledger optional; $K$ as in Switch/Mixtral |
| Single-agent ReAct | $M=1$ worker + tools as indices; ledger = scratchpad/memory |
| Magentic-One-like | Orchestrator router + worker agents + explicit ledgers |
| RAG-only | Router ranks retrievers/docs; generation–index consistency = citation faithfulness |
| Dense multi-agent chat | $K=M$ (no sparsity); alignment still applies to memory indices |

### 5.8 Theoretical sketch: why isolation helps

**Proposition 1 (Informal).** Suppose ledger writes from a coupled router-generator are corrupted with probability $p$ per step and reused with probability $q$ in future retrievals. Expected pollution grows as $\Theta(tpq)$ under naive overwrite. Under capability-isolated ledgers with reject/defer channels and provenance, accepted pollution requires joint failure of proposer *and* transition policy, reducing the leading term when policy true-negative rate is high.

This is a qualitative argument aligned with TARL's motivation (memory pollution, cumulative corruption) rather than a completed theorem; formal PAC-style bounds are left to future work (**proposal**).

**Proposition 2 (Informal).** If generation is constrained to cite only indices in $\bigcup_{s\le t} R_s$, then hallucination of external attributions is limited to misnaming within the activated set (a smaller set than the full corpus/registry). This parallels pointer-network constraints that force outputs to select from inputs (Vinyals et al., 2015).

---


## 5.5 Extended Formalization: Alignment Operators and Hierarchical Indices

### 5A.1 Typed morphisms between index spaces

Real systems often require *re-indexing*: a document ID becomes a memory path; a tool result becomes a ledger subject; an agent ID becomes a provenance stamp. We model these as typed morphisms

$$
\mu: \mathcal{I}_a \rightarrow \mathcal{I}_b \cup \{\bot\},
$$

where $\bot$ denotes a failed cast (e.g., citing a tool ID as if it were a document). **Index alignment** requires that every use of an index in generation or ledger writes be the image of a successful morphism from an activated source index.

**Definition 5 (Index lineage).** For a generated citation $c$ appearing in $y_t$, lineage $\mathrm{Lin}(c)$ is a path

$$
\iota_0 \xrightarrow{\mu_1} \iota_1 \xrightarrow{\mu_2} \cdots \xrightarrow{\mu_n} \iota_n = c
$$

with $\iota_0 \in \bigcup_{s\le t} R_s$. If no such path exists, $c$ is an **unaligned citation**.

This generalizes pointer-network discipline (outputs must point into inputs) to multi-store agent systems.

### 5A.2 Hierarchical sparsity

Let levels $\ell \in \{\mathrm{agent}, \mathrm{tool}, \mathrm{expert}, \mathrm{doc}\}$ each have budget $K_\ell$. Hierarchical activation:

$$
R_t^{(\ell)} = \mathrm{TopK}_{K_\ell}\big(s^{(\ell)}(\cdot \mid R_t^{(\mathrm{parent})}, L_t, C_t)\big).
$$

**Capability isolation** lifts recursively: a child router inside an agent still cannot commit to the global ledger except via proposals. This prevents "local MoE gates" from becoming hidden authoritative writers—an under-discussed risk when wrapping MoE models as agents.

### 5A.3 Alignment deficit as instantaneous Lagrangian

Rewrite $\Delta_t$ as a constrained objective. Maximize expected task return $J$ subject to alignment constraints:

$$
\max_\pi \; J(\pi) \quad \mathrm{s.t.}\quad \mathbb{E}_\pi[d_{\mathrm{gen}}] \le \epsilon_g,\;
\mathbb{E}_\pi[d_{\mathrm{led}}] \le \epsilon_L,\;
\mathbb{E}_\pi[1-\mathrm{Cont}] \le \epsilon_c.
$$

Lagrangian relaxation recovers Section 3.4's weighted sum. In practice, $\epsilon$ thresholds can be enforced by reject sampling or by activating continuity experts when constraints are near violation—mirroring Ada-K's difficulty-dependent allocation.

### 5A.4 Information-theoretic view of routing collapse

Let $I(X; R)$ be mutual information between inputs and routing decisions. Load-balancing losses implicitly encourage high entropy $H(R)$ while preserving task-useful $I(X;R)$. Collapse ($H(R)\to 0$) yields a dense model with wasted capacity. At agent level, collapse means the same worker is always called—sparse MoA degenerates to single-agent. Index alignment monitoring should therefore track $H(R_t)$ online as a health metric, not only offline MoE diagnostics.

### 5A.5 Continuity state as a projection

We require a projection operator

$$
\pi_{C\leftarrow L}: \mathrm{View}(L) \rightarrow C_{\mathrm{facts}},
$$

with discourse structure $C_{\mathrm{disc}}$ maintained separately. Full continuity state $C = (C_{\mathrm{facts}}, C_{\mathrm{disc}}, C_{\mathrm{goals}})$. Alignment demands $C_{\mathrm{facts}} \approx \pi_{C\leftarrow L}(\mathrm{View}(L))$; divergence indicates drift. Continuity experts primarily repair $C_{\mathrm{disc}}$ and $C_{\mathrm{goals}}$ and propose ledger updates when world facts change.

---


## 5.6 Design Patterns and Anti-Patterns

### 5B.1 Patterns (**proposal** catalog)

**Pattern P1: Propose–Validate–Commit.** Workers propose; critics validate; ledger commits. Echoes MetaGPT SOPs and TARL multi-action updates.

**Pattern P2: Index Echoing.** Always surface activated IDs in the generator prompt; parse outputs for ID mentions; score $d_{\mathrm{gen}}$.

**Pattern P3: Dual Ledgers.** Separate *task progress* ledger (Magentic-One style) from *world fact* ledger (TARL style) to avoid conflating plan state with environment state.

**Pattern P4: Continuity on Handoff.** Force continuity expert activation on every agent switch and session resume.

**Pattern P5: Router Read-Only Mounts.** Routers mount $\mathrm{View}(L)$ as read-only filesystem/API; write attempts throw.

**Pattern P6: Soft then Hard.** Train with $\mathcal{L}_{\mathrm{align}}$ soft penalties; at inference, optionally harden with constrained decoding over allowed citation IDs.

### 5B.2 Anti-patterns

**Anti-pattern A1: Omnibus Orchestrator.** One agent routes, writes memory, and generates user-facing text without isolation—debuggability collapses.

**Anti-pattern A2: Scratchpad Clobber.** `memory = new_summary` without supersession links destroys audit trails.

**Anti-pattern A3: Dense Always-On Teams.** All agents verbally "debate" every turn; cost explodes; provenance dilutes.

**Anti-pattern A4: Silent Tool Indices.** Tool outputs enter context without stable IDs—generation cannot cite them alignedly.

**Anti-pattern A5: Continuity by Context Stuffing Alone.** Dumping full history without structured $C_t$ or ledger projection fails at long horizons (motivation for MemGPT paging and StateLedger paths).

### 5B.3 Migration path for existing stacks

1. **Instrument** existing routers/orchestrators to emit structured $R_t$ logs.
2. **Wrap** scratchpads with append-only APIs implementing $\delta$.
3. **Add** a continuity specialist agent behind a risk gate.
4. **Enforce** citation checks in CI for agent traces.
5. **Tune** $K$ and adaptive policies under a fixed budget.

This path does not require training a new foundation model; it is primarily systems + evaluation work—consistent with Magentic-One's modular agent addition claim.

---


## 6. Experiments and Evaluation Design

**Status:** This section specifies protocols for future empirical work. It does **not** report new benchmark numbers. Where we mention published scores, they are from cited papers.

### 6.1 Research questions

- **RQ1 (Routing fidelity):** Does non-authoritative sparse routing match oracle expert/agent indices on controlled tasks?
- **RQ2 (Ledger consistency):** Do transactional ledgers reduce memory pollution vs. overwrite baselines under conflicting evidence?
- **RQ3 (Continuity retention):** Do generative continuity experts improve long-horizon coherence metrics without harming short-task accuracy?
- **RQ4 (Sparse MoA efficiency):** For fixed compute budget, does sparse agent activation ($K \ll M$) retain task success relative to dense activation?
- **RQ5 (End-to-end alignment):** Does optimizing $\Delta_t$ improve attribution faithfulness and reduce unauthorized memory writes?

### 6.2 Datasets and benchmarks (recommended)

**MoE / routing.** Language modeling perplexity and downstream suites used in Mixtral / Switch / Ada-K evaluations; expert-choice probes on synthetic cluster data as in Dikkala et al. (2023).

**RAG / index faithfulness.** Multi-hop QA (e.g., HotpotQA-style), attribution benchmarks, and GraphAnchor's multi-hop settings (arXiv:2601.16462). Measure whether answer spans are supported by retrieved IDs.

**Agent orchestration.** GAIA, AssistantBench, WebArena as used by Magentic-One (Fourney et al., 2024); OfficeBench-style workflow tasks as in LEGOMem (arXiv:2510.04851).

**Memory / ledger.** LongMemEval, LoCoMo, Evo-Memory (as cited by StateLedger); TARL-Mem for fine-grained update actions (arXiv:2608.03699).

**Continuity.** Long-form story/plan benchmarks with contradiction annotations (FactTrack, SCORE, DOME settings).

### 6.3 Metrics

1. **Top-$K$ routing agreement** with oracle or with held-out learned routers.
2. **Load balance** entropy / Switch-style auxiliary loss value.
3. **Ledger metrics:** action accuracy (TARL), pollution rate, conflict preservation rate, provenance completeness.
4. **Faithfulness / attribution:** fraction of factual claims entailed by activated indices' contents.
5. **Continuity:** entity consistency, temporal validity F1, contradiction rate, human coherence ratings.
6. **Efficiency:** activated parameters / agents per step, wall-clock latency, \$ cost of tool calls.
7. **Task success:** benchmark-primary metrics (Exact Match, success rate, pass@k).

### 6.4 Baselines

- Dense activation ($K=M$ or full FFN).
- Static top-$K$ MoE routing without ledger.
- Single-agent ReAct without shared ledger.
- Orchestrator + workers with scratchpad overwrite memory (no transactional ledger).
- RAG without index echoing / citation constraints.
- Continuity-agnostic decoding (no continuity experts).

### 6.5 Ablations

- Remove capability isolation (router writes memory directly).
- Remove continuity experts.
- Replace learned router with round-robin / random indices.
- Vary $K$ and adaptive-$K$ policies.
- Ledger with vs. without provenance.
- Soft vs. hard generation–index constraints.

### 6.6 Implementation notes (**proposal**)

A minimal research prototype can compose: (i) an open MoE or dense LLM backbone; (ii) AutoGen- or Magentic-One-style agent runtime; (iii) a path-addressed store implementing $\delta$; (iv) logging of all $R_t$ for offline $\Delta_t$ analysis. Router decoupling (Read-ME) helps batching and reproducible index traces.

### 6.7 Expected empirical patterns (hypotheses, not results)

H1: Isolation reduces irreversible memory pollution under conflicting tool outputs.  
H2: Index echoing improves attribution faithfulness with minor fluency cost.  
H3: Sparse MoA with $K\in\{1,2,3\}$ recovers most of dense MoA success on modular workflows while cutting agent calls.  
H4: Continuity experts help most when average session length or handoff count is high.  
H5: Adaptive $K$ tracks difficulty similarly to Ada-K's finding that harder tokens/tasks activate more experts.

---


## 6.5 Theoretical Analysis Sketch

### 6A.1 Finite-horizon pollution bound (informal)

Assume each step produces a conflicting proposal with probability $p$, and an overwrite-memory baseline accepts conflicts into the single slot used by future retrieval with probability 1. Then expected corrupted retrievals over horizon $T$ scale as $O(pT)$.

Under a ledger with reject channel of true-negative rate $\mathrm{TNR}$ on corrupt proposals, expected accepted corruptions scale as $O(p(1-\mathrm{TNR})T)$. If retrieval prefers freshest accepted facts, pollution in $\mathrm{View}$ is similarly reduced. **Caveat:** false rejects harm recall; TARL-Mem-style benchmarks are needed to measure the tradeoff.

### 6A.2 Sample complexity intuition for routers

Dikkala et al. (2023) show learned routers exploit cluster structure. In IA-MoA, ledger features $\phi(\mathrm{View}(L))$ act as additional clustering signals (e.g., "budget already known" → skip retrieval agent). We conjecture sample complexity for routing improves when ledger features are low-dimensional sufficient statistics—another reason to keep ledgers structured rather than purely neural keys.

### 6A.3 Continuity as contractiveness

View continuity repair as operator $T$ on discourse states. Desirable: $T$ is contractive w.r.t. a contradiction metric $d_\neg$, i.e., $d_\neg(T(C), C^\star) \le \gamma d_\neg(C, C^\star)$ with $\gamma<1$ toward a consistent $C^\star$ compatible with $\mathrm{View}(L)$. Designing losses that encourage contractiveness is an open problem; narrative repair systems provide empirical existence proofs without the formal operator view.

### 6A.4 When sparsity hurts

Sparsity fails when tasks need many simultaneous capabilities (e.g., tightly coupled multimodal editing). Adaptive $K$ and fallback to denser activation under high $\Delta_t$ are pragmatic mitigations (compare Ada-K allocating more experts to harder tokens). Index alignment does not mandate extreme sparsity; it mandates that whatever is activated be consistent with ledgers and generation.

---


## 6.6 Threats to Validity for Future Experiments

- **Benchmark leakage** for agent tasks if tools access live web.
- **Confound between model strength and orchestration** when comparing sparse MoA to single strong agents.
- **Ledger policy overfitting** to synthetic conflict distributions unlike real users.
- **Annotator disagreement** on continuity labels.
- **Hardware variability** masking FLOP savings from sparse experts.
- **Prompt brittleness** for non-finetuned continuity agents.

Pre-registration of metrics (Section 6.3) and open trace logs of $R_t$ would mitigate several threats.

---


## 7. Discussion

### 7.1 Index alignment as a unifying correctness lens

Across MoE, RAG, tools, and agents, systems already emit discrete choices. What differs is whether those choices are treated as *first-class state*. Serving stacks log expert IDs for load balancing; RAG pipelines log passage IDs for debugging; agent frameworks log tool calls for traces. Index alignment elevates these logs from telemetry to a correctness interface: the tuple $(R_t, L_t, y_t)$ must cohere.

This lens explains certain failure taxonomies more cleanly than "hallucination" alone:

| Observed failure | Index-alignment reading |
|------------------|-------------------------|
| Fluent but wrong expert behavior on a token | Misrouted $\mathcal{I}_{\mathrm{expert}}$ |
| Answer cites a paper not in context | Generation–index inconsistency |
| Agent team loops on obsolete plan | Ledger not updated / continuity drift |
| Two agents disagree forever | Missing conflict channel in ledger (`PEND`/`REJECT`) |
| Tool called with leaked credentials path | Capability policy $\Pi$ failure on tool indices |
| Session resume invents prior commitments | Continuity state not projected from ledger |

### 7.2 Why routers should be non-authoritative

Classical MoE routers are already non-authoritative w.r.t. parameters: they select among experts but do not rewrite expert weights online during inference. Problems arise when the *same* control channel is reused for durable world state—common in agent scaffolds where the orchestrator both picks the next worker *and* edits a shared scratchpad without transactional semantics.

Non-authoritativeness buys:

1. **Separation of concerns** for optimization (router can be PPO-trained for allocation as in Ada-K without being the memory model of record).
2. **Auditability** (proposals vs. commits).
3. **Safer multi-tenant agents** (governed shared memory).

The cost is latency and complexity: an extra commit path. For short single-agent chats the cost may not pay off; for persistent multi-agent systems the literature increasingly suggests it does (TARL, StateLedger, governed memory).

### 7.3 Sparse Mixture-of-Agents vs. Mixture-of-Experts

MoE sparsifies *parameters*; sparse MoA sparsifies *social computation* among agents. They compose: each agent may itself be an MoE model. Index alignment then becomes hierarchical—token-level expert indices inside agent-level indices inside ledger paths. Hierarchical indices are powerful but increase alignment surface area; capability isolation should be enforced at each level.

Dense multi-agent debate can improve quality on some tasks but scales poorly and complicates provenance. Sparse MoA is the conditional-computation bet: most subtasks need few specialists. Magentic-One's design (one Orchestrator directing few workers per step) is empirically in this spirit even when not branded as MoE.

### 7.4 Continuity experts are not "the writer"

A risk in role taxonomies is collapsing generation into a single omnipotent agent. We intentionally separate *generative continuity experts* from domain workers. Continuity specialists score and repair coherence; domain workers supply content, code, or retrieval. The decoder may be shared silicon, but the *routing index* distinguishes objectives—analogous to specialized MoE experts emerging by syntax/semantics (Shazeer et al., 2017, appendix).

### 7.4.1 Relations to pointer networks and constrained decoding

Pointer Networks force outputs to be indices into inputs (Vinyals et al., 2015). Generation–index consistency is a soft, large-vocabulary analogue: the model may generate free text, but attributions must point into $R_{\le t}$. Hard constraints (constrained decoding / automata over allowed citation IDs) are a possible implementation; soft penalties in $\mathcal{L}_{\mathrm{align}}$ are another. Both are compatible with IA-MoA.

### 7.4.2 Systems considerations

Read-ME's router decoupling enables pre-gating and expert-aware batching—system-level index alignment. Path-addressed ledgers enable caching and coalescing (StateLedger claims). Sparse activation without index-aware serving leaves performance on the table: if the system cannot schedule around $R_t$, theoretical FLOP savings will not appear as wall-clock savings.

### 7.4.3 Sociotechnical note

Ledgers with provenance support accountability (who asserted what, based on which tool output). Capability isolation reduces unauthorized leakage across agent teams. These are technical controls, not complete governance; policy $\Pi$ must still be specified by operators.

### 7.4.4 What would falsify the proposal?

The IA-MoA framing would be weakened if:

- End-to-end models with coupled router-memory consistently beat isolated ledgers on pollution *and* task success after matched tuning;
- Index echoing reliably harms usefulness without measurable faithfulness gains;
- Continuity specialists never outperform simply retrieving more raw history into a single generalist agent.

We consider these open empirical questions (Section 6).

---


## 7.5 Pedagogical Comparison Tables

### Table: Conditional computation across layers

| Layer | Unit activated | Index type | Typical $K$ | Authoritative store? |
|-------|----------------|------------|-------------|----------------------|
| Dense Transformer | All parameters | n/a | all | Weights (training) |
| MoE FFN | Experts | expert ID | 1–2 | No (router non-auth) |
| RAG | Passages / graph nodes | doc/node ID | 5–20 | Corpus immutable; session store optional |
| Tools | APIs | tool ID | 0–3 | External systems |
| Multi-agent | Agents | agent ID | 1–3 sparse | Should be ledger |
| IA-MoA (**proposal**) | Agents+tools+cont. | typed $\iota$ | adaptive | State ledger |

### Table: Failure → metric mapping

| Failure | Primary metric | Secondary metric |
|---------|----------------|------------------|
| Expert collapse | $H(R)$, load loss | Task accuracy |
| Bad agent pick | Routing agreement vs oracle | End-to-end success |
| Hallucinated citation | $d_{\mathrm{gen}}$ | Human faithfulness |
| Memory pollution | Pollution rate | Downstream regret |
| Continuity break | Contradiction rate | User-rated coherence |
| Unauthorized write | Policy violation count | Leakage probes |

### Table: What each role optimizes

| Role | Primary objective | Must not optimize alone |
|------|-------------------|-------------------------|
| Non-authoritative router | Task-aware allocation under budget $K$ | Durable world truth |
| State ledger | Consistent commits with provenance | Fluency / style |
| Generative continuity expert | $\mathrm{Cont}\uparrow$, repair | Unilateral fact invention |
| Domain worker | Local subtask quality | Global memory policy |

---


## 7.6 Implications for Evaluation Culture

Agent papers often report end-to-end success without releasing routing traces. MoE papers report perplexity without public expert-assignment entropy curves. RAG papers report EM without citation-ID alignment rates. **Index alignment suggests a norm:** publish $R_t$ traces (or aggregate statistics) alongside primary metrics. Magentic-One's emphasis on rigorous agentic evaluation harnesses (AutoGenBench) is complementary: isolation and repetition controls matter precisely because agent indices have side effects.

We also recommend **negative results** reporting: when increasing $K$ does not help; when continuity experts reduce contradiction but hurt latency; when hard citation constraints starve creative tasks. The proposal is falsifiable (Section 7.8); evaluation culture must allow falsification.

---


## 7.7 Broader Outlook

If conditional computation continues to dominate frontier training (sparse experts) and product architectures (agents + tools + RAG), then correctness work will shift from "make the next token better" to "make the next *index* better—and keep it consistent with what we already committed." Preference alignment (RLHF/RLAIF) and index alignment are orthogonal axes: a model can be preference-aligned yet cite inactive documents, or index-aligned yet rude. Systems that care about reliability in the physical or financial world need both.

Finally, sparse Mixture-of-Agents offers a research bridge between the MoE community and the agent community. Shared mathematics (top-$K$, load balancing, gating) and shared systems problems (scheduling, caching, telemetry) suggest joint venues and benchmarks. Index alignment is one candidate lingua franca.

---


## 7.9 Open Problems

1. **Joint training of multi-level routers.** Can token-level MoE gates and agent-level routers be co-trained under a shared $\Delta_t$ without instability?
2. **Standard ledger interchange formats.** A portable schema for accepted/pending/rejected records would enable cross-framework evaluation.
3. **Certified generation–index consistency.** Can constrained decoding provide certificates that all citations lie in $R_{\le t}$?
4. **Economic indices.** Tool dollar-cost as a first-class routing feature under budget constraints.
5. **Adversarial index attacks.** Prompt injections that manipulate routers toward privileged tool indices; defenses via $\Pi$ and critics.
6. **Human-readable provenance.** Summarizing long ledgers without creating a second, unaligned memory.
7. **Cross-session continuity experts.** Specialists that only activate on resume and compress prior ledgers into $C_0$.


## 8. Limitations

1. **This draft reports no new large-scale experiments.** Evaluation designs are prospective.
2. **Formal bounds** on pollution and alignment deficit are informal sketches.
3. **Ledger semantics** vary across cited systems; our $\delta$ is a unifying template, not a proven consensus protocol under Byzantine agents.
4. **Continuity metrics** remain partly task-specific; a single universal $\mathrm{Cont}$ may not exist.
5. **Adaptive multi-level sparsity** (token + agent + tool) may interact poorly without joint training.
6. **Human factors:** provenance-rich ledgers can become verbose; compression may reintroduce alignment debt.
7. **Security:** index echoing does not stop models from fabricating *content* under a real index—only from citing inactive indices. Entailment checks remain necessary.
8. **Terminology collision:** "alignment" here means index consistency, not preference-model alignment (RLHF). We use "index alignment" explicitly to reduce confusion but cross-field polysemy remains.

---


## 9. Conclusion

Sparse activation is no longer a niche training trick: it structures modern LLMs (MoE), modern retrieval (RAG indices), modern tool use, and modern multi-agent orchestration. We argued that the discrete *indices* these systems emit deserve first-class correctness treatment. **Index alignment** names the requirement that routed activations, ledgered commitments, and generated continuations remain mutually consistent.

We proposed a role taxonomy with **non-authoritative routers**, **state ledgers**, and **generative continuity experts**, under **capability isolation**, and sketched **sparse Mixture-of-Agents** as the agent-level analogue of MoE. The framework is deliberately grounded in real literature—from sparsely gated MoE and Switch/Mixtral routing, through pointer networks and tool-using LMs, to AutoGen/Magentic-One orchestration and transactional/path-addressed memories—while labeling synthesizing claims as proposal.

Future work should implement IA-MoA prototypes, measure the metrics of Section 6, and tighten theory around alignment deficits. If successful, index alignment may become a practical design and auditing principle for reliable conditional computation in LLM systems.

---


## Acknowledgments

[Placeholder for funding, compute, and colleague acknowledgments.]

---


## References

1. Shazeer, N., Mirhoseini, A., Maziarz, K., Davis, A., Le, Q., Hinton, G., & Dean, J. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer. *ICLR*. arXiv:1701.06538. https://arxiv.org/abs/1701.06538

2. Lepikhin, D., Lee, H., Xu, Y., Chen, D., Firat, O., Huang, Y., Krikun, M., Shazeer, N., & Chen, Z. (2020). GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding. arXiv:2006.16668. https://arxiv.org/abs/2006.16668

3. Fedus, W., Zoph, B., & Shazeer, N. (2022). Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity. *JMLR*. arXiv:2101.03961. https://arxiv.org/abs/2101.03961

4. Jiang, A. Q., et al. (2024). Mixtral of Experts. arXiv:2401.04088. https://arxiv.org/abs/2401.04088

5. Cai, W., et al. (2024). A Survey on Mixture of Experts in Large Language Models. arXiv:2407.06204. https://arxiv.org/abs/2407.06204

6. Huang, et al. (2024). Ada-K Routing: Boosting the Efficiency of MoE-based LLMs. arXiv:2410.10456. https://arxiv.org/abs/2410.10456

7. Read-ME authors (2024). Read-ME: Refactorizing LLMs as Router-Decoupled Mixture of Experts with System Co-Design. arXiv:2410.19123. https://arxiv.org/abs/2410.19123

8. Dikkala, N., et al. (2023). On the Benefits of Learning to Route in Mixture-of-Experts Models. *EMNLP*. https://aclanthology.org/2023.emnlp-main.583/

9. Fedus, W., et al. (2022). A Review of Sparse Expert Models in Deep Learning. arXiv:2209.01667. https://arxiv.org/abs/2209.01667

10. Vinyals, O., Fortunato, M., & Jaitly, N. (2015). Pointer Networks. *NeurIPS*. arXiv:1506.03134. https://arxiv.org/abs/1506.03134

11. Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*. arXiv:2005.11401. https://arxiv.org/abs/2005.11401

12. LTRR authors (2025). LTRR: Learning To Rank Retrievers for LLMs. arXiv:2506.13743. https://arxiv.org/abs/2506.13743

13. GraphAnchor authors (2026). Graph-Anchored Knowledge Indexing for Retrieval-Augmented Generation. arXiv:2601.16462. https://arxiv.org/abs/2601.16462

14. PG-RAG authors (2024). Empowering Large Language Models to Set up a Knowledge Retrieval Indexer via Self-Learning. arXiv:2405.16933. https://arxiv.org/abs/2405.16933

15. Segment-ordering / pointer-guided SO (2024). Pointer-guided segment ordering pretraining. arXiv:2406.04156. https://arxiv.org/abs/2406.04156

16. Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv:2302.04761. https://arxiv.org/abs/2302.04761

17. Yao, S., et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*. arXiv:2210.03629. https://arxiv.org/abs/2210.03629

18. Shen, Y., et al. (2023). HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. arXiv:2303.17580. https://arxiv.org/abs/2303.17580

19. Wu, Q., et al. (2023). AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. arXiv:2308.08155. https://arxiv.org/abs/2308.08155

20. Hong, S., et al. (2023). MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework. arXiv:2308.00352. https://arxiv.org/abs/2308.00352

21. Fourney, A., et al. (2024). Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks. arXiv:2411.04468. https://arxiv.org/abs/2411.04468

22. LEGOMem authors (2025). LEGOMem: Modular Procedural Memory for Multi-agent LLM Systems for Workflow Automation. arXiv:2510.04851. https://arxiv.org/abs/2510.04851

23. Packer, C., et al. (2023). MemGPT: Towards LLMs as Operating Systems. arXiv:2310.08560. https://arxiv.org/abs/2310.08560

24. Park, J. S., et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. arXiv:2304.03442. https://arxiv.org/abs/2304.03442

25. Governed Shared Memory authors (2026). Governed Shared Memory for Multi-Agent LLM Systems. arXiv:2606.24535. https://arxiv.org/abs/2606.24535

26. TARL authors (2026). TARL: Transaction-Aware Reliable Ledgers for Executable Memory Management in Long-Term Agents. arXiv:2608.03699. https://arxiv.org/abs/2608.03699

27. MAGE authors (2026). Diachronic Hypergraphs for Orchestrated Multi-Agent Multimodal Memory Curation. arXiv:2608.29678. https://arxiv.org/abs/2608.29678

28. StateLedger authors (2026). StateLedger: Path-Addressed External Memory for Persistent Multi-Agent Systems. NeurIPS 2026 poster. https://neurips.cc/virtual/2026/poster/151469

29. Kaplan, J., et al. (2020). Scaling Laws for Neural Language Models. arXiv:2001.08361. https://arxiv.org/abs/2001.08361

30. Hoffmann, J., et al. (2022). Training Compute-Optimal Large Language Models. arXiv:2203.15556. https://arxiv.org/abs/2203.15556

31. Bengio, Y., Léonard, N., & Courville, A. (2013). Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation. arXiv:1308.3432. https://arxiv.org/abs/1308.3432

32. Vaswani, A., et al. (2017). Attention Is All You Need. *NeurIPS*. arXiv:1706.03762. https://arxiv.org/abs/1706.03762

33. DSMoE authors (2025). DSMoE: Matrix-Partitioned Experts with Dynamic Routing for Computation-Efficient Dense LLMs. arXiv:2502.12455. https://arxiv.org/abs/2502.12455

34. Finedeep authors (2025). Finedeep: Mitigating Sparse Activation in Dense LLMs via Multi-Layer Fine-Grained Experts. Related preprint 2025. https://arxiv.org/html/2502.12928

35. DOME / long-form outlining with memory (2024). Generating Long-form Story Using Dynamic Hierarchical Outlining with Memory-Enhancement. arXiv:2412.13575. https://arxiv.org/abs/2412.13575

36. SCORE authors (2025). SCORE: Story Coherence and Retrieval Enhancement for AI Narratives. arXiv:2503.23512. https://arxiv.org/abs/2503.23512

37. FactTrack (2025). FactTrack: Time-Aware World State Tracking in Story Outlines. *NAACL*. https://doi.org/10.18653/v1/2025.naacl-long.144

38. STORYWRITER / long-form multi-agent writing (2025). Related preprint arXiv:2506.16445. https://arxiv.org/pdf/2506.16445

39. Gao, Y., et al. (2024). Retrieval-Augmented Generation for Large Language Models: A Survey. arXiv:2312.10997. https://arxiv.org/abs/2312.10997

40. Comprehensive MoE survey (2025). A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications. arXiv:2503.07137. https://arxiv.org/abs/2503.07137

---


## Appendix A. Glossary

| Term | Meaning in this paper |
|------|------------------------|
| Index | Typed discrete pointer into experts, agents, memory paths, tools, or documents |
| Index alignment | Consistency among routed indices, ledger state, and generation |
| Non-authoritative router | Module that proposes sparse activations without committing world state |
| State ledger | Append-oriented authoritative store with provenance and validity |
| Generative continuity expert | Specialist optimizing long-horizon coherence under sparse activation |
| Capability isolation | Hard separation of write permissions across roles |
| Sparse MoA | Top-$K$ activation over agents analogous to MoE over experts |
| Alignment deficit $\Delta_t$ | Scalar penalty aggregating routing, ledger, generation, continuity errors |


## Appendix B. Notation summary

| Symbol | Meaning |
|--------|---------|
| $R_t$ | Sparse routing decision at step $t$ |
| $L_t$ | Ledger prefix at step $t$ |
| $\mathrm{View}(L_t)$ | Committed key-value view |
| $C_t$ | Continuity state |
| $\Pi$ | Capability / permission policy |
| $\delta$ | Ledger transition function |
| $\Delta_t$ | Alignment deficit |
| $K$ | Sparse activation budget |


## Appendix C. Example trace (illustrative, not empirical)

**Task:** "Update the project budget spreadsheet and email the team if total exceeds \$10k."

1. Router activates indices: `agent:file_surfer`, `tool:python_exec` ($K=2$).
2. File surfer proposes ledger entry: `mem:/project/budget.total = 12500` with provenance `file:Q3.xlsx`.
3. Ledger `ACCEPT`s after schema check.
4. Continuity risk high (constraint "email if >10k"): activate `agent:continuity` + `agent:emailer`.
5. Continuity expert checks $C_t$ open goal; emailer drafts message citing `mem:/project/budget.total`.
6. Generation–index check: email mentions only activated memory path and tools.
7. Orchestrator marks goal complete in task ledger.

Failure mode without isolation: a single orchestrator overwrites `budget.total` with a hallucinated number mid-trace; later agents reuse it—classic pollution.


## Appendix D. Mapping roles to literature artifacts

| Role | Closest deployed/published artifact |
|------|-------------------------------------|
| Non-authoritative router | MoE gate; Magentic-One Orchestrator next-agent choice; LTRR retriever ranker |
| State ledger | Magentic-One ledgers; TARL; StateLedger; MemGPT stores |
| Generative continuity expert | SCORE/FactTrack repair; orchestrator replan; reflection modules |
| Sparse MoA | Magentic-One step-wise worker activation; MoE analogy (**proposal** name) |

---

*End of draft. Document version: 2026-11-05 (America/Los_Angeles). Speculative sections marked Proposal throughout.*

## Appendix E. Checklist for Index-Aligned Systems

Use this checklist when reviewing an LLM agent/MoE deployment:

- [ ] All activatable resources have stable typed IDs in a registry.
- [ ] Routers emit machine-readable $R_t$ traces every step.
- [ ] Routers cannot write durable memory except via proposals.
- [ ] Ledger supports accept/pend/reject (or equivalent) with provenance.
- [ ] Supersessions preserve historical values.
- [ ] Generation prompts echo activated indices when citations matter.
- [ ] Automated check fails builds/traces with unaligned citations.
- [ ] Continuity specialist exists for handoffs and long sessions.
- [ ] Capability policy $\Pi$ denies unauthorized tool/memory indices.
- [ ] Load/entropy health metrics monitored for routers at each sparsity level.
- [ ] Evaluation reports task metrics *and* alignment metrics from Section 6.3.
- [ ] Side-effecting tools run in sandboxes with reversible ledgers where possible.

