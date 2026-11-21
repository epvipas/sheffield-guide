const V = '{{V}}';
const CORE = {{CORE}};
const EXT = [];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(CORE).then(() => Promise.all(EXT.map(u => c.add(u).catch(() => {}))))));
  self.skipWaiting();
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== V && k !== '{{TILES}}').map(k => caches.delete(k)))));
  self.clients.claim();
});
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET') return;
  if (u.hostname === 'tile.openstreetmap.org') {
    // map tiles: cache as you browse so viewed areas work offline
    e.respondWith(caches.open('{{TILES}}').then(c => c.match(e.request).then(hit => {
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
