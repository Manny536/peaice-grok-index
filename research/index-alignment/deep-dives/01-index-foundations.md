# 01 — Index Foundations: Typed Indices, Registries, Lineage, and Scale Trees

*Backs manuscript §§1.1, 2.1, 3.1–3.2, 3.6 and Appendix C.*

## 1.1 The problem the index abstraction solves

A sparse language-model system does not produce text from a single undifferentiated computation. At each step it makes discrete selections: a top-k gate chooses experts inside a layer (Shazeer et al., 2017; Fedus et al., 2022; Jiang et al., 2024); an orchestrator chooses an agent (Wu et al., 2023; Fourney et al., 2024); a retriever chooses passages (Lewis et al., 2020); a planner chooses a tool (Schick et al., 2023; Yao et al., 2023); a memory manager chooses a path (Packer et al., 2023). Each selection is an identifier drawn from a finite set. Coleman (2026a, §3.1) named these identifiers *indices* and observed that a large class of production failures is a mismatch between indices rather than a defect of fluency: the citation that names a document never retrieved, the tool call that uses a deregistered version, the summary that silently drops a committed fact.

The value of the abstraction is that indices are *observable*. Hidden activations are not certifiable objects; an expert ID in a router log, a document hash in a retrieval record, and a commit record in a ledger are. Any boolean claim has to be about something that can be enumerated and compared, and indices are the part of a sparse system that already has that shape. The manuscript's restriction to indices is therefore not a simplification of convenience; it is the condition under which a yes/no answer means anything.

## 1.2 Why every index must be typed and versioned

Definition 1 writes an index as `ι = (type, name, epoch, version)`. Each component removes a specific ambiguity that otherwise breaks a checker.

**Type.** Coleman (2026a) already used a disjoint union `𝓘_expert ∪ 𝓘_agent ∪ 𝓘_mem ∪ 𝓘_tool ∪ 𝓘_doc`. The continuation extends it with `claim`, `correction`, `source`, and `obligation`, because those are the objects corrections and continuity act on. Disjointness matters operationally: a string such as `search` can be a tool, an agent persona, and a memory namespace at once. A checker that compares untyped names can certify that "the cited `search` was active" when the active `search` was a tool and the cited one a document. Typing converts that silent category error into a failed cast (`⊥`) in Definition 3.

**Epoch.** A registry changes. Tools are deprecated, experts are retrained, policies are revised. The epoch names the registry state against which liveness and permission are evaluated. Without it, `Live(ι)` is ill-posed: live *when*? Trace E in the manuscript (stale tool authority) depends entirely on this field — the approval was genuine under `r7` and obsolete under `r8`.

**Version.** The version distinguishes contents or interface of the resource itself. A document revised from version 2 to 3 (Trace G) keeps its name; claims supported by version 2 may be unsupported by version 3. Version is the hook by which a correction finds its dependents.

The rule "an index name without a type is not a well-formed certificate field" is therefore a parsing rule with semantic consequences: it forces every downstream predicate to operate on unambiguous objects.

## 1.3 Registry entries and the separation of liveness from permission

A registry entry `Reg(ι) = (type, capabilities, input_schema, output_schema, authority_scope, validity_interval, digest)` supports two predicates the manuscript keeps apart:

- `Live_k(ι)`: the entry exists at scale `k`, its validity interval covers the relevant logical time, and its digest matches the observed artifact.
- `Permitted_k(ι, a)`: policy `Π_k` permits action `a` on that entry for the authenticated principal.

The distinction is the content of Trace B. A registered, live, in-budget expert can be activated for a task it is not permitted to perform. Registry membership answers "does this thing exist and is it the thing I think it is?"; policy answers "may this principal use it for this?". Conflating them is the most common authorization bug in tool-using agents, where a tool's presence in the tool list is treated as license to call it. The digest field closes a third gap — substitution — by binding the name to the artifact actually executed.

The policy is declared an *input* to the audit, "not something inferred from successful execution." This is a deliberate refusal of a tempting inference. A call that succeeded shows that the environment accepted it; it does not show that it was permitted. Many environments accept calls they should not.

## 1.4 Activation records and why gate weights are telemetry

Definition 2's activation record `r = (ι, parent, gate, input_digest, output_digest, principal, event_id)` records the fact of selection. The manuscript states that "a nonzero gate does not imply permission, authority, support, or correctness." The reason is mechanistic. In a softmax gate `p_i(x) = exp(h_i)/Σ_j exp(h_j)` followed by top-k (Coleman 2026a, §3.1, following Shazeer et al. 2017), the gate value measures the router's learned affinity between an input and an expert. It is trained for loss reduction, often with an auxiliary load-balancing term (Lepikhin et al., 2020; Fedus et al., 2022). Nothing in that objective encodes authorization or factual support. A high gate on a wrong expert and a low gate on the right one are both ordinary. Hence `A_route` never reads gate magnitude as quality; gates enter only as telemetry and, where a budget is declared, through `Budget(r)`.

## 1.5 Morphisms and lineage: the pointer discipline generalized

