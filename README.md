# PeAIce · Grok Index (hosted module)

**Goal.** Host the Grok Index module so lovelabslca.com embeds it with a one-line iframe instead of 550 lines of code.

**Why.** The IONOS HTML Module held a pile of concatenated documents (the L²_C Granular Compaction module and the Grok Index Module, each with its own meta tags and stylesheet), which made it hard to update. This repo holds one standalone `index.html` with a single head and scoped styles. The two original modules are unchanged and kept in the same order. A third section, after them, holds the Boolean Index Alignment continuation.

**How it's checked.** https://manny536.github.io/peaice-grok-index/ returns 200 and allows framing; the two original modules' visible text matches the source module word for word, and every link and image is checked to resolve. The continuation section's local document links resolve inside this repository.

Embed:

```html
<iframe src="https://manny536.github.io/peaice-grok-index/" title="PeAIce · Grok Index" style="width:100%;height:HEIGHTpx;border:0;display:block" loading="lazy"></iframe>
```

## Boolean Index Alignment continuation

The root navigation links to [Boolean Index Alignment](research/index-alignment/README.md). The manuscript is Manuel Coleman, *Boolean Index Alignment: Traceable Induction on Scales for Sparse Language-Model Systems* (5 November 2026). `research/index-alignment/` holds that package: the manuscript and its [57-page PDF](research/index-alignment/index-alignment-boolean-induction.pdf), the abstract, nine deep dives, the deep-dive PDF, the claim–evidence matrix, the reference list, Coleman (2026a) and Coleman (2026b) under `sources/`, the audit files, and `SHA256SUMS`. The Granular Compaction module and the Grok Index module stay above it, in their existing wording.

The independent review, organized literature and applied corrections are linked from the [research package](research/index-alignment/README.md). All 47 listed claims were assessed; the architecture and LLM evaluation remain proposed.

## PeAIce reference catalog (Services)

**Goal.** Give Love Labs Services its own research-reference subpage. The page is [references/index.html](references/index.html), published at `https://manny536.github.io/peaice-grok-index/references/`. It indexes discovered peaice.org paths. It is a research-index catalog. Research validation is outside its scope.

**Services integration.** The root `index.html` stays the Home embed. It still contains only Granular Compaction, the Grok Index at `#grok-index`, and Boolean Index Alignment, with the same embed-end `postMessage`. The catalog is not inserted into that file, and Home has no link to it. Services loads the catalog with a separate iframe. Catalog navigation lives on the catalog page. That page has its own `#embed-end` script, so Services sizes this frame from this document’s height.

```html
<iframe src="https://manny536.github.io/peaice-grok-index/references/" title="PeAIce reference catalog" style="width:100%;border:0;display:block" loading="lazy"></iframe>
```

Use the `embedHeight` posted by the references page. A modest starting height is enough until that message arrives. Do not reuse the Home frame, and do not pin an enormous fixed height.

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

**How it is checked.** `python3 references/check_catalog.py` reads `references/inventory.csv`, `references/index.html`, and this README. It checks the 56/52/51/40/12/4 counts in the inventory and requires this README to keep that accounting, including the 4 folded input forms and the 140 raw local references that are not copied. On the public page it checks that each included path appears once with the inventory destination and relation, that each explanation carries its source snippet, that OPEN, PROPOSED, ARCHIVED, and superseded stay on the cards that have them, that the 12 unavailable paths and the login URL are not `href`s, that `/outcomes1gpt` stays HTTP 401 with the login requirement distinct from the HTTP 404 rows, that `/dpsa` uses the reachable-page sentence above, that the only iframes are the two demos on Manuel Coleman's GitHub Pages and have no fixed height attribute, that new catalog copy spells Benevolence Drift in full, that the references page carries its own embed-end script, and that the root `index.html` is unchanged, including its three modules and its embed-end behavior. `python3 references/check_catalog.py --live` additionally GETs each included destination and reports the HTTP status. The local check compares the catalog with the inventory file.
