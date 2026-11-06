# Index Alignment Research Package

**Boolean Index Alignment: Traceable Induction on Scales for Sparse Language-Model Systems**
Manuel Coleman · AgreeYa Solutions (Computacenter), Folsom, CA · November 5, 2026

This package contains the manuscript, its abstract, nine companion research documents, a revised claim–evidence matrix, an annotated bibliography, and the two historical papers it continues. An independent source review assessed all 47 listed claims; its findings and applied corrections are included in `audit/`. The architecture remains proposed and no LLM efficacy evaluation is reported.

## Contents

| Path | What it is |
|---|---|
| `index-alignment-boolean-induction.md` / `.pdf` | Main manuscript, 57 pages, regenerated from current Markdown |
| `ABSTRACT.md` | Standalone abstract |
| `deep-dives/01-index-foundations.md` | Typed indices, registries, lineage, receipts, scale trees |
| `deep-dives/02-boolean-evidence-semantics.md` | Semantic vs evidence layers, strong Kleene soundness, non-compensation, non-vacuity |
| `deep-dives/03-scale-refinement-composition.md` | R/C/N/K, annotated proof of cross-scale induction, sticky/non-sticky, shared-budget counterexample |
| `deep-dives/04-routing-ledger-continuity.md` | The four predicate families and the literature that motivates each clause |
| `deep-dives/05-correction-causal-freshness.md` | Corrections, happened-before, vector-clock staleness, affected closure, storms |
| `deep-dives/06-custody-release.md` | Custody vs authority vs release, S·H·U, five outcomes, partial release |
| `deep-dives/07-localization-traces.md` | First failure, frontiers, two-ends/directional checks, the fourteen traces as selected illustrations |
| `deep-dives/08-evaluation-falsification.md` | Fixtures, mutations, execution taxonomy, independent labels, metrics, baselines, cost |
| `deep-dives/09-related-work-bibliography.md` | Annotated bibliography and positioning |
| `index-alignment-deep-dives.pdf` | All deep dives plus the matrix in one 48-page PDF |
| `CLAIM-EVIDENCE-MATRIX.md` | 47 major claims → manuscript section → deep-dive anchor → primary citations; seat-contribution paths |
| `REFERENCES.md` | Bibliography (51 entries; StateLedger unresolved) |
| `sources/` | Coleman (2026a) and Coleman (2026b), the two former papers and their linked errata |
| `audit/` | Independent review, literature lists, revision dispositions, finite specification checks, reference record, renderer, HTML, PDF text and historical audits |
| `SHA256SUMS` | Checksums of every file in the package |

## Independent review

Start with [applied corrections](audit/REVISION.md), the [full review](audit/independent-research-review.md), [organized papers](audit/organized-literature.md) and [source errata](sources/ERRATA.md). The review is critical source research, not external peer review or experimental validation. The 14 worked traces and 32 mutation designs remain unexecuted as an LLM evaluation; the small deterministic specification checks have a separately labeled receipt.

## Reading order

Abstract → manuscript §§1–4 with deep dives 01–02 → §§5–6 with 03 → §§7–8 with 04–06 → §9 with 07 → §§10–11 with 08 → §12 and references with 09. The matrix lets any claim be traced directly to its argument and sources.

## Sources and scope

The original authoring package attributes material to both former papers, local seat packets and public repository documents. The independent review checked the supplied archive against the pinned GitHub folder and researched scholarly sources. Historical local seat packets and the 26-repository handoff inventory were not included, so their reported contents and totals were not independently reconstructed. Current reference limits appear in `audit/reference-verification.md`. Only public repositories were used; private repositories, `-Colemanfiles`, quarantined material, and legacy GIUS material are not part of this package.

Run finite checks with `python3 audit/check_specification.py`. See [rendering instructions](audit/RENDERING.md) to rebuild the PDFs. Verify integrity with `sha256sum -c SHA256SUMS` (Linux) or `shasum -a 256 -c SHA256SUMS` (macOS).
