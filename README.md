# PeAIce · Grok Index (hosted module)

**Goal.** Host the Grok Index module so lovelabslca.com embeds it with a one-line iframe instead of 550 lines of code.

**Why.** The IONOS HTML Module held a pile of concatenated documents (the L²_C Granular Compaction module and the Grok Index Module, each with its own meta tags and stylesheet), which made it hard to update. This repo holds one standalone `index.html` with a single head and scoped styles; content is unchanged and kept in the same order.

**How it's checked.** https://manny536.github.io/peaice-grok-index/ returns 200 and allows framing; the page's visible text matches the source module word for word, and every link and image is checked to resolve.

Embed:

```html
<iframe src="https://manny536.github.io/peaice-grok-index/" title="PeAIce · Grok Index" style="width:100%;height:HEIGHTpx;border:0;display:block" loading="lazy"></iframe>
```
