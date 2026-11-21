const V = 'sheffield-v2';
const CORE = ["vendor/leaflet.js", "vendor/leaflet.css", "./", "index.html", "data.js", "manifest.webmanifest", "icon-192.png", "icon-512.png", "apple-touch-icon.png", "favicon.png", "img/cover.svg", "img/n1.svg", "img/n10.svg", "img/n11.svg", "img/n12.svg", "img/n13.svg", "img/n14.svg", "img/n15.svg", "img/n16.svg", "img/n17.svg", "img/n18.svg", "img/n19.svg", "img/n2.svg", "img/n20.svg", "img/n21.svg", "img/n22.svg", "img/n23.svg", "img/n24.svg", "img/n25.svg", "img/n26.svg", "img/n27.svg", "img/n28.svg", "img/n29.svg", "img/n3.svg", "img/n30.svg", "img/n31.svg", "img/n32.svg", "img/n33.svg", "img/n34.svg", "img/n35.svg", "img/n36.svg", "img/n37.svg", "img/n38.svg", "img/n39.svg", "img/n4.svg", "img/n40.svg", "img/n41.svg", "img/n42.svg", "img/n43.svg", "img/n44.svg", "img/n45.svg", "img/n46.svg", "img/n47.svg", "img/n48.svg", "img/n49.svg", "img/n5.svg", "img/n50.svg", "img/n51.svg", "img/n52.svg", "img/n53.svg", "img/n54.svg", "img/n55.svg", "img/n56.svg", "img/n6.svg", "img/n7.svg", "img/n8.svg", "img/n9.svg", "img/transit.svg"];
const EXT = [];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(CORE).then(() => Promise.all(EXT.map(u => c.add(u).catch(() => {}))))));
  self.skipWaiting();
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V && k !== 'sheffield-tiles').map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET') return;
  if (u.hostname === 'tile.openstreetmap.org') {
    // map tiles: cache as you browse so viewed areas work offline
    e.respondWith(caches.open('sheffield-tiles').then(c => c.match(e.request).then(hit => {
      const net = fetch(e.request).then(r => { if (r.ok || r.type === 'opaque') c.put(e.request, r.clone()); return r; }).catch(() => hit);
      return hit || net;
    })));
    return;
  }
  // app shell (pages, data, scripts): network first, so updates arrive as soon as you're online; cache is the offline fallback
  if (u.origin === location.origin && !u.pathname.includes('/img/') && !u.pathname.includes('/vendor/')) {
    e.respondWith(fetch(e.request).then(r => {
      if (r.ok) caches.open(V).then(c => c.put(e.request, r.clone()));
      return r;
    }).catch(() => caches.match(e.request, {ignoreSearch: true}).then(h => h || caches.match('index.html'))));
    return;
  }
  e.respondWith(caches.match(e.request, {ignoreSearch: true}).then(hit => {
    const net = fetch(e.request).then(r => {
      if (r.ok && (u.origin === location.origin || u.hostname.includes('unpkg') || u.hostname.includes('fonts.g'))) caches.open(V).then(c => c.put(e.request, r.clone()));
      return r;
    }).catch(() => hit || caches.match('index.html'));
    return hit || net;
  }));
});
