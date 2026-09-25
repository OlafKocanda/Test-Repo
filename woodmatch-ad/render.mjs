// Rendert index.html Frame für Frame zu MP4 (H.264, 1080x1920, 30 fps).
// Nutzung: node render.mjs [out.mp4]      – komplettes Video
//          node render.mjs --stills 1,5,9 – einzelne Vorschaubilder
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';

const FFMPEG = process.env.FFMPEG || 'ffmpeg';
const FPS = 30;
// Musik: "Forest" von Damtaro (freetouse.com). Ab 11,6 s, damit der Drop (0:34) auf die Marktplatz-Szene fällt.
const MUSIC = process.env.MUSIC ?? 'assets/music-damtaro-forest.mp3';
const MUSIC_START = 11.6;
const args = process.argv.slice(2);
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto(pathToFileURL(path.resolve('index.html')).href);
await page.evaluate(() => window.ready);

if (args[0] === '--stills') {
  for (const t of args[1].split(',')) {
    await page.evaluate(t => window.render(t), +t);
    await page.screenshot({ path: `still-${t}.png` });
  }
} else {
  const out = args[0] || 'woodmatch-reel.mp4';
  const duration = await page.evaluate(() => window.DURATION);
  const ff = spawn(FFMPEG, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  const frames = Math.round(duration * FPS);
  for (let i = 0; i < frames; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 90 === 0) console.log(`frame ${i}/${frames}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  if (MUSIC) {
    // Musik anlegen: Ausschnitt ab MUSIC_START, weich ein- und ausblenden
    const tmp = out.replace(/\.mp4$/, '') + '.tmp.mp4';
    const mux = spawn(FFMPEG, ['-y', '-loglevel', 'error', '-i', out, '-ss', String(MUSIC_START), '-i', MUSIC,
      '-af', `afade=t=in:d=0.8,afade=t=out:st=${duration - 2.5}:d=2.5`, '-map', '0:v', '-map', '1:a',
      '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-t', String(duration), '-movflags', '+faststart', tmp], { stdio: 'inherit' });
    await new Promise(r => mux.on('close', r));
    (await import('node:fs')).renameSync(tmp, out);
  }
  console.log('fertig:', out);
}
await browser.close();
