# PeAIce · Grok Index (hosted module)

**Goal.** Host the Grok Index module so lovelabslca.com embeds it with a one-line iframe instead of 550 lines of code.

**Why.** The IONOS HTML Module held a pile of concatenated documents (the L²_C Granular Compaction module and the Grok Index Module, each with its own meta tags and stylesheet), which made it hard to update. This repo holds one standalone `index.html` with a single head and scoped styles. The two original modules are unchanged and kept in the same order. A third section, after them, holds the Boolean Index Alignment continuation. A fourth section, after that, holds the November 2026 Excellence Engine v4 cross-model compaction research, including the original evidence screenshots.

**How it's checked.** https://manny536.github.io/peaice-grok-index/ returns 200 and allows framing; the two original modules' visible text matches the source module word for word, and every link and image is checked to resolve. The continuation section's local document links resolve inside this repository.

Embed:

```html
<iframe src="https://manny536.github.io/peaice-grok-index/" title="PeAIce · Grok Index" style="width:100%;height:HEIGHTpx;border:0;display:block" loading="lazy"></iframe>
```

## Boolean Index Alignment continuation

The root navigation links to [Boolean Index Alignment](research/index-alignment/README.md). The manuscript is Manuel Coleman, *Boolean Index Alignment: Traceable Induction on Scales for Sparse Language-Model Systems* (5 November 2026). `research/index-alignment/` holds that package: the manuscript and its [57-page PDF](research/index-alignment/index-alignment-boolean-induction.pdf), the abstract, nine deep dives, the deep-dive PDF, the claim–evidence matrix, the reference list, Coleman (2026a) and Coleman (2026b) under `sources/`, the audit files, and `SHA256SUMS`. The Granular Compaction module and the Grok Index module stay above it, in their existing wording. The Cross-model compaction section follows it and does not change those modules.

The independent review, organized literature and applied corrections are linked from the [research package](research/index-alignment/README.md). All 47 listed claims were assessed; the architecture and LLM evaluation remain proposed.

## Cross-model compaction research (November 2026)

**Goal.** Put the Excellence Engine v4 cross-model compaction study on the public Home module, dated November 2026, so the Love Labs Home embed can show it.

