"""Build a city guide PWA.  Usage: python3 build/kit/make.py   (run from the repo root)

Reads build/city.json, build/places.py, build/content.html, build/info.js, build/geo.json
and writes index.html, data.js, img/, manifest.webmanifest, sw.js, icons.
"""
import json, math, os, random, re, shutil, subprocess, sys

KIT = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(KIT)
OUT = os.path.dirname(BUILD)
sys.path.insert(0, KIT); sys.path.insert(0, BUILD)

import svgs
from svgs import GEN, wrap, sky, clouds, warehouse
CFG = json.load(open(os.path.join(BUILD, "city.json")))
import cats
cats.CITY = CFG["city"]
import places  # noqa: F401  (fills cats.P)
from cats import P, CATS

geo = {}
gp = os.path.join(BUILD, "geo.json")
if os.path.exists(gp): geo = json.load(open(gp))

def dist(a, b):
    R = 6371000; t = math.radians
    h = math.sin(t(b[0]-a[0])/2)**2 + math.cos(t(a[0]))*math.cos(t(b[0]))*math.sin(t(b[1]-a[1])/2)**2
    return 2*R*math.asin(math.sqrt(h))

def coords(p):
    r = geo.get(p["name"]) or []
    if r:
        g = tuple(r[0][:2])
        if not p["ll"] or dist(g, p["ll"]) < 400: return g
    if p["ll"]: return tuple(p["ll"])
    raise SystemExit("no coords for " + p["name"] + " (run build/kit/geocode.py or give ll=)")

BASE = CFG["base"]
os.makedirs(os.path.join(OUT, "img"), exist_ok=True)

# stable ids across rebuilds
try:
    prev = json.loads(open(os.path.join(OUT, "data.js")).read()[len("window.GUIDE="):].rstrip().rstrip(";"))
    IDS = {it["name"]: it["id"] for it in prev["items"]}
except Exception:
    IDS = {}
RENAMED = CFG.get("renamed", {})
nxt = [max([int(v[1:]) for v in IDS.values()] + [0]) + 1]
def stable_id(name):
    pid = IDS.get(name) or IDS.get(RENAMED.get(name, ""))
    if not pid:
        pid = f"n{nxt[0]}"; nxt[0] += 1
    return pid

names = [p["name"] for p in P]
dups = {n for n in names if names.count(n) > 1}
if dups: raise SystemExit("duplicate names: " + ", ".join(dups))

items = []
for p in P:
    lat, lon = coords(p)
    pid = stable_id(p["name"])
    r = random.Random(CFG["slug"] + p["name"])
    open(os.path.join(OUT, "img", pid + ".svg"), "w").write(wrap(GEN[p["cat"]](r, "g" + pid)))
    walk = max(1, round(dist((BASE["lat"], BASE["lon"]), (lat, lon)) * 1.3 / 80))
    q = p["name"] + ", " + p["addr"] + ("" if CFG["city"].lower() in p["addr"].lower() else ", " + CFG["city"])
    items.append(dict(id=pid, cat=p["cat"], name=p["name"], addr=p["addr"], text=p["text"], tip=p["tip"],
                      lat=round(lat, 6), lon=round(lon, 6), price=p["price"], walk=walk, img=f"img/{pid}.svg",
                      q=q, ta=p["ta"], far=p["far"] or walk > 25, web=p["web"], drive=p["drive"], who=p["who"]))
# remove images of places that no longer exist
keep = {it["img"][4:] for it in items}
for f in os.listdir(os.path.join(OUT, "img")):
    if re.fullmatch(r"n\d+\.svg", f) and f not in keep: os.remove(os.path.join(OUT, "img", f))