Pointer Networks (Vinyals et al., 2015) make a model's output an index into its input, which guarantees by construction that the output refers to something present. Definition 3 generalizes that guarantee across stores. A typed morphism `μ: 𝓘_a → 𝓘_b ∪ {⊥}` records a legal cast — document to memory path, tool output to ledger subject. A lineage for `c` is a witnessed path `ι_0 → … → c` with `ι_0` in the visible activation history `R_{≤t}`.

Three properties follow directly from the definition and are used throughout the manuscript:

1. **Existence is not lineage.** "If no path exists, `c` is unaligned with the activation history even when its display name is real in some registry." A citation to a real document that was never activated in this run fails. This is the "index echo" falsifier (§11.9, item 8).
2. **Lineage is not support.** A path shows that evidence was visible, not that it entails the claim. The generation predicate (deep dive 02 and §4.4) therefore adds `Fidelity` separately.
3. **Lineage is finite and checkable.** Given a finite trace, deciding whether a witnessed path exists is graph reachability, which is linear in nodes and edges. This is the basis of the verification bound in Proposition 10.

## 1.6 Content-bound receipts: what a hash does and does not show

Definition 4 introduces the receipt `R(u) = (digest, version, quoted_span, span_offset, verifier_id, intake_event, vector_clock, scope)`. The key analytical point is the difference between *binding* and *reading*. SHA-256 binds bytes to an identifier: if two parties hold the same digest they almost certainly hold the same bytes. It does not show that a model processed those bytes, that the processing preserved meaning, or that the holder was entitled to them. A system that reports "read 40 files" because it computed 40 hashes has demonstrated file access, not comprehension.

The quoted span chosen by a verifier is what moves the receipt from presence toward content: the receipt holder must reproduce a span the verifier selected, at an offset, which it cannot do without access to the content. Even this is only as strong as the verifier's independence. The manuscript's rule that "independent verification requires a verifier outside the process capable of forging the receipt" is the standard trust-boundary argument: if the same process chooses the challenge, holds the key, and checks the answer, it can produce passing receipts for content it never handled. Section 8.5 applies the same reasoning to in-process HMACs. This distinction is the basis of the PROV-002 hash-only falsifier and of mutation M03 (valid hash, wrong quoted span).

## 1.7 Scale trees: what "scale" means here

Definition 5 defines a ladder `s_0 > … > s_M` of partitions `P_k`, each refining the previous one: every child chunk has a unique parent containing it. Three choices in this definition carry the weight of later results.

**Finiteness.** `M` is finite and declared by the implementation. Every localization result in §6 depends on finite enumeration; nothing is claimed about limits.

**Refinement as containment.** Requiring `C ⊆ parent(C)` gives each fine item exactly one coarse ancestor. That is what makes the sticky case (deep dive 03) well defined and what makes failure localization a tree walk.

**Scales are audit levels, not model scales.** "Leaves represent the finest declared units, not unknowable token-level neural semantics." A scale may be a routing layer, a retrieval-to-claim stage, a tool boundary, a handoff, or a chunk refinement. The induction in §6.2 is over these declared levels. It is not induction over parameter count, training compute, or context length, and no result about those is implied. Keeping this explicit prevents the most tempting misreading of "induction on scales."

The manuscript also notes that "no formula for `M` is imported from geometry." In Guth–Wang–Zahl (2026) the scale chain `ρ_k = δ^{k/M}` is part of a proof; here depth is an engineering budget.

## 1.8 Density observables and boolean stickiness

Definitions 6–7 introduce `KT_k` (maximum ratio of selected chunks in a window to the data owner's expected count) and `F_k` (maximum concentration of supported mass inside a chunk). The names echo the Katz–Tao and Frostman conditions in the Kakeya literature, and the manuscript says plainly that they "are not the Katz–Tao or Frostman quantities themselves." They are computational analogues that detect two audit-relevant pathologies: over-concentration of selections in one region (many citations drawn from one window, suggesting the rest of the source was skipped) and over-concentration of support inside one chunk.

`STICKY_k(θ) := [KT_k ≤ θ_KT] ∧ [F_k ≤ θ_F]` becomes a boolean only because thresholds are supplied. If the denominator, measure, or expected count is unspecified, the observables are `UNKNOWN`; if the thresholds are unspecified, the result is `NO_VERDICT`. That rule — no hidden defaults — recurs everywhere and is examined in deep dive 02.

## 1.9 Events, happened-before, and slices

Definition 13's event tuple collects routing, proposals, commits, text, continuity state, reads, writes, actor, authority evidence, lineage edges, and clocks into one record per step, so all four predicate families read from a common trace. Definition 14 defines happened-before as the smallest relation containing program order, send/receive, intake/receipt, proposal/commit, and correction/dependency edges — Lamport's (1978) relation specialized to the event kinds that matter for certification. Wall clocks alone are insufficient across distributed components because clock skew can invert causal order; explicit edges cannot.

Definition 16's slice completeness rule — a predicate whose required inputs are absent returns `UNKNOWN` — is what prevents a truncated log from being certified. It is the foundation of every non-vacuity argument in the paper.

## 1.10 Summary of what this layer establishes

The foundation layer makes three things true by construction: every object a predicate inspects is unambiguous (typed, epoched, versioned); every relationship a predicate relies on is an explicit, witnessed edge in a finite graph; and every absent input produces a named non-pass rather than a default. Those three properties are what allow the later sections to state results about boolean outcomes that are provable rather than aspirational.
