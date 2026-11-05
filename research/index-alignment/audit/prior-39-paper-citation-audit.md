# Index Alignment: citation word counts and draft assessment

**Draft audited:** `/workspace/peaice/index-alignment-llms-arxiv-draft.md`  
**Audit date:** November 5, 2026 (America/Los_Angeles)

## Bottom line

- **Our draft:** **8,962 whitespace-delimited words** in the complete file; **8,296 words excluding the bibliography**; **7,705 words from Abstract through Conclusion**, excluding title/front matter, acknowledgments, bibliography, and appendices.
- **Cited literature:** 39 full texts counted, totaling **497,557 words**. Their mean is **12,758 words** and median is **11,944 words**. StateLedger is abstract-only (113 words) and excluded from these full-text statistics.
- Our full file is **70.2% of the cited-paper mean** and **75.0% of the median**. Excluding our bibliography, it is **65.0% of the mean** and **69.5% of the median**. This comparison is only approximate because cited-PDF counts include references and appendices while our body-only count does not.
- Closest full papers to our **8,962-word file**: **Read-ME** (8,916), **Ada-K v1** (8,915), **MemGPT** (8,631), **LEGOMem** (8,158), **Governed Shared Memory** (9,874), and **RAG** (9,911).
- **Assessment:** strong breadth, unusually clear role separation, useful formal scaffolding, and honest proposal labeling; not yet at the empirical or theoretical evidentiary standard of the stronger cited papers. It reads as a long position/framework paper with an evaluation plan, not a completed 25-page empirical research article.

## Counting method and limitations

1. Read the complete 40-entry References section. Found 37 arXiv IDs in the bibliography; also retrieved the two cited ACL Anthology papers and the StateLedger NeurIPS abstract. FactTrack has arXiv ID **2407.16347**, although the draft cites only its DOI.
2. Downloaded current arXiv PDFs, except Ada-K, whose current arXiv v2 is withdrawn and has no PDF; its original **v1** was used. The Dikkala and FactTrack counts use their published ACL Anthology PDFs.
3. Extracted PDF text with `pdftotext -layout`, repaired alphabetic line-break hyphenation, and removed standalone page-number lines. Counted whitespace-delimited tokens.
4. **Counts are estimates, not publisher-certified word totals.** They include front matter, author lists, captions, mathematics as extracted tokens, references, and appendices. Equations and two-column PDF extraction create noise. Image-only text is not OCRed. StateLedger is explicitly abstract-only. No counts were inferred from page counts.
5. The draft uses the same whitespace convention for reproducibility; Markdown syntax and mathematical expressions therefore contribute tokens. “Body” below means everything except the 666-word bibliography.

## Our draft: exact partitions

| Partition | Words | What it contains |
|---|---:|---|
| Complete file | **8,962** | Everything: title, author block, main text, bibliography, appendices |
| Before References heading | **7,766** | Title/front matter through Acknowledgments |
| Bibliography entries only | **666** | All 40 entries, excluding the `## References` heading |
| Body excluding pure bibliography | **8,296** | Complete file minus bibliography entries; includes title/front matter and appendices |
| Abstract through Conclusion | **7,705** | Main research-paper text only; excludes front matter, acknowledgments, bibliography, appendices |
| Appendices and end matter after bibliography | **527** | Appendices A–E, separators/end note as counted |

## Every referenced work

Counts in the table are **full-text estimates unless marked abstract-only**. Page counts are supplied as a cross-check, not used to estimate words.

