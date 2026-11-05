# Boolean Index Alignment: citation word counts, prior-paper comparison, and rendered length

**Audit date:** November 5, 2026 (America/Los_Angeles)  
**Primary manuscript:** `/workspace/peaice/index-alignment-boolean-induction-2026-11-05.md`  
**Machine-readable counts:** `/workspace/peaice/boolean-induction-counts.json`

## Bottom line

- **New manuscript:** **19,935 whitespace-delimited words** in the complete Markdown file; **19,002 words excluding bibliography entries**; **15,628 words from Abstract through Conclusion**, excluding title/front matter, bibliography, and appendices.
- **Standalone abstract file:** **439 words**, complete file including its title, author block, keywords, and status line.
- **Rendered PDF:** **56 actual US-Letter pages**. The Abstract-through-Conclusion and preceding front matter occupy **42 substantive pages before the bibliography**. References occupy pages **43–45** (3 pages), and substantive appendices occupy pages **46–56** (11 pages). Thus there are **53 substantive pages including appendices and excluding bibliography**.
- The requirement of at least 40 substantive rendered pages is therefore met **even before bibliography and without counting appendices**: 42 pages. This is a PDF measurement, not a words-per-page estimate.
- The complete manuscript is **156.3% of the 39-paper cited-literature mean (12,758 words)** and **166.9% of the median (11,944 words)**. The body excluding bibliography is **148.9% of the mean** and **159.1% of the median**. These are length comparisons only, not quality or evidentiary percentiles.

## Exact new-manuscript partitions

| Partition | Words | Inclusion rule |
|---|---:|---|
| Complete Markdown file | **19,935** | Title, author/status front matter, main paper, references, appendices |
| Bibliography entries and reference-section headings | **933** | Text between `## References` and Appendix A, excluding only the `## References` heading and horizontal-rule-only lines |
| Body excluding bibliography | **19,002** | Complete file minus the 933 bibliography words; includes front matter and appendices |
| Abstract through Conclusion | **15,628** | From `## Abstract` through the end of Section 14, before `## References`; excludes front matter, references, and appendices |

The complete-file and body-excluding-bibliography figures use the same simple whitespace convention as the prior audit. “Bibliography” here includes the reference subsection content and excludes the section heading itself. No word count is inferred from the PDF.

## Both former papers as primary references

| Draft | Complete file | Excluding bibliography | Abstract through Conclusion | Audit status |
|---|---:|---:|---:|---|
| Coleman (2026a), *Index Alignment in Large Language Models* | **8,962** | **8,296** | **7,707** | Former primary reference; full local draft inspected |
| Coleman (2026b), *Kakeya Grain at the Slab* | **4,847** | **4,557** | **4,373** | Former primary reference; full local draft inspected |
| New continuation | **19,935** | **19,002** | **15,628** | New draft; rendered and measured |

The complete-file and bibliography-excluded counts for Coleman (2026a) reproduce the established audit exactly. Its Abstract-through-Conclusion count here is **7,707**, two words above the earlier note's **7,705**. The earlier partition appears to have applied an additional small cleanup that was not fully specified; to preserve a transparent rule, the present table counts every whitespace-delimited token between the Abstract heading and Acknowledgments, including Markdown headings and horizontal-rule tokens. This two-token discrepancy is disclosed rather than silently overwriting the prior audit. The new count uses the same explicit heading-to-References rule, with no Acknowledgments section present.

For Coleman (2026b), Abstract through Conclusion means the text from `## Abstract` through the paragraph ending “Nothing in this paper was published to lovelabslca.com or peaice.org.”, before `## References`. Its bibliography count includes the external-mathematics and internal-source subsections under References, but not the `## References` heading.

## Comparison with the established cited-literature distribution

The earlier citation audit counted **39 full-text papers**, totaling **497,557 words**, with mean **12,758** and median **11,944**. StateLedger is abstract-only (113 words) and excluded from full-text statistics.

| Measure | 39-paper full-text distribution | New complete file | New body excluding bibliography |
|---|---:|---:|---:|
| Mean comparison | 12,758 | **19,935 (156.3%)** | **19,002 (148.9%)** |
| Median comparison | 11,944 | **19,935 (166.9%)** | **19,002 (159.1%)** |
| Observed range | 2,691–29,656 | Within range | Within range |

This comparison is approximate in kind: the 39 cited-PDF counts generally include references and appendices, whereas the new body-only count excludes bibliography but includes appendices. Longer is not better. The new draft's contribution is formalization, conditional proofs, failure localization, traces, and evaluation design; it still reports no new experiments and does not match an empirical paper's evidentiary burden by length alone.

The complete prior-paper table, individual 39 full-text counts, page counts, methods, and limitations remain in `/workspace/peaice/index-alignment-citation-wordcounts.md`. They are extended here rather than recomputed or replaced.

## New external citations: counting status

The continuation adds scholarly references used for attribution/support, causal citation faithfulness, long-context position effects, omissions, module diagnosis, agent verification, conformity, selective evaluation, criteria drift, governance, refinement, runtime verification, noninterference, linearizability, happened-before, and open addressing. Their bibliographic landing pages or abstracts were inspected for the specific roles stated in the manuscript. **Their full texts were not re-counted this turn**, and no word totals are invented for them.

New external works not included in the earlier 39-paper mean/median are:

1. Rashkin et al. (2023), *Measuring Attribution in Natural Language Generation Models* — not re-counted this turn.
2. Gao et al. (2023), *Enabling Large Language Models to Generate Text with Citations* — not re-counted this turn.
3. Wallat et al. (2024), *Correctness is not Faithfulness in RAG Attributions* — not re-counted this turn.
4. Liu et al. (2024), *Lost in the Middle* — not re-counted this turn.
5. Kim et al. (2024), *FABLES* — not re-counted this turn.
6. Ru et al. (2024), *RAGChecker* — not re-counted this turn.
7. Sung, Kim, and Zhang (2025), *VeriLA* — not re-counted this turn.
8. Sharma et al. (2024), *Towards Understanding Sycophancy in Language Models* — not re-counted this turn.
9. Weng, Chen, and Wang (2025), *Do as We Do, Not as You Think* — not re-counted this turn.
10. Wang et al. (2025), *Cer-Eval* — not re-counted this turn.
11. Wan et al. (2025), *Derailer-Rerailer* — not re-counted this turn.
12. Shankar et al. (2024), *Who Validates the Validators?* — not re-counted this turn.
13. Grill (2024), *Constructing Capabilities* — not re-counted this turn.
14. Abadi and Lamport (1991), *The Existence of Refinement Mappings* — not re-counted this turn.
15. Bauer, Leucker, and Schallhart (2011), *Runtime Verification for LTL and TLTL* — not re-counted this turn.
16. Farach-Colton, Krapivin, and Kuszmaul (2024/2025), *Optimal Bounds for Open Addressing Without Reordering* — not re-counted this turn.
17. Goguen and Meseguer (1982), *Security Policies and Security Models* — not re-counted this turn.
18. Herlihy and Wing (1990), *Linearizability* — not re-counted this turn.
19. Lamport (1978), *Time, Clocks, and the Ordering of Events in a Distributed System* — not re-counted this turn.

Wang–Zahl, Guth–Wang–Zahl, and Wang–Wu are inherited mathematical background from Coleman (2026b), not silently inserted into the earlier LLM bibliography's 39-paper statistics. Their full texts were not re-counted for this continuation.

## Counting method and limitations

1. Counts use Python `len(text.split())`: whitespace-delimited tokens, not a publisher's word processor count.
2. Markdown syntax, headings, URLs, code, JSON keys, and mathematical expressions contribute tokens. This creates extraction/counting noise but is reproducible.
3. “Complete file” includes everything. “Body excluding bibliography” subtracts bibliography content only. “Abstract through Conclusion” includes the Abstract heading, section headings, display text, tables, and any horizontal-rule tokens within that span.
4. The established cited-PDF method used `pdftotext -layout`, repaired alphabetic line-break hyphenation, and removed standalone page-number lines. PDF mathematics and two-column extraction add noise; image-only text was not OCRed.
5. New external citation metadata checks do not imply full-PDF review. The earlier 39-paper statistics are reused, not represented as freshly recomputed.
6. Public Git archive extraction is unrelated to scholarly word counting. The handoff reports 717 extracted research-text files; extraction does not mean those files were read, validated, or counted here.

## Reproducible PDF settings and actual page boundaries

**PDF:** `/workspace/peaice/index-alignment-boolean-induction-2026-11-05.pdf`  
**Renderer script:** `/workspace/peaice/render_boolean_induction.py`  
**CSS:** `/workspace/peaice/index-alignment-boolean-induction-render.css`  
**Dependency lock:** `/workspace/peaice/render-requirements-freeze.txt`

Settings:

- Python virtual environment `/workspace/peaice/render-venv`; Markdown and WeasyPrint installed locally, not system-wide.
- US Letter, **612 × 792 points**.
- Margins **0.82 in left/right/top and 0.80 in bottom**.
- Body **11 pt DejaVu Serif**, line height **1.35**, justified; conventional running header and centered page number.
- Sans-serif headings; monospace code; tables with fixed borders and wrapping; widows/orphans set to 3.
- Forced page breaks before References and Appendix A to make the count boundary unambiguous.

Reproduction commands:

```bash
/workspace/peaice/render-venv/bin/python /workspace/peaice/render_boolean_induction.py
pdfinfo /workspace/peaice/index-alignment-boolean-induction-2026-11-05.pdf
pdftotext -layout /workspace/peaice/index-alignment-boolean-induction-2026-11-05.pdf \
  /workspace/peaice/index-alignment-boolean-induction-2026-11-05-pdf.txt
```

Measured result:

| Pages | Content |
|---|---|
| **1–42** | Front matter, Abstract, Sections 1–14 through Conclusion; **42 substantive pre-bibliography pages** |
| **43–45** | References; **3 bibliography pages** |
| **46–56** | Appendices A–H; **11 substantive appendix pages** |
| **1–56 total** | **56 pages**, of which **53 are substantive when appendices count and bibliography is excluded** |

Final independent visual inspection covered title/abstract, routing and ledger predicates, refinement and coverage, restricted verification, correction traces, metrics, status tables, references, JSON, pseudocode, notation/mutation tables, and the final checklist. Text extraction verified actual section boundaries. No page total is inferred from Markdown length alone. Final corrections added non-vacuity explicitly to `RELEASE_FULL`, qualified the restricted verifier bound with shared-traversal and bounded-check assumptions, separated first-fail from first-non-pass, clarified UNKNOWN versus NO_VERDICT and preserved witnessed transfer failures in pseudocode, distinguished evidence cycles from incomplete evidence, included the combined team notes in contributor accounting without naming the inaccessible room as a contributor, and corrected EvalGen to UIST. The 39-paper distribution and 19-addition/geometry-not-re-counted labels were preserved unchanged.
