# Sheffield Guide

A mobile web app (PWA) for independent Sheffield: places to eat and drink, real-ale pubs, Kelham Island, record shops, cameras, antiques, museums, parks and Peak District day trips. Every place has links to Google reviews, TripAdvisor, its own website where it has one, and walking directions in Apple Maps or Google Maps, plus a built-in map.

It's a plain static site with no build step needed to host it. To change the content, edit `build/places.py`, `build/content.html` or `build/info.js`, then run `python3 build/kit/make.py`.
