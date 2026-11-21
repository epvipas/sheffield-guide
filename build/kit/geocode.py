"""Look up coordinates for places without them.  python3 build/kit/geocode.py  (from repo root)
Prints each match so you can spot wrong ones; add ll=(lat, lon) in places.py to override."""
import json, os, sys, time, urllib.parse, urllib.request
KIT = os.path.dirname(os.path.abspath(__file__)); BUILD = os.path.dirname(KIT)
sys.path.insert(0, KIT); sys.path.insert(0, BUILD)
CFG = json.load(open(os.path.join(BUILD, "city.json")))
import cats; cats.CITY = CFG["city"]
import places  # noqa
from cats import P
gp = os.path.join(BUILD, "geo.json"); g = json.load(open(gp)) if os.path.exists(gp) else {}
lat, lon = CFG["center"]; vb = f"{lon-0.35},{lat+0.25},{lon+0.35},{lat-0.25}"
for p in P:
    if p["name"] in g: continue
    res = []
    for bounded in (1, 0):
        q = {"q": p["geo"], "format": "json", "limit": 1, "countrycodes": "gb"}
        if bounded: q.update(viewbox=vb, bounded=1)
        try:
            res = json.load(urllib.request.urlopen(urllib.request.Request("https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode(q),
                  headers={"User-Agent": "city-guide-builder/1.0"}), timeout=20))
        except Exception: res = []
        time.sleep(1.1)
        if res or not p["far"]: break
    g[p["name"]] = [(float(x["lat"]), float(x["lon"]), x["class"], x["type"], x["display_name"][:80]) for x in res]
    print(("OK   " if res else "NONE ") + p["name"][:40].ljust(40) + (res[0]["display_name"][:70] if res else f'  (ll={p["ll"]})'))
json.dump(g, open(gp, "w"), indent=0)
