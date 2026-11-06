# Reference verification — independent-review revision

November 5, 2026 (America/Los_Angeles). The bibliography now has 51 entries: two same-author unpublished manuscripts and 49 external entries. Reference 23 (StateLedger) remains unresolved and is excluded from substantive support. The former blanket “43/43 verified” conclusion is not adopted.

The [45-entry identity audit](bibliography-identity-audit.csv) records the review of the original bibliography; the [organized literature](organized-literature.md) contains 20 prioritized papers and source links. Identity, source contents, claim support and experimental replication are different checks. The independent review used SciSpace for discovery and selected extractions, then primary records to check substantive points. Its generated search metadata was corrected when primary records disagreed. No claim of full-text reading or replication of every reference is made.

| Entry / issue | Current disposition |
|---|---|
| 13, Wu et al., arXiv:2601.16462v2 | Primary §3.2 names KAIR; evolving keyword/relation/RDF indexing supports the mechanism description. GraphAnchor alias removed from current claims. |
| 23, claimed StateLedger NeurIPS poster | Given primary page inaccessible; no confirming primary record recovered by the review. Unresolved, not a finding of nonexistence. |
| 46, Necula 1997 | Original Proof-Carrying Code paper; DOI 10.1145/263699.263712. A later SciSpace record was not used as the original publication. |
| 47, Chaki et al. 2009 | NASA record 20150004720 confirms title and four authors, including Charles Weinstock. |
| 48, Saltzer & Schroeder 1975 | Primary paper; DOI 10.1109/PROC.1975.9939. Established security principles, not validation of this framework. |
| 49, Kadyrbek & Mansurova 2026 | Publisher identifies Scientific Reports, correcting SciSpace venue metadata. DOI 10.1038/s41598-026-74900-x. Reported small tests and microbenchmark do not validate INDEX-ALIGN-CERT. |
| 50, Liu Yanglet et al. 2026 | arXiv:2605.24462; trace certification proposal/formal background, not field efficacy evidence. |
| 51, Debenedetti et al. 2024 | arXiv:2406.13352; AgentDojo supplies an external adversarial evaluation comparison. |

The current manuscript and REFERENCES.md contain identical numbered entries. The original check is retained below as provenance, with its narrower methods and superseded conclusion visible.

---

# Original authoring check (historical)

Checked November 5, 2026 (America/Los_Angeles) from the box.

**Method.** arXiv entries were queried through the arXiv API (`export.arxiv.org/api/query?id_list=…`) and the returned title and author list compared with the bibliography. ACL Anthology and NeurIPS virtual pages were fetched and their page titles and schema.org author records compared. DOIs were resolved through `doi.org` (HTTP 302 redirect to publisher = resolves).

| Ref | Identifier | Check | Result |
|---|---|---|---|
| Shazeer 2017 | arXiv:1701.06538 | API title/authors | match (7 authors) |
| Lepikhin 2020 | arXiv:2006.16668 | API | match (9 authors; full list now in bibliography) |
| Fedus 2022 | arXiv:2101.03961 | API | match |
| Jiang 2024 | arXiv:2401.04088 | API | match |
| Cai W. 2024 | arXiv:2407.06204 | API | match |
| Yue 2024 (Ada-K) | arXiv:2410.10456 | API | match; current version v2 |
| Cai R. 2024 (Read-ME) | arXiv:2410.19123 | API | authors filled from record: Cai, Ro, Kim, Wang, Bejnordi, Akella, Wang |
| Vinyals 2015 | arXiv:1506.03134 | API | match |
| Lewis 2020 | arXiv:2005.11401 | API | match |
| Kim & Diaz 2025 (LTRR) | arXiv:2506.13743 | API | authors filled from record |
| Wu M. 2026 (GraphAnchor) | arXiv:2601.16462 | API | **title corrected** to "Finding What Matters: Anchoring Context Knowledge with Evolving Indices for Iterative Retrieval"; authors filled |
| Liang 2024 (PG-RAG) | arXiv:2405.16933 | API | authors filled from record |
| Schick 2023 | arXiv:2302.04761 | API | match |
| Yao 2023 | arXiv:2210.03629 | API | match |
| Wu Q. 2023 | arXiv:2308.08155 | API | match |
| Hong 2023 | arXiv:2308.00352 | API | match |
| Fourney 2024 | arXiv:2411.04468 | API | match |
| Packer 2023 | arXiv:2310.08560 | API | match |
| Park 2023 | arXiv:2304.03442 | API | match |
| Xiao 2026 (TARL) | arXiv:2608.03699 | API | authors filled from record |
| Yang 2026 (StateLedger) | neurips.cc/virtual/2026/poster/151469 | page JSON-LD | authors filled: Geer Yang, Xixuan Liu, Bin Wu, Shaojiang Wang |
| Wang & Zahl 2025 | arXiv:2502.17655 | API | match |
| Guth, Wang & Zahl 2026 | arXiv:2601.14411 | API | match |
| Wang & Wu 2024 | arXiv:2411.08871 | API | match |
| Rashkin 2023 | aclanthology 2023.cl-4.2 | page title | match |
| Gao 2023 | arXiv:2305.14627 | API | match |
| Wallat 2024 | arXiv:2412.18004 | API | match |
| Liu 2024 | aclanthology 2024.tacl-1.9 | page title | match |
| Kim Y. 2024 | arXiv:2404.01261 | API | match |
| Ru 2024 | arXiv:2408.08067 | API | match |
| Sung 2025 | arXiv:2503.12651 | API | match |
| Sharma 2024 | arXiv:2310.13548 | API | match |
| Weng 2025 | arXiv:2501.13381 | API | match |
| Wang G. 2025 | arXiv:2505.03814 | API | match |
| Wan 2025 | aclanthology 2025.findings-acl.18 | page title | match |
| Shankar 2024 | arXiv:2404.12272 | API | match |
| Grill 2024 | doi:10.1145/3630106.3659009 | doi.org | resolves |
| Abadi & Lamport 1991 | doi:10.1016/0304-3975(91)90224-P | doi.org | resolves |
| Bauer et al. 2011 | doi:10.1145/2000799.2000800 | doi.org | resolves |
| Farach-Colton et al. | arXiv:2501.02305 | API | match |
| Goguen & Meseguer 1982 | doi:10.1109/SP.1982.10014 | doi.org | resolves |
| Herlihy & Wing 1990 | doi:10.1145/78969.78972 | doi.org | resolves |
| Lamport 1978 | doi:10.1145/359545.359563 | doi.org | resolves |

**Original reported result (not adopted by the independent review).** 43 of 43 external references resolve to the stated work. One title was corrected (GraphAnchor) and seven author lists that the earlier bibliography left as placeholders were filled from the primary records. Venue/page fields for DOI-only references were carried over from the prior bibliography and were not re-read from the publisher page. The two Coleman (2026a/b) manuscripts are included in `sources/`.
