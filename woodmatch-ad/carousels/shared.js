// Gemeinsame Bausteine für die WoodMatch-Karussells (1080×1350 je Slide, als Panorama nebeneinander).
// Keine Fotos: Illustrationen (Bäume, Höhenlinien, Wanderweg) werden als SVG erzeugt.
const W = 1080, H = 1350;

function rng(seed) { return () => (seed = (seed * 16807) % 2147483647) / 2147483647; }

// Stilisierter Wald als Streifen: mehrere Ebenen (hinten hell, vorne dunkel)
function forestSVG(width, seed, layers) {
  const r = rng(seed);
  let out = '';
  for (const L of layers) {
    // Hügel als Boden der Ebene
    let d = `M0 ${H} L0 ${L.y}`;
    for (let x = 0; x <= width + 200; x += 200) d += ` S ${x + 100} ${L.y + (r() - .5) * L.hill} ${x + 200} ${L.y + (r() - .5) * L.hill * .6}`;
    d += ` L ${width} ${H} Z`;
    out += `<path d="${d}" fill="${L.ground}"/>`;
    for (let x = -40; x < width + 40; x += L.step * (.6 + r() * .8)) {
      const s = L.scale * (.75 + r() * .5), y = L.y + (r() - .5) * 18;
      if (r() < L.spruce) {
        const w = 46 * s, h = 150 * s;
        out += `<g fill="${L.tree}"><rect x="${x - 3 * s}" y="${y - 14 * s}" width="${6 * s}" height="${24 * s}"/>` +
          `<polygon points="${x},${y - h} ${x - w * .55},${y - h * .45} ${x + w * .55},${y - h * .45}"/>` +
          `<polygon points="${x},${y - h * .75} ${x - w * .8},${y - h * .15} ${x + w * .8},${y - h * .15}"/>` +
          `<polygon points="${x},${y - h * .5} ${x - w},${y} ${x + w},${y}"/></g>`;
      } else {
        const rr = 36 * s;
        out += `<g fill="${L.tree}"><rect x="${x - 4 * s}" y="${y - 40 * s}" width="${8 * s}" height="${46 * s}"/>` +
          `<circle cx="${x}" cy="${y - 70 * s}" r="${rr}"/><circle cx="${x - rr * .6}" cy="${y - 48 * s}" r="${rr * .75}"/><circle cx="${x + rr * .6}" cy="${y - 50 * s}" r="${rr * .8}"/></g>`;
      }
    }
  }
  return `<svg class="pano" width="${width}" height="${H}" viewBox="0 0 ${width} ${H}">${out}</svg>`;
}

// Höhenlinien als dezentes Hintergrundmuster
function topoSVG(width, seed, color, opacity = .18) {
  const r = rng(seed); let out = '';
  for (let k = 0; k < 14; k++) {
    const y0 = 60 + k * 70 + r() * 30; let d = `M-50 ${y0}`;
    for (let x = 0; x <= width + 300; x += 300) d += ` S ${x + 150} ${y0 + (r() - .5) * 120} ${x + 300} ${y0 + (r() - .5) * 60}`;
    out += `<path d="${d}" fill="none" stroke="${color}" stroke-width="2"/>`;
  }
  return `<svg class="pano" width="${width}" height="${H}" style="opacity:${opacity}" viewBox="0 0 ${width} ${H}">${out}</svg>`;
}

// Gestrichelter Wanderweg über alle Slides mit nummerierten Wegpunkten
function trailSVG(width, points, color, labels = []) {
  let d = `M ${points[0][0]} ${points[0][1]}`;
  for (let i = 1; i < points.length; i++) {
    const [x0, y0] = points[i - 1], [x1, y1] = points[i], mx = (x0 + x1) / 2;
    d += ` C ${mx} ${y0}, ${mx} ${y1}, ${x1} ${y1}`;
  }
  const pins = labels.map((l, i) => l == null ? '' : `<g transform="translate(${points[i][0]} ${points[i][1]})">
      <circle r="34" fill="${color}"/><text y="11" text-anchor="middle" font-size="30" font-weight="800" fill="#10240f">${l}</text></g>`).join('');
  return `<svg class="pano" width="${width}" height="${H}" viewBox="0 0 ${width} ${H}"><path d="${d}" fill="none" stroke="${color}" stroke-width="6" stroke-dasharray="4 18" stroke-linecap="round"/>${pins}</svg>`;
}

function buildStage(n, bgHTML, slides) {
  const st = document.getElementById('stage');
  st.style.width = n * W + 'px';
  st.innerHTML = bgHTML + slides.map((s, i) => `<section class="slide" style="left:${i * W}px">${s}</section>`).join('');
  window.SLIDES = n;
}
