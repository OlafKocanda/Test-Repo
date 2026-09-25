// Rendert App-Zustände aus ../index.html als freigestellte Laptop-PNGs für die Karussells.
import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const SHOTS = [
  // [Datei, Zeitpunkt, Kamera [cx, cy, z] oder null = wie im Video]
  ['laptop-uebersicht.png', 9.7, [800, 426, 1]],
  ['laptop-suche-flurstueck.png', 12.5, [600, 300, 1.35]],
  ['laptop-karte-baumart.png', 14.6, null],
  ['laptop-polter.png', 18.6, null],
  ['laptop-massnahme.png', 20.9, null],
  ['laptop-fbg.png', 26.0, null],
];
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto(pathToFileURL(path.resolve('../index.html')).href);
await page.evaluate(() => window.ready);
for (const [file, t, camPos] of SHOTS) {
  await page.evaluate(([t, camPos]) => {
    window.render(t);
    if (camPos) {
      const [cx, cy, z] = camPos, SW = 964, SH = 513, K = SW / 1600, sc = K * z;
      const tx = Math.min(0, Math.max(SW - 1600 * sc, SW / 2 - cx * sc));
      const ty = Math.min(0, Math.max(SH - 852 * sc, SH / 2 - cy * sc));
      document.getElementById('app').style.transform = `translate(${tx}px, ${ty}px) scale(${sc})`;
    }
    // alles außer dem Laptop ausblenden, Hintergrund transparent
    for (const s of ['html', 'body', '#stage', '#features']) document.querySelector(s).style.background = 'transparent';
    document.querySelectorAll('#stage > .scene').forEach(el => { if (el.id !== 'features') el.style.visibility = 'hidden'; });
    document.querySelectorAll('#features > *').forEach(el => { if (el.id !== 'laptop') el.style.visibility = 'hidden'; });
    document.getElementById('features').style.opacity = 1; document.getElementById('features').style.visibility = 'visible';
    const lp = document.getElementById('laptop'); lp.style.transform = 'none'; lp.style.visibility = 'visible';
  }, [t, camPos]);
  await page.screenshot({ path: 'assets/' + file, omitBackground: true, clip: { x: 0, y: 630, width: 1080, height: 680 } });
  console.log(file);
}
await browser.close();