# ---------- landmark artwork (cover, icon) ----------
def landmark(kind, stone):
    s = ""
    if kind == "cathedral":   # three-towered gothic cathedral on a hill
        s += f'<rect x="120" y="120" width="160" height="70" fill="{stone}"/>'
        s += f'<path d="M120 120 L200 92 L280 120Z" fill="{stone}"/>'
        for x, h in ((128, 120), (178, 150), (240, 120)):
            s += f'<rect x="{x}" y="{190-h}" width="32" height="{h}" fill="{stone}"/>'
            s += ''.join(f'<rect x="{x+3+i*8}" y="{182-h}" width="5" height="10" fill="{stone}"/>' for i in range(4))
            s += f'<rect x="{x+11}" y="{205-h}" width="10" height="26" rx="5" fill="#5A4A3A"/>'
        s += '<circle cx="200" cy="140" r="12" fill="#5A4A3A"/>'
    elif kind == "clocktower":  # Victorian clock tower
        s += f'<rect x="175" y="70" width="50" height="120" fill="{stone}"/><path d="M168 70 L200 30 L232 70Z" fill="#7FA79A"/>'
        s += '<circle cx="200" cy="95" r="15" fill="#fff"/><path d="M200 95 L200 85 M200 95 L208 99" stroke="#2B2D42" stroke-width="3"/>'
        s += f'<rect x="160" y="160" width="80" height="30" fill="{stone}"/>'
        s += ''.join(f'<rect x="{185+i*12}" y="{120}" width="6" height="30" rx="3" fill="#5A4A3A"/>' for i in range(3))
    elif kind == "townhall":    # columned town hall with clock tower and dome
        s += f'<rect x="100" y="120" width="200" height="70" fill="{stone}"/>'
        s += ''.join(f'<rect x="{110+i*22}" y="128" width="12" height="62" fill="#C9BFA8"/>' for i in range(9))
        s += f'<rect x="176" y="55" width="48" height="65" fill="{stone}"/><circle cx="200" cy="80" r="12" fill="#fff"/>'
        s += f'<path d="M176 55 Q200 15 224 55Z" fill="#7FA79A"/><rect x="198" y="8" width="4" height="16" fill="#FFD23F"/>'
    else:                       # steel city: hills, chimney and a glass winter garden
        s += f'<path d="M110 190 L110 140 Q200 70 290 140 L290 190Z" fill="#BFE3F0" stroke="#7FA79A" stroke-width="4"/>'
        s += ''.join(f'<path d="M{130+i*30} 190 L{130+i*30} {140-abs(i-2.5)*8:.0f}" stroke="#7FA79A" stroke-width="3"/>' for i in range(6))
        s += f'<rect x="300" y="70" width="18" height="120" fill="{stone}"/><rect x="296" y="66" width="26" height="8" fill="#555"/>'
        s += '<ellipse cx="315" cy="50" rx="22" ry="10" fill="#fff" opacity=".7"/>'
    return s

r = random.Random("cover" + CFG["slug"])
stone = CFG.get("stone", "#E6C38F")
cover = sky(r, "cv") + clouds(r)
cover += '<path d="M0 250 L0 170 Q90 140 200 165 Q300 185 400 150 L400 250Z" fill="#7CB342"/>'
cover += warehouse(10, 90, 60, "#B5523B", r, 200) + warehouse(310, 90, 70, "#A4442F", r, 205)
cover += landmark(CFG.get("landmark", "steel"), stone)
cover += '<rect y="200" width="400" height="50" fill="#8F9AA3"/>'
open(os.path.join(OUT, "img", "cover.svg"), "w").write(wrap(cover))
r = random.Random("train" + CFG["slug"])
train = sky(r, "tr") + clouds(r) + '<rect y="190" width="400" height="60" fill="#8F9AA3"/><rect y="196" width="400" height="4" fill="#555"/>'
train += f'<rect x="40" y="110" width="320" height="80" rx="18" fill="{CFG["theme"]}"/><rect x="40" y="165" width="320" height="10" fill="#FFD23F"/>'
train += ''.join(f'<rect x="{60+i*58}" y="122" width="44" height="34" rx="6" fill="#C2E9FB"/>' for i in range(5))
train += '<rect x="250" y="200" width="80" height="34" rx="6" fill="#1877D0"/><text x="290" y="223" font-family="Arial" font-weight="700" font-size="14" fill="#fff" text-anchor="middle">P</text>'
open(os.path.join(OUT, "img", "transit.svg"), "w").write(wrap(train))

used = []
for p in P:
    if p["cat"] not in used: used.append(p["cat"])
