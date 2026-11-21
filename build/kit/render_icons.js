// node render_icons.js <icon.svg> <outdir>
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const [svgPath, outDir] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage();
  const svg = fs.readFileSync(svgPath, 'utf8');
  for (const [f, n] of [['icon-512.png',512],['icon-maskable-512.png',512],['icon-192.png',192],['apple-touch-icon.png',180],['favicon.png',32]]) {
    await p.setViewportSize({ width: n, height: n });
    await p.setContent(`<html><body style="margin:0">${svg.replace('<svg ', `<svg width="${n}" height="${n}" `)}</body></html>`);
    await p.screenshot({ path: path.join(outDir, f), clip: { x: 0, y: 0, width: n, height: n } });
  }
  await b.close();
})();
