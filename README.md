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