**Why.** The formal package is on `Manny536/excellence-engine-v4` at [evaluations/cross-model-compaction](https://github.com/Manny536/excellence-engine-v4/tree/main/evaluations/cross-model-compaction), merged through [PR #19](https://github.com/Manny536/excellence-engine-v4/pull/19), [PR #20](https://github.com/Manny536/excellence-engine-v4/pull/20), [PR #21](https://github.com/Manny536/excellence-engine-v4/pull/21), and [PR #22](https://github.com/Manny536/excellence-engine-v4/pull/22), with the Frozen definition and standing meaning of \(h < 1\) from [AIce PR #12](https://github.com/Manny536/AIce/pull/12) and [PR #13](https://github.com/Manny536/AIce/pull/13). The Home page embeds this repository’s root `index.html`. The new section, at `#cross-model-compaction`, states what the study asks, the audit design, Frozen, the one standing meaning of \(h < 1\), the recorded live evidence and its scope, and the items that remain open. Original screenshots from the package are in `assets/compaction/`, with SHA-256 sums matching the EEv4 manifests. The three earlier Home modules stay byte-for-byte.

**How it's checked.** `python3 references/check_catalog.py` still requires the Granular Compaction, Grok Index, and Boolean Index Alignment modules to match their recorded SHA-256 values, and now also records the Cross-model compaction section. Every copied screenshot is checked against the EEv4 SHA-256 manifests. A 388-pixel-wide headless pass checks that the new section does not overflow horizontally.


## PeAIce reference catalog (Services)

**Goal.** Give Love Labs Services its own research-reference subpage. The page is [references/index.html](references/index.html), published at `https://manny536.github.io/peaice-grok-index/references/`. It indexes discovered peaice.org paths. It is a research-index catalog. Research validation is outside its scope.

**Services integration.** The root `index.html` stays the Home embed. It contains Granular Compaction, the Grok Index at `#grok-index`, Boolean Index Alignment, and the November 2026 Cross-model compaction section at `#cross-model-compaction`, with the same embed-end `postMessage`. The three earlier modules stay byte-for-byte. The catalog is not inserted into that file, and Home has no link to it. Services loads the catalog with a separate iframe. Catalog navigation lives on the catalog page. That page has its own `#embed-end` script, so Services sizes this frame from this document’s height.

```html
<iframe src="https://manny536.github.io/peaice-grok-index/references/" title="PeAIce reference catalog" style="width:100%;border:0;display:block" loading="lazy"></iframe>
```

Use the `embedHeight` posted by the references page. A modest starting height is enough until that message arrives. Do not reuse the Home frame, and do not pin an enormous fixed height.

**Game frame.** The shooter paints 1:1 into its iframe, so the catalog sizes that one frame instead of cropping it. In the Services column, and any catalog viewport under 840px, the stage is a 5:8 page and uses the full catalog width. At 840px and wider it is 16:10. Viewport-height units are not used for this stage, because the outer frame's height is the catalog's own `embedHeight`. Expand game asks the game iframe to go fullscreen. Open game leaves the catalog for the game page. The simulator keeps a separate frame, `min(36rem, 640px)`, and its scrolling stays in that frame (`overscroll-behavior: contain`). Wheel input on the game does not chain to the catalog (`overscroll-behavior: none`).

The live Services module already listens for `embedHeight` and starts the outer iframe at 900px. Two host changes are still required, and they are outside this repository:

```html
<iframe src="https://manny536.github.io/peaice-grok-index/references/" title="PeAIce reference catalog" style="width:100%;border:0;display:block;height:900px" loading="lazy" allow="fullscreen" allowfullscreen></iframe>
```

`allow="fullscreen"` and `allowfullscreen` are required on that outer frame. Without them, Expand game cannot leave the nested iframe. Keep the existing `message` listener so the outer height follows `embedHeight`. A fixed outer height will clip the taller game stage. `references/nested-scroll-fixture.html` is a local 600px column used to check that wheel input on the game does not scroll the page around it.

The module currently sits in `grid-column-medium-6` / `grid-column-large-8` beside an empty column, inside `section-inner-width-small` (960px). That is the ~600px column. The game already uses 100% of that width. A wider arena means moving this HTML module to a full-width row (`grid-column-small-12 grid-column-medium-12 grid-column-large-12`). This repository cannot change that IONOS layout.

**Why it is separate.** The catalog is not placed inside a KakeyaLogic frame. Whole peaice.org pages are linked. The inventory said framing those pages was untested and recommended link cards. The only frames on the catalog are the two demos on Manuel Coleman's GitHub Pages, `/games` and `/pnp-loop`, each capped at `min(28rem, 70vh)`. The public page does not repeat this integration note.

**Canonical root.** Public PeAIce links use `https://peaice.org/lovelabslca`. The site root, `http://peaice.org`, `https://peaice.org`, and `https://www.peaice.org` fold into that home. `https://peaice.org/lovelabslca/` folds into the same page without the trailing slash.

**Why it is checked.** A redirect should stay attached to its reachable destination, a 404 should stay out of the public links, a login wall should stay out of the public links, a broken embed should stay described as broken, and a source label (OPEN, PROPOSED, ARCHIVED, superseded) should stay the label the inventory records. Benevolence Drift is written in full. RH and proof language is not upgraded. The check compares the page with the inventory file rather than with a later recollection of it.

**Included.** From [references/inventory.csv](references/inventory.csv), the 6 November 2026 hand-off:

- 56 input URL rows.
- 52 unique normalized paths.
- 51 rows with `primary_record` yes: 32 canonical pages, 4 GitHub Pages redirects (`/games`, `/pnp`, `/pnp-loop`, `/report`), 1 duplicate-content alias (`/blueprint`), 2 Google Doc landings (`/Grok`, `/deepseekr1`), and 12 unreachable paths.
- 40 catalog records. That is every normalized path whose representative row is HTTP 200. The 40th record is `https://peaice.org/`. Every CSV input row for that root, including `https://peaice.org/` itself, says `primary_record` `no (see normalized_url row)`, and there is no primary=yes row. The normalized path is still one of the 52, it redirects to `https://peaice.org/lovelabslca`, and the catalog records it once.
- Each of the 40 has one sentence taken from the inventory purpose and shows the reachable destination URL. OPEN, PROPOSED, ARCHIVED, and superseded appear on the card only when the inventory records that label. The public page states once: “Status labels appear where the source carries them.”
- Groups: Research map (3), Featured papers (3), KakeyaLogic and geometry (7), Benevolence Drift and benchmarks (9), Thinking Machines archive (10), Interactive demos (2), Reports and model exchange (4), Errata (2).

**Excluded, and where the exclusion is visible.**

- 12 unreachable paths, listed in the public “Link status and unavailable records” section and not linked: 11 HTTP 404, and `https://peaice.org/outcomes1gpt` as HTTP 401. The 401 path redirects to a login-protected chatgpt.site URL. That URL is written as text so the failure is identifiable, and it is not a link.
- `/dpsa` is one of the 40 because the page returned HTTP 200. The public sentence is: “The page is reachable, but its embedded Canva asset returns 404. Its purpose is not stated in the available text.” The broken asset is not embedded and not linked.
- 4 input forms folded into a record, not given their own cards: `http://peaice.org`, `https://peaice.org` (no trailing slash), `https://www.peaice.org`, and `https://peaice.org/lovelabslca/`. The inventory prose names the three root/www/scheme/slash variants; the CSV adds the no-slash `https://peaice.org` row.
- 140 raw local references (asset URLs, blob object IDs, malformed captures) are not copied. The hand-off kept them in a separate file that is not this repository.
- Third-party image, video, playlist, and Google Doc bodies are not copied into this repo. Google Docs are link-only. peaice.org pages are not framed.
- The pre-existing Granular Compaction archive on Home still names `/appendix` among older destinations. `/appendix` is an HTTP 404 in the catalog’s unavailable list. That Home sentence is unchanged historical module text. The Grok Index block is unchanged.

**How it is checked.** `python3 references/check_catalog.py` reads `references/inventory.csv`, `references/index.html`, and this README. It checks the 56/52/51/40/12/4 counts in the inventory and requires this README to keep that accounting, including the 4 folded input forms and the 140 raw local references that are not copied. On the public page it checks that each included path appears once with the inventory destination and relation, that each explanation carries its source snippet, that OPEN, PROPOSED, ARCHIVED, and superseded stay on the cards that have them, that the 12 unavailable paths and the login URL are not `href`s, that `/outcomes1gpt` stays HTTP 401 with the login requirement distinct from the HTTP 404 rows, that `/dpsa` uses the reachable-page sentence above, that the only iframes are the two demos on Manuel Coleman's GitHub Pages and have no fixed height attribute, that new catalog copy spells Benevolence Drift in full, that the references page carries its own embed-end script, and that the root `index.html` keeps the three original modules byte-for-byte and the same embed-end behavior, with the Cross-model compaction section as a fourth Home module. `python3 references/check_catalog.py --live` additionally GETs each included destination and reports the HTTP status. The local check compares the catalog with the inventory file.
