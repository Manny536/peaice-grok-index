# Rendering and finite specification checks

Run `python3 audit/check_specification.py` from the research package. This uses only the Python standard library and rewrites `audit/specification-checks.json`. It exercises small specification examples; it is not an implementation or empirical evaluation of INDEX-ALIGN-CERT.

The PDF renderer requires Node.js, `marked`, `playwright`, a Chromium-compatible browser and DejaVu fonts. Install the dependencies declared in `audit/package.json` in a suitable environment and supply a local browser. The renderer itself makes no network requests. Run `python3 audit/render.py` from any working directory; all input/output paths are resolved relative to the renderer.

Optional environment variables:

| Variable | Meaning |
|---|---|
| `NODE_BINARY` | Node executable for the Python wrapper |
| `NODE_MODULES_DIR` | Existing dependency directory when dependencies are not beside the script |
| `CHROMIUM_PATH` | Local Chromium/Chrome executable; otherwise Playwright's installed Chromium |
| `FONT_DIR` | Directory containing the seven DejaVu TTF files named in `render.mjs`; embeds them during PDF rendering |

Outputs are both PDFs plus `audit/manuscript.html` and `audit/deep-dives.html`. Source text is parsed locally; the companion PDF concatenates all nine deep dives and the current claim matrix in filename order. The saved HTML uses locally installed fonts. `FONT_DIR` supplies fonts embedded during PDF rendering without bundling font files in the repository. Browser/font versions affect pagination and PDF bytes; hashes identify the published rendering, not a claim of bit-for-bit rebuilds across environments.

After rendering, extract text from both PDFs, check key passages and inspect page images (especially tables, equations and page boundaries). Update the current `audit/QA.md` record and `SHA256SUMS` only after the final artifacts are complete. The manifest covers all package files except itself and ignored dependency/cache directories. It may be checked with `shasum -a 256 -c SHA256SUMS` on macOS or `sha256sum -c SHA256SUMS` on Linux.
