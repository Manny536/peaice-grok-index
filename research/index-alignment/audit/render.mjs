// Local-only rendering of both research documents from their current Markdown.
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';

const audit = path.dirname(fileURLToPath(import.meta.url));
const root = path.dirname(audit);
const require = createRequire(process.env.NODE_MODULES_DIR
  ? path.join(process.env.NODE_MODULES_DIR, '..', 'package.json')
  : import.meta.url);
const { marked } = await import(pathToFileURL(require.resolve('marked')).href);
const { chromium } = require('playwright');
const baseCss = await fs.readFile(path.join(audit, 'render.css'), 'utf8');
let css = baseCss;
// Embed fonts only during PDF rendering; saved HTML uses locally installed fonts.
if (process.env.FONT_DIR) {
  const fonts = [
    ['DejaVu Serif', 'DejaVuSerif.ttf', 'normal', 'normal'],
    ['DejaVu Serif', 'DejaVuSerif-Bold.ttf', 'bold', 'normal'],
    ['DejaVu Serif', 'DejaVuSerif-Italic.ttf', 'normal', 'italic'],
    ['DejaVu Serif', 'DejaVuSerif-BoldItalic.ttf', 'bold', 'italic'],
    ['DejaVu Sans', 'DejaVuSans.ttf', 'normal', 'normal'],
    ['DejaVu Sans', 'DejaVuSans-Bold.ttf', 'bold', 'normal'],
    ['DejaVu Sans Mono', 'DejaVuSansMono.ttf', 'normal', 'normal'],
  ];
  const rules = await Promise.all(fonts.map(async ([family, name, weight, style]) => {
    const bytes = await fs.readFile(path.join(process.env.FONT_DIR, name));
    return `@font-face{font-family:'${family}';font-weight:${weight};font-style:${style};src:url(data:font/ttf;base64,${bytes.toString('base64')}) format('truetype');}`;
  }));
  css = rules.join('\n') + '\n' + css;
}
const manuscript = await fs.readFile(path.join(root, 'index-alignment-boolean-induction.md'), 'utf8');
const dives = (await fs.readdir(path.join(root, 'deep-dives'))).filter(x => x.endsWith('.md')).sort();
const companion = [
  '# Boolean Index Alignment: Deep Dives and Claim–Evidence Matrix\n\nManuel Coleman · Independent-review revision · November 5, 2026\n\nNine companion essays and the current 47-claim map. Definitions and examples are proposed or conditional; no LLM efficacy evaluation is reported. The archived review and source errata are in the package audit and sources folders.\n',
  ...await Promise.all(dives.map(name => fs.readFile(path.join(root, 'deep-dives', name), 'utf8'))),
  await fs.readFile(path.join(root, 'CLAIM-EVIDENCE-MATRIX.md'), 'utf8'),
].join('\n\n---\n\n');
const docs = [
  ['manuscript', 'index-alignment-boolean-induction.pdf', manuscript],
  ['deep-dives', 'index-alignment-deep-dives.pdf', companion],
];
const browser = await chromium.launch({ headless: true,
  ...(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}) });
try {
  for (const [stem, output, markdown] of docs) {
    let body = marked.parse(markdown, { gfm: true, breaks: false });
    body = body.replace(/<h2>(References|Appendix A\.[^<]*)<\/h2>/g, '<h2 class="new-page">$1</h2>');
    body = body.replace(/(<h1>Claim–Evidence Matrix<\/h1>[\s\S]*?)<table>/, '$1<table class="claim-matrix">');
    const html = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Boolean Index Alignment — ${stem}</title><style>${css}</style></head><body>${body}</body></html>`;
    const htmlPath = path.join(audit, `${stem}.html`);
    await fs.writeFile(htmlPath, html.replace(css, baseCss));
    const page = await browser.newPage();
    await page.route(/^https?:\/\//, route => route.abort());
    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: 'load' });
    await page.addStyleTag({ content: css });
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.join(root, output), printBackground: true,
      preferCSSPageSize: true, tagged: true, outline: true });
    await page.close();
    process.stdout.write(`Rendered ${output}\n`);
  }
} finally { await browser.close(); }
