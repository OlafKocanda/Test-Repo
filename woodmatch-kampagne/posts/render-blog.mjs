// Rendert alle Blog-Karussells aus blog-data.js nach export/blog-<name>/NN.png (+ Übersicht).
// Nutzung: node render-blog.mjs [name …]   (ohne Argument: alle)
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const src = fs.readFileSync('blog-data.js', 'utf8');
const all = [...src.matchAll(/^  (\w+): \{/gm)].map(m => m[1]);
const keys = process.argv.slice(2).length ? process.argv.slice(2) : all;
const browser = await chromium.launch();
for (const k of keys) {
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
  await page.goto(pathToFileURL(path.resolve('blog-karussell.html')).href + '?k=' + k);
  await page.evaluate(() => window.ready);
  const n = await page.evaluate(() => window.SLIDES);
  await page.setViewportSize({ width: 1080 * n, height: 1350 });
  const out = path.join('export', 'blog-' + k);
  fs.mkdirSync(out, { recursive: true });
  for (let i = 0; i < n; i++)
    await page.screenshot({ path: path.join(out, `${String(i + 1).padStart(2, '0')}.png`), clip: { x: i * 1080, y: 0, width: 1080, height: 1350 } });
  await page.addStyleTag({ content: `.slide{box-shadow:inset -3px 0 0 rgba(255,255,255,.9)}` });
  await page.screenshot({ path: path.join('export', `blog-${k}-uebersicht.png`), clip: { x: 0, y: 0, width: 1080 * n, height: 1350 } });
  console.log(`${k}: ${n} Slides → ${out}`);
  await page.close();
}
await browser.close();
