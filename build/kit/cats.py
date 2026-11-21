# Shared category definitions for all city guides
CATS = {
 "sights":   {"sec":"see","title":"Sights & oddities","emoji":"🏰","color":"#C0392B"},
 "galleries":{"sec":"see","title":"Galleries","emoji":"🎨","color":"#8E44C9"},
 "shops":    {"sec":"see","title":"Indie shops & makers","emoji":"🛍️","color":"#E8930C"},
 "records":  {"sec":"see","title":"Records, books & comics","emoji":"📀","color":"#1877D0"},
 "vintage":  {"sec":"see","title":"Vintage & antiques","emoji":"🧥","color":"#0F766E"},
 "gear":     {"sec":"see","title":"Cameras, music & tech","emoji":"📷","color":"#0E7490"},
 "food":     {"sec":"see","title":"Food shops & world grocers","emoji":"🧀","color":"#B45309"},
 "fun":      {"sec":"see","title":"Escape rooms & things to do","emoji":"🧩","color":"#DB2777"},
 "museums":  {"sec":"see","title":"Museums","emoji":"🏛️","color":"#7C2D12"},
 "sport":    {"sec":"see","title":"Sport","emoji":"🏏","color":"#166534"},
 "markets":  {"sec":"see","title":"Markets","emoji":"🧺","color":"#A16207"},
 "fashion":  {"sec":"see","title":"Clothes & boutiques","emoji":"👗","color":"#9D174D"},
 "charity":  {"sec":"see","title":"Charity shops","emoji":"♻️","color":"#15803D"},
 "parks":    {"sec":"see","title":"Parks & walks","emoji":"🌳","color":"#2F855A"},
 "trips":    {"sec":"see","title":"Day trips","emoji":"🚗","color":"#1D4ED8"},
 "cafes":    {"sec":"eat","title":"Cafés & coffee","emoji":"☕","color":"#0F9D8A"},
 "cheap":    {"sec":"eat","title":"Cheap eats & street food","emoji":"🌮","color":"#E8483B"},
 "mid":      {"sec":"eat","title":"Mid-range","emoji":"🍽️","color":"#E8930C"},
 "splurge":  {"sec":"eat","title":"Splurge & Michelin","emoji":"⭐","color":"#8E44C9"},
 "pubs":     {"sec":"eat","title":"Historic & real-ale pubs","emoji":"🍺","color":"#A0522D"},
 "bars":     {"sec":"eat","title":"Cocktails & craft bars","emoji":"🍸","color":"#1877D0"},
 "music":    {"sec":"eat","title":"Live music & comedy","emoji":"🎸","color":"#7C3AED"},
}

P = []
CITY = ""
def add(cat, name, addr, text, tip, price=0, web="", ta=True, far=False, geo=None, ll=None, drive="", who=None):
    assert cat in CATS, cat
    P.append(dict(cat=cat, name=name, addr=addr, text=text, tip=tip, price=price, web=web, ta=ta, far=far, drive=drive, who=who or [],
                  geo=geo or f"{name}, {CITY}", ll=ll))
