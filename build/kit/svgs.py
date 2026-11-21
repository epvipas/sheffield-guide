import random

# ---------------- illustrations ----------------
PAL = {
 "sky": [("#8EC5FC", "#E0C3FC"), ("#A1C4FD", "#C2E9FB"), ("#FBC2EB", "#A6C1EE"), ("#FFD3A5", "#FD6585"), ("#84FAB0", "#8FD3F4")],
 "brick": ["#B5523B", "#A4442F", "#C2614A", "#9A3E2B", "#B9583F"],
 "stone": ["#D9B07A", "#E2BE88", "#CFA46C", "#E6C38F"],
 "pop": ["#E8483B", "#E8930C", "#FFD23F", "#2EC4B6", "#1877D0", "#8E44C9", "#E5007E", "#24563F"],
}
def sky(r, gid):
    a, b = r.choice(PAL["sky"])
    return f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs><rect width="400" height="250" fill="url(#{gid})"/>'
def warehouse(x, w, h, col, r, ground=200):
    s = f'<rect x="{x}" y="{ground-h}" width="{w}" height="{h}" fill="{col}"/>'
    s += f'<rect x="{x-4}" y="{ground-h-6}" width="{w+8}" height="8" fill="#00000030"/>'
    cols = max(2, w // 22)
    for i in range(cols):
        for j in range(max(1, (h-20)//30)):
            wx = x + 8 + i*(w-16)/cols; wy = ground - h + 14 + j*30
            s += f'<rect x="{wx:.0f}" y="{wy}" width="{(w-16)/cols-7:.0f}" height="18" rx="7" fill="#FFF3D6" opacity=".85"/>'
    return s
def clouds(r):
    return ''.join(f'<ellipse cx="{r.randint(30,370)}" cy="{r.randint(20,60)}" rx="{r.randint(18,34)}" ry="{r.randint(6,10)}" fill="#fff" opacity=".8"/>' for _ in range(r.randint(1,3)))

def svg_sights(r, gid):
    s = sky(r, gid) + clouds(r)
    stone = r.choice(PAL["stone"])
    s += f'<path d="M0 250 L0 150 Q60 120 130 135 Q200 150 260 125 Q330 100 400 130 L400 250Z" fill="{stone}"/>'
    for _ in range(r.randint(2,4)):
        cx = r.randint(30, 370); cy = r.randint(175, 215)
        s += f'<path d="M{cx-16} {cy+20} L{cx-16} {cy} Q{cx} {cy-22} {cx+16} {cy} L{cx+16} {cy+20}Z" fill="#5A3A22" opacity=".75"/>'
    x = r.randint(60, 220); col = r.choice(PAL["brick"]); w = r.randint(90, 140); h = r.randint(55, 80); top = 150 - h - 6
    if r.random() < .5:
        m = x + w/2
        s += f'<path d="M{m-36} {top} Q{m} {top-60} {m+36} {top}Z" fill="#7FA79A"/><rect x="{m-3}" y="{top-62}" width="6" height="16" fill="#FFD23F"/>'
    s += warehouse(x, w, h, col, r, ground=150)
    s += f'<rect x="0" y="236" width="400" height="14" fill="#00000018"/>'
    return s
def svg_galleries(r, gid):
    wall = r.choice(["#F4EFE6", "#EDE7F6", "#E8F1EE", "#FBEDE7"])
    s = f'<rect width="400" height="250" fill="{wall}"/><rect y="200" width="400" height="50" fill="#B98A5E"/><rect y="200" width="400" height="5" fill="#00000020"/>'
    x = 30
    while x < 360:
        w = r.randint(60, 110); h = r.randint(60, 120); y = r.randint(40, 190 - h)
        s += f'<rect x="{x-5}" y="{y-5}" width="{w+10}" height="{h+10}" fill="#2B2D42"/><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff"/>'
        for _ in range(3):
            c = r.choice(PAL["pop"]); kind = r.random()
            if kind < .4: s += f'<circle cx="{x+r.randint(10,w-10)}" cy="{y+r.randint(10,h-10)}" r="{r.randint(6,min(w,h)//3)}" fill="{c}" opacity=".85"/>'
            elif kind < .75: s += f'<rect x="{x+r.randint(4,w//2)}" y="{y+r.randint(4,h//2)}" width="{r.randint(10,w//2)}" height="{r.randint(10,h//2)}" fill="{c}" opacity=".85"/>'
            else: s += f'<path d="M{x+4} {y+h-6} Q{x+w/2} {y+r.randint(5,h)} {x+w-4} {y+8}" stroke="{c}" stroke-width="5" fill="none"/>'
        x += w + r.randint(25, 45)
    s += '<ellipse cx="200" cy="0" rx="160" ry="26" fill="#FFF8D0" opacity=".5"/>'
    return s
def svg_shops(r, gid):
    s = sky(r, gid) + clouds(r)
    x = 10
    while x < 400:
        w = r.randint(110, 150); col = r.choice(PAL["brick"]); aw = r.choice(PAL["pop"])
        s += f'<rect x="{x}" y="60" width="{w}" height="170" fill="{col}"/>'
        s += ''.join(f'<rect x="{x+12+i*(w-24)/3:.0f}" y="76" width="{(w-24)/3-8:.0f}" height="30" rx="10" fill="#FFF3D6" opacity=".85"/>' for i in range(3))
        s += f'<rect x="{x+8}" y="140" width="{w-16}" height="80" fill="#BFE3F0"/><rect x="{x+8}" y="140" width="{w-16}" height="80" fill="none" stroke="#2B2D42" stroke-width="4"/>'
        stripes = ''.join(f'<rect x="{x+4+i*(w-8)/6:.0f}" y="118" width="{(w-8)/12:.0f}" height="22" fill="#fff" opacity=".7"/>' for i in range(6))
        s += f'<rect x="{x+4}" y="118" width="{w-8}" height="22" fill="{aw}"/>' + stripes
        for _ in range(3):
            s += f'<rect x="{x+16+r.randint(0,w-50)}" y="{r.randint(170,195)}" width="{r.randint(12,24)}" height="{r.randint(14,24)}" rx="3" fill="{r.choice(PAL["pop"])}"/>'
        x += w + 8
    s += '<rect y="228" width="400" height="22" fill="#9AA0A6"/>'
    return s
def svg_records(r, gid):
    bg = r.choice(["#FFE29A", "#C2E9FB", "#FBC2EB", "#D4F5E0"])
    s = f'<rect width="400" height="250" fill="{bg}"/><rect y="190" width="400" height="60" fill="#8D6346"/>'
    for i in range(r.randint(2, 3)):
        cx = 80 + i*95 + r.randint(-10, 10); cy = 120 + r.randint(-15, 10); c = r.choice(PAL["pop"])
        s += f'<circle cx="{cx}" cy="{cy}" r="58" fill="#1C1C1C"/>' + ''.join(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="#333" stroke-width="1.5"/>' for rr in (48, 40, 32))
        s += f'<circle cx="{cx}" cy="{cy}" r="18" fill="{c}"/><circle cx="{cx}" cy="{cy}" r="3" fill="#fff"/>'
    bx = r.randint(280, 320); y = 190
    for _ in range(4):
        h = r.randint(12, 18); w = r.randint(70, 90)
        s += f'<rect x="{bx}" y="{y-h}" width="{w}" height="{h}" rx="2" fill="{r.choice(PAL["pop"])}"/>'; y -= h
    return s
def svg_vintage(r, gid):
    bg = r.choice(["#F7E1C4", "#E3F0E8", "#F3DDE6", "#E4E9F7"])
    s = f'<rect width="400" height="250" fill="{bg}"/><rect y="210" width="400" height="40" fill="#A47551"/>'
    s += '<rect x="40" y="50" width="320" height="6" rx="3" fill="#555"/><rect x="40" y="50" width="6" height="160" fill="#555"/><rect x="354" y="50" width="6" height="160" fill="#555"/>'
    x = 60
    while x < 330:
        c = r.choice(PAL["pop"] + PAL["brick"]); w = r.randint(28, 42); h = r.randint(80, 130)
        s += f'<path d="M{x+w/2} 56 l0 10" stroke="#555" stroke-width="3"/><path d="M{x} 76 L{x+w/2} 66 L{x+w} 76 L{x+w-3} {76+h} L{x+3} {76+h}Z" fill="{c}"/>'
        x += w + r.randint(2, 8)
    return s
def svg_food(r, gid, kind):
    bg = r.choice(["#FFF3B0", "#FDE3DF", "#DDEBFA", "#D8F3EE", "#EFE2F8"])
    s = f'<rect width="400" height="250" fill="{bg}"/><rect y="175" width="400" height="75" fill="{r.choice(["#8D6346","#A0522D","#6F4E37"])}"/><rect y="175" width="400" height="6" fill="#00000022"/>'
    cx = r.randint(150, 250)
    if kind == "cafes":
        s += f'<ellipse cx="{cx}" cy="185" rx="80" ry="14" fill="#fff"/><path d="M{cx-50} 110 L{cx+50} 110 L{cx+40} 180 L{cx-40} 180Z" fill="{r.choice(PAL["pop"])}"/>'
        s += f'<path d="M{cx+48} 125 q30 5 0 35" stroke="{r.choice(PAL["pop"])}" stroke-width="9" fill="none"/><ellipse cx="{cx}" cy="112" rx="48" ry="9" fill="#6F4E37"/>'
        s += ''.join(f'<path d="M{cx-20+i*20} 95 q-8 -15 0 -30 q8 -15 0 -30" stroke="#fff" stroke-width="4" fill="none" opacity=".8"/>' for i in range(3))
        s += f'<circle cx="{cx+130}" cy="170" r="22" fill="#E9A25B"/><circle cx="{cx+130}" cy="170" r="8" fill="{bg}"/>'
    elif kind == "cheap":
        s += f'<ellipse cx="{cx}" cy="183" rx="110" ry="16" fill="#E8483B"/><path d="M{cx-70} 150 Q{cx} 70 {cx+70} 150Z" fill="#E9A25B"/>'
        s += f'<rect x="{cx-75}" y="148" width="150" height="10" rx="5" fill="#7CB342"/><rect x="{cx-72}" y="156" width="144" height="14" rx="6" fill="#6B3E26"/><rect x="{cx-70}" y="168" width="140" height="12" rx="6" fill="#E9A25B"/>'
        s += ''.join(f'<ellipse cx="{cx-40+i*25}" cy="{110+abs(i-1.5)*6:.0f}" rx="3" ry="2" fill="#FFF3D6"/>' for i in range(4))
    else:
        s += f'<ellipse cx="{cx}" cy="180" rx="95" ry="22" fill="#fff"/><ellipse cx="{cx}" cy="178" rx="70" ry="15" fill="#F3EFE7"/>'
        for _ in range(4):
            s += f'<circle cx="{cx+r.randint(-40,40)}" cy="{r.randint(168,180)}" r="{r.randint(6,13)}" fill="{r.choice(["#7CB342","#E8483B","#E8930C","#8D6346","#FFD23F"])}"/>'
        gx = cx + 130 if cx < 200 else cx - 130
        s += f'<path d="M{gx-18} 100 Q{gx} 150 {gx+18} 100Z" fill="#8E1C2B" opacity=".9"/><rect x="{gx-2}" y="125" width="4" height="45" fill="#ddd"/><ellipse cx="{gx}" cy="172" rx="16" ry="4" fill="#ddd"/>'
        if kind == "splurge":
            s += ''.join(f'<path d="M{x} 40 l6 14 15 1 -12 10 4 15 -13 -8 -13 8 4 -15 -12 -10 15 -1z" fill="#FFD23F"/>' for x in (cx-30, cx+10)[:1 + (r.random() < .5)])
    return s
def svg_pubs(r, gid):
    stone = r.choice(PAL["stone"])
    s = f'<rect width="400" height="250" fill="{stone}"/>'
    s += ''.join(f'<path d="M0 {y} Q100 {y+r.randint(-8,8)} 200 {y} T400 {y}" stroke="#00000018" stroke-width="3" fill="none"/>' for y in range(20, 160, 26))
    s += '<path d="M90 250 L90 120 Q200 20 310 120 L310 250Z" fill="#4A2E1A"/><path d="M110 250 L110 128 Q200 50 290 128 L290 250Z" fill="#6B4226"/>'
    s += f'<circle cx="200" cy="105" r="14" fill="#FFD23F" opacity=".9"/><circle cx="200" cy="105" r="30" fill="#FFD23F" opacity=".2"/>'
    s += '<rect y="200" width="400" height="50" fill="#5A3A22"/>'
    cx = r.randint(150, 250)
    s += f'<path d="M{cx-26} 120 L{cx+26} 120 L{cx+20} 200 L{cx-20} 200Z" fill="{r.choice(["#C77A1A","#8B3A0F","#D99A2B","#3B1F10"])}" opacity=".95"/>'
    s += f'<path d="M{cx-27} 112 Q{cx} 100 {cx+27} 112 L{cx+26} 124 L{cx-26} 124Z" fill="#FFF8E7"/><path d="M{cx-26} 120 L{cx+26} 120 L{cx+20} 200 L{cx-20} 200Z" fill="none" stroke="#fff" stroke-width="3" opacity=".6"/>'
    return s
def svg_bars(r, gid):
    bg = r.choice(["#1E1B3A", "#14213D", "#2B1B2E", "#10302A"])
    s = f'<rect width="400" height="250" fill="{bg}"/>'
    s += ''.join(f'<circle cx="{r.randint(10,390)}" cy="{r.randint(10,140)}" r="{r.choice([1,1.5,2])}" fill="#fff" opacity=".6"/>' for _ in range(18))
    neon = r.choice(["#FF4FA3", "#2EC4B6", "#FFD23F", "#9D7BFF"])
    s += f'<rect x="40" y="30" width="120" height="44" rx="22" fill="none" stroke="{neon}" stroke-width="5"/><rect x="40" y="30" width="120" height="44" rx="22" fill="none" stroke="{neon}" stroke-width="14" opacity=".2"/>'
    s += '<rect y="190" width="400" height="60" fill="#3B2A20"/><rect y="190" width="400" height="6" fill="#00000040"/>'
    cx = r.randint(190, 300); c = r.choice(PAL["pop"])
    s += f'<path d="M{cx-45} 90 L{cx+45} 90 L{cx} 140Z" fill="{c}" opacity=".9"/><path d="M{cx-45} 90 L{cx+45} 90 L{cx} 140Z" fill="none" stroke="#fff" stroke-width="3"/>'
    s += f'<rect x="{cx-2}" y="140" width="4" height="40" fill="#fff"/><ellipse cx="{cx}" cy="182" rx="22" ry="5" fill="#fff"/><circle cx="{cx+28}" cy="88" r="9" fill="#7CB342"/>'
    return s

def svg_gear(r, gid):
    bg = r.choice(["#DDEBFA", "#E3F0E8", "#F3DDE6", "#FFF3B0"])
    s = f'<rect width="400" height="250" fill="{bg}"/><rect y="185" width="400" height="65" fill="#5B6770"/><rect y="185" width="400" height="6" fill="#00000030"/>'
    k = r.random()
    # camera
    s += '<rect x="40" y="105" width="130" height="80" rx="12" fill="#2B2D42"/><rect x="60" y="92" width="40" height="16" rx="4" fill="#2B2D42"/>'
    s += '<circle cx="105" cy="145" r="30" fill="#555"/><circle cx="105" cy="145" r="20" fill="#1877D0"/><circle cx="98" cy="138" r="6" fill="#fff" opacity=".7"/>'
    # lens
    s += '<rect x="185" y="140" width="50" height="45" rx="6" fill="#333"/><rect x="185" y="150" width="50" height="6" fill="#E8483B"/>'
    # guitar
    c = r.choice(PAL["pop"])
    s += f'<rect x="318" y="30" width="10" height="100" fill="#6B4226"/><rect x="312" y="20" width="22" height="22" rx="4" fill="#3B1F10"/>'
    s += f'<ellipse cx="323" cy="150" rx="34" ry="30" fill="{c}"/><ellipse cx="323" cy="120" rx="24" ry="22" fill="{c}"/><circle cx="323" cy="140" r="9" fill="#2B2D42"/>'
    # phone
    s += '<rect x="252" y="120" width="34" height="62" rx="6" fill="#111"/><rect x="256" y="126" width="26" height="48" rx="3" fill="#2EC4B6"/>'
    return s
def svg_food_shop(r, gid):
    bg = r.choice(["#FFF3B0", "#FDE3DF", "#D8F3EE", "#EFE2F8"])
    s = f'<rect width="400" height="250" fill="{bg}"/>'
    for y in (70, 140):
        s += f'<rect x="20" y="{y}" width="360" height="8" fill="#8D6346"/>'
        x = 30
        while x < 360:
            c = r.choice(PAL["pop"]); w = r.randint(24, 40); h = r.randint(28, 55)
            if r.random() < .5: s += f'<rect x="{x}" y="{y-h}" width="{w}" height="{h}" rx="4" fill="{c}"/><rect x="{x}" y="{y-h+8}" width="{w}" height="10" fill="#fff" opacity=".6"/>'
            else: s += f'<rect x="{x+w/2-5}" y="{y-h}" width="10" height="10" fill="{c}"/><rect x="{x}" y="{y-h+8}" width="{w}" height="{h-8}" rx="8" fill="{c}" opacity=".85"/>'
            x += w + r.randint(4, 10)
    s += '<rect y="185" width="400" height="65" fill="#A0522D"/>'
    cx = r.randint(110, 290)
    s += f'<path d="M{cx-70} 215 L{cx+70} 215 L{cx+40} 175 L{cx-40} 175Z" fill="#FFD23F"/><path d="M{cx-70} 215 L{cx-40} 175 L{cx-40} 200Z" fill="#E9B500"/>'
    s += ''.join(f'<circle cx="{cx+r.randint(-30,40)}" cy="{r.randint(182,208)}" r="{r.randint(3,6)}" fill="#E9B500"/>' for _ in range(5))
    return s
def svg_fun(r, gid):
    bg = r.choice(["#2B1B2E", "#14213D", "#10302A"])
    s = f'<rect width="400" height="250" fill="{bg}"/>'
    s += '<path d="M120 250 L120 120 Q200 30 280 120 L280 250Z" fill="#D9B07A" opacity=".25"/>'
    c = r.choice(["#FFD23F", "#FF4FA3", "#2EC4B6"])
    # padlock
    s += f'<path d="M170 110 L170 85 Q200 45 230 85 L230 110" stroke="{c}" stroke-width="12" fill="none"/><rect x="150" y="105" width="100" height="85" rx="12" fill="{c}"/>'
    s += f'<circle cx="200" cy="140" r="11" fill="{bg}"/><rect x="195" y="145" width="10" height="24" fill="{bg}"/>'
    # dice and puzzle pieces
    s += '<rect x="290" y="160" width="46" height="46" rx="8" fill="#fff" transform="rotate(12 313 183)"/>'
    s += ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#2B2D42"/>' for x, y in [(303,172),(322,192),(313,182)])
    s += f'<path d="M50 170 h30 a8 8 0 1 1 14 0 h22 v30 a8 8 0 1 0 0 14 v20 h-66z" fill="{r.choice(PAL["pop"])}"/>'
    s += ''.join(f'<circle cx="{r.randint(10,390)}" cy="{r.randint(10,90)}" r="1.5" fill="#fff" opacity=".6"/>' for _ in range(14))
    return s

def svg_music(r, gid):
    bg = r.choice(["#1E1B3A", "#2B1B2E", "#14213D"])
    s = f'<rect width="400" height="250" fill="{bg}"/>'
    for x in (90, 200, 310):
        c = r.choice(["#FF4FA3", "#FFD23F", "#2EC4B6", "#9D7BFF"])
        s += f'<path d="M{x} 0 L{x-60} 190 L{x+60} 190Z" fill="{c}" opacity=".18"/><rect x="{x-10}" y="0" width="20" height="14" fill="#555"/>'
    s += '<rect y="190" width="400" height="60" fill="#3B2A20"/><rect y="186" width="400" height="6" fill="#111"/>'
    s += '<rect x="196" y="110" width="6" height="80" fill="#888"/><ellipse cx="199" cy="106" rx="9" ry="13" fill="#333"/>'
    c = r.choice(PAL["pop"])
    s += f'<rect x="250" y="120" width="12" height="70" fill="#6B4226" transform="rotate(25 256 155)"/><ellipse cx="236" cy="178" rx="26" ry="20" fill="{c}"/>'
    s += '<rect x="90" y="150" width="60" height="40" rx="4" fill="#222"/><circle cx="120" cy="170" r="13" fill="#444"/>'
    s += ''.join(f'<text x="{r.randint(20,380)}" y="{r.randint(40,140)}" font-size="{r.randint(18,28)}" fill="#fff" opacity=".7" font-family="Arial">♪</text>' for _ in range(4))
    return s
def svg_parks(r, gid):
    s = sky(r, gid) + clouds(r)
    s += f'<path d="M0 250 L0 150 Q100 120 200 145 T400 140 L400 250Z" fill="{r.choice(["#7CB342","#8BC34A","#689F38"])}"/>'
    if r.random() < .6:
        s += '<path d="M0 205 Q120 185 220 200 T400 195 L400 230 Q260 220 160 232 T0 235Z" fill="#4FC3F7" opacity=".85"/>'
    s += '<path d="M150 250 Q190 200 230 170 Q250 160 270 160" stroke="#E6C38F" stroke-width="16" fill="none"/>'
    for _ in range(r.randint(4, 7)):
        x = r.randint(10, 390); y = r.randint(135, 185); h = r.randint(30, 60); c = r.choice(["#2E7D32", "#388E3C", "#1B5E20", "#558B2F"])
        s += f'<rect x="{x-3}" y="{y}" width="6" height="{h//2}" fill="#6B4226"/><circle cx="{x}" cy="{y}" r="{h//2.2:.0f}" fill="{c}"/>'
    return s
def svg_trips(r, gid):
    s = sky(r, gid) + clouds(r)
    s += '<path d="M0 170 Q80 120 170 150 T340 130 T400 140 L400 250 L0 250Z" fill="#9CCC65"/><path d="M0 200 Q120 170 240 195 T400 185 L400 250 L0 250Z" fill="#7CB342"/>'
    x = r.randint(110, 230); stone = r.choice(PAL["stone"])
    s += f'<rect x="{x}" y="110" width="120" height="70" fill="{stone}"/>'
    s += ''.join(f'<rect x="{x+i*24}" y="100" width="12" height="12" fill="{stone}"/>' for i in range(6))
    s += f'<rect x="{x-20}" y="85" width="30" height="95" fill="{stone}"/><rect x="{x+110}" y="85" width="30" height="95" fill="{stone}"/>'
    s += ''.join(f'<rect x="{x+12+i*26}" y="128" width="12" height="22" rx="6" fill="#5A4A3A"/>' for i in range(4))
    s += f'<rect x="{x+50}" y="150" width="20" height="30" rx="10" fill="#5A4A3A"/>'
    s += '<path d="M330 250 Q300 215 280 195" stroke="#E6C38F" stroke-width="10" fill="none"/>'
    for _ in range(3):
        tx = r.choice([r.randint(10, x-40), r.randint(x+160, 390)]) if x > 60 else r.randint(300, 390); ty = r.randint(160, 190)
        s += f'<rect x="{tx-3}" y="{ty}" width="6" height="22" fill="#6B4226"/><circle cx="{tx}" cy="{ty}" r="20" fill="#2E7D32"/>'
    return s

def svg_fashion(r, gid):
    bg = r.choice(["#FDE0F0", "#EDE7F6", "#E3F0E8", "#FFF3B0"])
    s = f'<rect width="400" height="250" fill="{bg}"/><rect y="210" width="400" height="40" fill="#C9A27A"/>'
    for cx in (120, 280):
        c = r.choice(PAL["pop"])
        s += f'<circle cx="{cx}" cy="45" r="16" fill="#E9C9A8"/><rect x="{cx-3}" y="60" width="6" height="12" fill="#E9C9A8"/>'
        s += f'<path d="M{cx-34} 75 Q{cx} 66 {cx+34} 75 L{cx+28} 125 L{cx+42} 200 L{cx-42} 200 L{cx-28} 125Z" fill="{c}"/>'
        s += f'<rect x="{cx-2}" y="200" width="4" height="10" fill="#555"/>'
    s += f'<rect x="185" y="150" width="30" height="24" rx="4" fill="{r.choice(PAL["pop"])}"/><path d="M190 150 q10 -16 20 0" stroke="#333" stroke-width="3" fill="none"/>'
    return s
def svg_charity(r, gid):
    s = sky(r, gid) + clouds(r)
    col = r.choice(PAL["brick"])
    s += f'<rect x="40" y="50" width="320" height="180" fill="{col}"/><rect x="60" y="62" width="280" height="36" rx="6" fill="#15803D"/>'
    s += '<path d="M200 70 c-8 -10 -22 -2 -14 10 l14 12 14 -12 c8 -12 -6 -20 -14 -10z" fill="#fff"/>'
    s += '<rect x="60" y="112" width="190" height="108" fill="#BFE3F0" stroke="#2B2D42" stroke-width="4"/><rect x="270" y="112" width="70" height="108" fill="#5A3A22"/>'
    s += '<rect x="80" y="180" width="70" height="30" rx="4" fill="#8D6346"/><rect x="88" y="170" width="54" height="14" rx="4" fill="#A0522D"/>'
    s += f'<circle cx="200" cy="170" r="22" fill="#1C1C1C"/><circle cx="200" cy="170" r="7" fill="{r.choice(PAL["pop"])}"/>'
    s += f'<rect x="160" y="125" width="22" height="34" rx="3" fill="{r.choice(PAL["pop"])}"/>'
    s += '<rect y="230" width="400" height="20" fill="#9AA0A6"/>'
    return s

def svg_museums(r, gid):
    s = sky(r, gid) + clouds(r)
    stone = r.choice(["#EFE6D2", "#E2D6BC", "#D8CCB0"])
    s += f'<path d="M80 95 L200 45 L320 95Z" fill="{stone}"/><rect x="80" y="95" width="240" height="12" fill="#C9BFA8"/>'
    s += ''.join(f'<rect x="{96+i*44}" y="107" width="18" height="88" fill="{stone}"/>' for i in range(6))
    s += f'<rect x="70" y="195" width="260" height="14" fill="#C9BFA8"/><rect x="60" y="209" width="280" height="14" fill="#B9AE96"/>'
    s += f'<rect y="223" width="400" height="27" fill="{r.choice(["#7CB342","#9AA0A6"])}"/>'
    return s
def svg_sport(r, gid):
    s = sky(r, gid)
    s += '<path d="M0 120 Q200 60 400 120 L400 150 L0 150Z" fill="#B0BEC5"/>'
    s += ''.join(f'<rect x="{i*20}" y="{110 - abs(200 - i*20)//12}" width="14" height="6" fill="{r.choice(PAL["pop"])}" opacity=".8"/>' for i in range(20))
    s += '<rect y="150" width="400" height="100" fill="#4CAF50"/>' + ''.join(f'<rect x="{i*50}" y="150" width="25" height="100" fill="#66BB6A"/>' for i in range(8))
    s += '<rect x="185" y="175" width="30" height="60" fill="#D7CCC8"/><g stroke="#fff" stroke-width="3"><line x1="192" y1="172" x2="192" y2="186"/><line x1="200" y1="172" x2="200" y2="186"/><line x1="208" y1="172" x2="208" y2="186"/></g>'
    s += f'<circle cx="{r.randint(80,140)}" cy="{r.randint(170,210)}" r="9" fill="#C62828"/>'
    return s
def svg_markets(r, gid):
    s = sky(r, gid) + clouds(r)
    s += '<rect y="200" width="400" height="50" fill="#9AA0A6"/>'
    for i in range(3):
        x = 20 + i*130; c = r.choice(PAL["pop"])
        s += f'<rect x="{x}" y="130" width="110" height="70" fill="#8D6346"/>'
        s += ''.join(f'<rect x="{x+j*22}" y="100" width="11" height="30" fill="{c}"/><rect x="{x+11+j*22}" y="100" width="11" height="30" fill="#fff"/>' for j in range(5))
        s += ''.join(f'<circle cx="{x+15+k*20}" cy="{125}" r="8" fill="{r.choice(["#E8483B","#FFD23F","#7CB342","#E8930C"])}"/>' for k in range(5))
        s += f'<rect x="{x}" y="96" width="110" height="6" fill="#5A3A22"/><rect x="{x}" y="96" width="4" height="104" fill="#5A3A22"/><rect x="{x+106}" y="96" width="4" height="104" fill="#5A3A22"/>'
    return s

GEN = {"sights": svg_sights, "galleries": svg_galleries, "shops": svg_shops, "records": svg_records, "vintage": svg_vintage,
       "cafes": lambda r, g: svg_food(r, g, "cafes"), "cheap": lambda r, g: svg_food(r, g, "cheap"),
       "mid": lambda r, g: svg_food(r, g, "mid"), "splurge": lambda r, g: svg_food(r, g, "splurge"),
       "pubs": svg_pubs, "bars": svg_bars, "gear": svg_gear, "food": svg_food_shop, "fun": svg_fun, "music": svg_music, "parks": svg_parks, "trips": svg_trips, "fashion": svg_fashion, "charity": svg_charity, "museums": svg_museums, "sport": svg_sport, "markets": svg_markets}
def wrap(body, vb="0 0 400 250"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">{body}</svg>'
