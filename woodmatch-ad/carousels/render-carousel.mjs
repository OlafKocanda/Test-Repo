// Rendert ein Karussell-HTML in einzelne PNG-Slides (1080×1350) plus eine Übersicht.
// Nutzung: node render-carousel.mjs karussell-1-fragen.html
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import fs from 'node:fs';
import path from 'node:path';

const file = process.argv[2];
const name = path.basename(file, '.html');
const outDir = path.join('export', name);
fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto(pathToFileURL(path.resolve(file)).href);
await page.evaluate(() => window.ready);
const n = await page.evaluate(() => window.SLIDES);
await page.setViewportSize({ width: 1080 * n, height: 1350 });
for (let i = 0; i < n; i++) {
  await page.screenshot({ path: path.join(outDir, `${String(i + 1).padStart(2, '0')}.png`), clip: { x: i * 1080, y: 0, width: 1080, height: 1350 } });
}
// Übersicht (verkleinert, mit Trennlinien)
await page.addStyleTag({ content: `.slide{box-shadow:inset -3px 0 0 rgba(255,255,255,.9)}` });
await page.screenshot({ path: path.join('export', `${name}-uebersicht.png`), clip: { x: 0, y: 0, width: 1080 * n, height: 1350 }, scale: 'css' });
console.log(`${n} Slides → ${outDir}`);
await browser.close();