| # | Citation | arXiv ID / other ID | Words | Pages | Source | Notes |
|---:|---|---|---:|---:|---|---|
| 1 | Sparsely-Gated Mixture-of-Experts | [1701.06538](https://arxiv.org/pdf/1701.06538) | 10,471 | 19 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 2 | GShard | [2006.16668](https://arxiv.org/pdf/2006.16668) | 19,211 | 35 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 3 | Switch Transformers | [2101.03961](https://arxiv.org/pdf/2101.03961) | 15,945 | 40 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 4 | Mixtral of Experts | [2401.04088](https://arxiv.org/pdf/2401.04088) | 4,908 | 13 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 5 | Survey on MoE in LLMs | [2407.06204](https://arxiv.org/pdf/2407.06204) | 26,303 | 29 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 6 | Ada-K Routing | [2410.10456](https://arxiv.org/pdf/2410.10456v1) | 8,915 | 16 | arXiv v1 PDF | Full text incl. front matter, references & appendices. Current arXiv v2 is withdrawn; original v1 used. Bibliography says Huang et al.; actual first author differs. |
| 7 | Read-ME | [2410.19123](https://arxiv.org/pdf/2410.19123) | 8,916 | 16 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 8 | Benefits of Learning to Route | [source](https://aclanthology.org/2023.emnlp-main.583.pdf) | 12,889 | 21 | ACL Anthology PDF | Full text incl. front matter, references & appendices. |
| 9 | Review of Sparse Expert Models | [2209.01667](https://arxiv.org/pdf/2209.01667) | 12,455 | 23 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 10 | Pointer Networks | [1506.03134](https://arxiv.org/pdf/1506.03134) | 4,996 | 9 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 11 | Retrieval-Augmented Generation | [2005.11401](https://arxiv.org/pdf/2005.11401) | 9,911 | 19 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 12 | LTRR | [2506.13743](https://arxiv.org/pdf/2506.13743) | 6,970 | 10 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 13 | Graph-Anchored Knowledge Indexing | [2601.16462](https://arxiv.org/pdf/2601.16462) | 13,180 | 22 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 14 | Knowledge Retrieval Indexer via Self-Learning | [2405.16933](https://arxiv.org/pdf/2405.16933) | 10,299 | 18 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 15 | Pointer-Guided Segment Ordering | [2406.04156](https://arxiv.org/pdf/2406.04156) | 6,808 | 17 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 16 | Toolformer | [2302.04761](https://arxiv.org/pdf/2302.04761) | 11,944 | 17 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 17 | ReAct | [2210.03629](https://arxiv.org/pdf/2210.03629) | 17,171 | 33 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 18 | HuggingGPT | [2303.17580](https://arxiv.org/pdf/2303.17580) | 13,691 | 27 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 19 | AutoGen | [2308.08155](https://arxiv.org/pdf/2308.08155) | 24,990 | 43 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 20 | MetaGPT | [2308.00352](https://arxiv.org/pdf/2308.00352) | 11,427 | 29 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 21 | Magentic-One | [2411.04468](https://arxiv.org/pdf/2411.04468) | 14,100 | 31 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 22 | LEGOMem | [2510.04851](https://arxiv.org/pdf/2510.04851) | 8,158 | 10 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 23 | MemGPT | [2310.08560](https://arxiv.org/pdf/2310.08560) | 8,631 | 13 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 24 | Generative Agents | [2304.03442](https://arxiv.org/pdf/2304.03442) | 20,101 | 22 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 25 | Governed Shared Memory | [2606.24535](https://arxiv.org/pdf/2606.24535) | 9,874 | 15 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 26 | TARL | [2608.03699](https://arxiv.org/pdf/2608.03699) | 23,528 | 32 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 27 | MAGE / Diachronic Hypergraphs | [2608.29678](https://arxiv.org/pdf/2608.29678) | 14,998 | 17 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 28 | StateLedger | [source](https://neurips.cc/virtual/2026/poster/151469) | 113 (abstract only) | — | NeurIPS HTML abstract | OpenReview full PDF was access-blocked; not included in 39-paper full-text statistics. |
| 29 | Scaling Laws for Neural LMs | [2001.08361](https://arxiv.org/pdf/2001.08361) | 15,556 | 30 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 30 | Training Compute-Optimal LLMs | [2203.15556](https://arxiv.org/pdf/2203.15556) | 15,460 | 36 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 31 | Stochastic Neurons for Conditional Computation | [1308.3432](https://arxiv.org/pdf/1308.3432) | 7,013 | 12 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 32 | Attention Is All You Need | [1706.03762](https://arxiv.org/pdf/1706.03762) | 6,134 | 15 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 33 | DSMoE | [2502.12455](https://arxiv.org/pdf/2502.12455) | 6,774 | 12 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 34 | Finedeep | [2502.12928](https://arxiv.org/pdf/2502.12928) | 7,770 | 14 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 35 | DOME | [2412.13575](https://arxiv.org/pdf/2412.13575) | 20,242 | 39 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 36 | SCORE | [2503.23512](https://arxiv.org/pdf/2503.23512) | 2,691 | 5 | arXiv PDF | Full text incl. front matter, references & appendices. Short 5-page version. |
| 37 | FactTrack | [2407.16347](https://aclanthology.org/2025.naacl-long.144.pdf) | 13,970 | 24 | ACL Anthology PDF | Full text incl. front matter, references & appendices. arXiv ID found: 2407.16347; counted published ACL version. |
| 38 | STORYWRITER | [2506.16445](https://arxiv.org/pdf/2506.16445) | 5,941 | 9 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 39 | RAG for LLMs: A Survey | [2312.10997](https://arxiv.org/pdf/2312.10997) | 15,560 | 21 | arXiv PDF | Full text incl. front matter, references & appendices. |
| 40 | Comprehensive MoE Survey | [2503.07137](https://arxiv.org/pdf/2503.07137) | 29,656 | 29 | arXiv PDF | Full text incl. front matter, references & appendices. |

## Length distribution

| Measure | Full-text cited papers (n=39) | Our complete file | Our file minus bibliography |
|---|---:|---:|---:|
| Words | Mean **12,758**; median **11,944** | **8,962** | **8,296** |
| Ratio to cited mean | 100% | **70.2%** | **65.0%** |
| Ratio to cited median | 100% | **75.0%** | **69.5%** |
| Range across cited papers | 2,691–29,656 | Within range | Within range |

Fourteen of 39 full-text papers are at or below our complete file length, so our draft is around the lower-middle of this particular bibliography by length. That is **not** a quality percentile: the set mixes short preprints, conference papers, long system papers, and surveys.

### Closest in length

| Cited paper | Words | Difference from our 8,962-word file |
|---|---:|---:|
| Read-ME | 8,916 | -46 |
| Ada-K Routing | 8,915 | -47 |
| MemGPT | 8,631 | -331 |
| LEGOMem | 8,158 | -804 |
| Governed Shared Memory | 9,874 | +912 |
| Retrieval-Augmented Generation | 9,911 | +949 |
| Finedeep | 7,770 | -1,192 |
| Knowledge Retrieval Indexer via Self-Learning | 10,299 | +1,337 |

## Assessment: details and delivery

### What is strong

1. **Clear central construct.** The four-part definition of index alignment is specific enough to discuss and test: routing–capability, routing–ledger, generation–index, and continuity–ledger consistency. The typed-index framing connects MoE, RAG, tools, and agents without reducing them to the same mechanism.
2. **Excellent role separation.** Non-authoritative routers, state ledgers, and generative continuity experts are distinguished by responsibility and write permissions. The capability-isolation table is one of the paper’s strongest delivery devices because it turns an analogy into an inspectable design constraint.
3. **Broad and current literature coverage.** Forty entries span foundational sparse computation, modern MoE routing, retrieval, tools, agent orchestration, memory, and narrative continuity. The paper generally connects a citation to a design implication instead of merely listing names.
4. **Useful formal and engineering scaffolding.** The draft has 23 display-math blocks, a reference architecture, pseudocode, nine Markdown tables, a worked trace, failure mappings, ablations, baselines, threats to validity, and a deployment checklist. This makes the proposal actionable.
5. **Honest claim boundaries.** “Proposal” appears 40 times. The draft explicitly says there are no new large-scale experiments and distinguishes hypotheses from results. That restraint is a real strength.
6. **Readable delivery.** The scenarios, comparison tables, anti-patterns, and migration path explain the idea to both researchers and system builders. The abstract accurately reflects the manuscript.

### What is weaker than the stronger cited work

1. **No empirical results.** Section 6 is a protocol, not an experiment section. Most primary cited papers supply implemented systems, datasets, quantitative results, and ablations. Our draft supplies metrics and hypotheses but no measured routing fidelity, ledger pollution reduction, continuity gains, task success, latency, or cost. This is the largest gap—not word count.
2. **Theory is suggestive rather than established.** The two “propositions” and the later pollution bound are informal. Definitions such as the task-specific distances in the alignment deficit and the continuity score are not operationalized enough for independent implementation. No proof establishes the claimed isolation benefit or contractive continuity behavior.
3. **Breadth dilutes depth.** MoE routing, citation attribution, transactional memory, agent orchestration, and narrative continuity each have different semantics and evaluation requirements. The paper needs either a tighter central theorem/evaluation or a clearly labeled position-paper genre. At present it sometimes moves from analogy to architectural obligation too quickly.
4. **Some claims outrun their cited evidence.** For example, the claim that prior work “rarely treats index alignment” needs a more systematic literature comparison. The information-theoretic discussion of routing entropy and the sample-complexity conjecture are plausible but not derived or validated. Index echoing should be treated as a candidate intervention, not presumed to improve faithfulness.
5. **Bibliographic metadata needs correction.** “Read-ME authors,” “LTRR authors,” and similar placeholders are not submission-ready author lists. Ada-K is listed as Huang et al., but the arXiv v1 author list begins Tongtian Yue; its current arXiv version is withdrawn even though an ICLR 2025 publication exists. FactTrack’s arXiv ID can be added. Every reference should be checked against the version actually cited.
6. **Structure needs a professional pass.** Numbering repeats and jumps: Section 5.5 and 5.6 recur after 5.8; 6.5 and 6.6 recur after 6.7; 7.8 is referenced but absent; 7.9 follows 7.7. Appendix E appears after the “End of draft” marker. Several constructs such as `**Design rules (**proposal**).**` have malformed nested emphasis.
7. **The draft is long but not yet information-dense in results.** Its detail is concentrated in definitions, patterns, restatements, and proposed metrics. Stronger empirical papers devote more space to exact configurations, result tables, statistical variation, error analysis, and reproducibility artifacts. Our repeated role summaries could be compressed to make room for evidence.
8. **Submission apparatus is incomplete.** Acknowledgments are a placeholder; there is no real rendered LaTeX/PDF, no reproducibility statement with artifacts, no ethics statement beyond short governance/security discussion, and no experimental appendix. “About 25 pages” is not established from Markdown word count alone; rendered length depends heavily on equations, tables, and formatting.

### Overall judgment

**Delivery is clear and promising; evidentiary detail is not yet comparable to the best cited papers.** As a position/framework manuscript, it is substantial and coherent, with a genuinely useful taxonomy and evaluation agenda. As a conventional arXiv research paper claiming a validated method, it is premature. More words would not solve the main problem. The highest-value revision is a small, well-controlled IA-MoA prototype with at least one routing/attribution task and one conflicting-memory task, matched baselines, reported variance, released traces, and a precise ledger transition specification.

### Recommended revision order

1. Decide explicitly between **position/framework paper** and **empirical systems paper**; adjust title, abstract, and claims accordingly.
2. Fix numbering, malformed emphasis, author metadata, withdrawn-version handling, and the end-of-draft placement.
3. Consolidate repeated role descriptions and pedagogical tables.
4. Define each distance term in the alignment deficit, ledger acceptance rules, continuity labels, and oracle-routing construction precisely.
5. Run a minimal empirical study with dense/scratchpad/no-isolation/no-continuity baselines, multiple seeds, cost/latency reporting, and failure cases.
6. Either strengthen the theoretical claims with formal assumptions and proofs or relabel them consistently as intuition/conjecture.
7. Render LaTeX/PDF before making a page-count claim and complete the submission checklists.

## Reproducibility artifacts

- Parsed bibliography: `/workspace/peaice/citation-wordcounts/refs.json`
- PDF acquisition results: `/workspace/peaice/citation-wordcounts/fetch-results.json`
- Extracted-text counts and page counts: `/workspace/peaice/citation-wordcounts/counts.json`
- Table data and statistics: `/workspace/peaice/citation-wordcounts/report-data.json`
- PDFs and extracted texts: `/workspace/peaice/citation-wordcounts/pdfs/` and `/workspace/peaice/citation-wordcounts/text/`
