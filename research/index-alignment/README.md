# Index Alignment Research Package

**Boolean Index Alignment: Traceable Induction on Scales for Sparse Language-Model Systems**
Manuel Coleman · AgreeYa Solutions (Computacenter), Folsom, CA · November 5, 2026

This package contains the manuscript, its abstract, nine deep-dive research documents that develop and support every major claim, a claim–evidence matrix, the verified bibliography, and the two former papers it continues.

## Contents

| Path | What it is |
|---|---|
| `index-alignment-boolean-induction.md` / `.pdf` | Main manuscript (55 pages rendered) |
| `ABSTRACT.md` | Standalone abstract |
| `deep-dives/01-index-foundations.md` | Typed indices, registries, lineage, receipts, scale trees |
| `deep-dives/02-boolean-evidence-semantics.md` | Semantic vs evidence layers, strong Kleene soundness, non-compensation, non-vacuity |
| `deep-dives/03-scale-refinement-composition.md` | R/C/N/K, annotated proof of cross-scale induction, sticky/non-sticky, shared-budget counterexample |
| `deep-dives/04-routing-ledger-continuity.md` | The four predicate families and the literature that motivates each clause |
| `deep-dives/05-correction-causal-freshness.md` | Corrections, happened-before, vector-clock staleness, affected closure, storms |
| `deep-dives/06-custody-release.md` | Custody vs authority vs release, S·H·U, five outcomes, partial release |
| `deep-dives/07-localization-traces.md` | First failure, frontiers, two-ends/directional checks, the fourteen traces as a coverage argument |
| `deep-dives/08-evaluation-falsification.md` | Fixtures, mutations, execution taxonomy, independent labels, metrics, baselines, cost |
| `deep-dives/09-related-work-bibliography.md` | Annotated bibliography and positioning |
| `index-alignment-deep-dives.pdf` | All deep dives plus the matrix in one PDF |
| `CLAIM-EVIDENCE-MATRIX.md` | 47 major claims → manuscript section → deep-dive anchor → primary citations; seat-contribution paths |
| `REFERENCES.md` | Bibliography (45 entries) |
| `sources/` | Coleman (2026a) and Coleman (2026b), the two former papers |
| `audit/` | Reference verification record, render script and HTML, PDF text extraction, prior citation/word-count audits |
| `SHA256SUMS` | Checksums of every file in the package |

## Reading order

Abstract → manuscript §§1–4 with deep dives 01–02 → §§5–6 with 03 → §§7–8 with 04–06 → §9 with 07 → §§10–11 with 08 → §12 and references with 09. The matrix lets any claim be traced directly to its argument and sources.

## Sources and scope

Built from the full manuscript, both former papers, the seat contributions listed in the matrix, the AIce public repository documents named there, and the public scholarly records in `audit/reference-verification.md`. Only public repositories were used; private repositories, `-Colemanfiles`, quarantined material, and legacy GIUS material are not part of this package.

Verify integrity with `sha256sum -c SHA256SUMS`.