catdefs = {k: dict(v) for k, v in CATS.items() if k in used}
open(os.path.join(OUT, "data.js"), "w").write("window.GUIDE=" + json.dumps({"cats": catdefs, "items": items, "base": BASE}, ensure_ascii=False) + ";\n")

# ---------- index.html ----------
t = open(os.path.join(KIT, "template.html")).read()
info = open(os.path.join(BUILD, "info.js")).read()
# info.js must only reference places that exist
missing = sorted({m.replace("\\'", "'") for block in re.findall(r"refs\(\[(.*?)\]\)", info, re.S) for m in re.findall(r"'((?:[^'\\]|\\.)+)'", block)} - set(names))
if missing: raise SystemExit("info.js refers to unknown places: " + "; ".join(missing))
vals = {"SHORT": CFG["short"], "CITY": CFG["city"], "DESC": CFG["desc"], "THEME": CFG["theme"], "GRADIENT": CFG["gradient"],
        "TAGLINE": CFG["tagline"], "BASESHORT": BASE["short"], "BASE_THE": BASE["the"], "CENTER": ", ".join(map(str, CFG["center"])),
        "ZOOM": str(CFG.get("zoom", 15)), "BASEICON": BASE["icon"], "SLUG": CFG["slug"],
        "SPECIAL_ICON": CFG["special"]["icon"], "SPECIAL_TAB": CFG["special"]["tab"],
        "VIEWS": open(os.path.join(BUILD, "content.html")).read(), "INFOJS": info}
for k, v in vals.items(): t = t.replace("{{" + k + "}}", v)
assert "{{" not in t.replace("${", ""), re.findall(r"\{\{\w+\}\}", t)
open(os.path.join(OUT, "index.html"), "w").write(t)

# ---------- manifest, service worker, static files ----------
man = {"name": f'{CFG["short"]} Guide: Eat, Drink, Shops, Galleries & Days Out', "short_name": CFG["short"], "description": CFG["desc"],
       "id": "./", "start_url": "./#explore", "scope": "./", "display": "standalone", "orientation": "portrait",
       "background_color": "#F6F5F0", "theme_color": CFG["theme"],
       "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                 {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
       "shortcuts": [{"name": "Map", "url": "./#map"}, {"name": "Eat & Drink", "url": "./#eat"}, {"name": "My list", "url": "./#saved"}]}
open(os.path.join(OUT, "manifest.webmanifest"), "w").write(json.dumps(man, ensure_ascii=False, indent=2))
ver = CFG.get("version", 1)
imgs = sorted("img/" + f for f in os.listdir(os.path.join(OUT, "img")))
core = ["vendor/leaflet.js", "vendor/leaflet.css", "./", "index.html", "data.js", "manifest.webmanifest", "icon-192.png", "icon-512.png", "apple-touch-icon.png", "favicon.png"] + imgs
sw = open(os.path.join(KIT, "sw.template.js")).read().replace("{{V}}", f'{CFG["slug"]}-v{ver}').replace("{{TILES}}", f'{CFG["slug"]}-tiles').replace("{{CORE}}", json.dumps(core))
open(os.path.join(OUT, "sw.js"), "w").write(sw)
if not os.path.exists(os.path.join(OUT, "vendor")): shutil.copytree(os.path.join(KIT, "vendor"), os.path.join(OUT, "vendor"))
open(os.path.join(OUT, ".nojekyll"), "w").close()

# icon
a, b2 = CFG["icon_colors"]
icon = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b2}"/></linearGradient></defs><rect width="512" height="512" fill="url(#g)"/>'
        + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="#fff" opacity=".12"/>' for x in range(0, 520, 48) for y in range(0, 520, 48))
        + f'<g transform="translate(-184,6) scale(2.2)">{landmark(CFG.get("landmark","steel"), "#F3ECDD")}</g></svg>')
open(os.path.join(BUILD, "icon.svg"), "w").write(icon)
if True:
    subprocess.run(["node", os.path.join(KIT, "render_icons.js"), os.path.join(BUILD, "icon.svg"), OUT], check=True)

print(len(items), "places in", len(catdefs), "categories;", sum(1 for i in items if i["far"]), "outside the centre")
