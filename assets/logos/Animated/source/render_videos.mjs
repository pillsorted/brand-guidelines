// Renders the MP4 on Brand Pink and the transparent WebM from the Lottie JSON, frame by frame, with lottie-web
// (the web Lottie player) in headless Chromium, then encodes them with ffmpeg.
//
// Run from this folder:
//   npm install
//   npx playwright-core install chromium-headless-shell   (once per machine)
//   node render_videos.mjs
// Needs ffmpeg on the PATH.

import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium } from 'playwright-core';

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = dirname(HERE);
const NAME = 'PS-Logo-Wordmark-White-Animated';
const BRAND_PINK = '#eb1f79';
const SCALE = 3;

const animation = JSON.parse(readFileSync(join(OUT, `${NAME}.json`), 'utf8'));
const { w, h, fr, ip, op } = animation;
const lottieJs = createRequire(import.meta.url).resolve('lottie-web/build/player/lottie.min.js');

const frames = mkdtempSync(join(tmpdir(), 'ps-logo-frames-'));
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
try {
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: SCALE });
  await page.setContent(`<html><body style="margin:0;background:transparent"><div id="a" style="width:${w}px;height:${h}px"></div></body></html>`);
  await page.addScriptTag({ path: lottieJs });
  await page.evaluate((data) => new Promise((resolve) => {
    window.anim = lottie.loadAnimation({ container: document.getElementById('a'), renderer: 'svg', loop: false, autoplay: false, animationData: data });
    window.anim.addEventListener('DOMLoaded', resolve);
  }), animation);
  for (let frame = ip; frame < op; frame++) {
    await page.evaluate((n) => window.anim.goToAndStop(n, true), frame);
    const png = await page.screenshot({ omitBackground: true });
    writeFileSync(join(frames, `${String(frame - ip).padStart(4, '0')}.png`), png);
  }
} finally {
  await browser.close();
}

const input = ['-y', '-loglevel', 'error', '-framerate', String(fr), '-i', join(frames, '%04d.png')];
const size = `${w * SCALE}x${h * SCALE}`;
execFileSync('ffmpeg', [
  '-y', '-loglevel', 'error', '-f', 'lavfi', '-i', `color=c=${BRAND_PINK}:s=${size}:r=${fr}`,
  ...input.slice(3),
  '-filter_complex', '[0][1]overlay=shortest=1,format=yuv420p', '-c:v', 'libx264', '-crf', '18', '-movflags', '+faststart',
  join(OUT, `${NAME}-on-Pink.mp4`),
]);
execFileSync('ffmpeg', [
  ...input, '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p', '-b:v', '0', '-crf', '30', '-auto-alt-ref', '0',
  join(OUT, `${NAME}-Transparent.webm`),
]);
rmSync(frames, { recursive: true });
console.log(`wrote ${NAME}-on-Pink.mp4 and ${NAME}-Transparent.webm (${size}, ${op - ip} frames at ${fr} fps)`);
