# Reference Verification Record

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

**Result.** 43 of 43 external references resolve to the stated work. One title was corrected (GraphAnchor) and seven author lists that the earlier bibliography left as placeholders were filled from the primary records. Venue/page fields for DOI-only references were carried over from the prior bibliography and were not re-read from the publisher page. The two Coleman (2026a/b) manuscripts are included in `sources/`.
