from pathlib import Path
import markdown
from weasyprint import HTML, CSS

root=Path('/workspace/peaice')
src=Path('/workspace/peaice/index-alignment-research/index-alignment-boolean-induction.md')
out=Path('/workspace/peaice/index-alignment-research/index-alignment-boolean-induction.pdf')
text=src.read_text()
body=markdown.markdown(text, extensions=['extra','tables','fenced_code','sane_lists','toc'])
body=body.replace('<h2 id="references">References</h2>', '<h2 class="new-page">References</h2>').replace('<h2 id="appendix-a-json-like-certificate-schema">Appendix A. JSON-Like Certificate Schema</h2>', '<h2 class="new-page">Appendix A. JSON-Like Certificate Schema</h2>')
css=r'''
@page {
  size: Letter;
  margin: 0.82in 0.82in 0.80in 0.82in;
  @bottom-center { content: counter(page); font-family: "DejaVu Serif", serif; font-size: 9pt; color:#333; }
  @top-right { content: "Boolean Index Alignment — Manuel Coleman"; font-family: "DejaVu Sans", sans-serif; font-size: 7.5pt; color:#555; }
}
@page :first { @top-right { content: none; } }
html { font-family: "DejaVu Serif", "Liberation Serif", serif; font-size: 11pt; line-height: 1.35; color: #111; }
body { margin:0; padding:0; }
h1 { font-family:"DejaVu Sans",sans-serif; font-size:20pt; line-height:1.17; text-align:center; margin:0.12in 0 0.18in; color:#102b46; }
h2.new-page { break-before: page; }
h2 { font-family:"DejaVu Sans",sans-serif; font-size:14pt; line-height:1.2; margin:0.22in 0 0.09in; color:#153e60; border-bottom:0.7pt solid #8199ab; padding-bottom:3pt; break-after:avoid; }
h3 { font-family:"DejaVu Sans",sans-serif; font-size:11.1pt; line-height:1.25; margin:0.16in 0 0.055in; color:#1e4b69; break-after:avoid; }
p { margin:0 0 0.075in; text-align:justify; orphans:3; widows:3; }
strong { color:#101d29; }
ul,ol { margin:0.035in 0 0.085in 0.23in; padding-left:0.12in; }
li { margin:0 0 0.027in; }
code { font-family:"DejaVu Sans Mono","Liberation Mono",monospace; font-size:8.8pt; overflow-wrap:anywhere; }
pre { font-family:"DejaVu Sans Mono","Liberation Mono",monospace; font-size:8.1pt; line-height:1.24; white-space:pre-wrap; overflow-wrap:anywhere; background:#f3f5f7; border-left:2.5pt solid #54768e; padding:7pt 8pt; margin:0.08in 0 0.11in; break-inside:avoid; }
pre code { font-size:inherit; }
table { width:100%; border-collapse:collapse; margin:0.08in 0 0.12in; font-family:"DejaVu Sans",sans-serif; font-size:7.7pt; line-height:1.2; }
th { background:#e5edf2; color:#102b46; font-weight:bold; }
th,td { border:0.5pt solid #7f8f99; padding:3.4pt 3.8pt; text-align:left; vertical-align:top; overflow-wrap:anywhere; }
tr { break-inside:avoid; }
a { color:#164c74; text-decoration:none; overflow-wrap:anywhere; }
blockquote { margin:0.08in 0.15in; padding-left:0.12in; border-left:2pt solid #777; color:#333; }
hr { border:0; border-top:0.6pt solid #aaa; margin:0.16in 0; }
'''
html='<!doctype html><html><head><meta charset="utf-8"><title>Boolean Index Alignment</title></head><body>'+body+'</body></html>'
(src.parent/'audit'/'manuscript.html').write_text(html)
HTML(string=html, base_url=str(root)).write_pdf(str(out), stylesheets=[CSS(string=css)])
(src.parent/'audit'/'render.css').write_text(css)
print(out)
