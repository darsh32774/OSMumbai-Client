# OSMumbai — AI Map Interface

> Query OpenStreetMap data for the Mumbai region using plain English.

![MapLibre GL JS](https://img.shields.io/badge/MapLibre_GL_JS-4.7.1-green.svg)
![MapTiler](https://img.shields.io/badge/tiles-MapTiler-orange.svg)
![Hosted on Netlify](https://img.shields.io/badge/hosted_on-Netlify-00C7B7.svg)

**🌐 Live at [osmumbai.netlify.app](https://osmumbai.netlify.app)**

---

## What is this?

OSMumbai is a natural language interface for exploring OpenStreetMap data across the Mumbai metropolitan region. Type a question in plain English — the app translates it into a PostGIS SQL query, runs it against a database of Mumbai OSM data, and plots the results on an interactive WebGL map in real time.

No SQL knowledge required.

---

## Example Queries

- `hospitals in Dharavi`
- `cafes near Bandra station`
- `ATMs in Andheri West`
- `parks in Powai`
- `pharmacies in Thane`

---

## How It Works

```
User types a query
        ↓
Backend (Gemini API) translates it to SQL
        ↓
SQL runs on a PostGIS database of Mumbai OSM data
        ↓
GeoJSON results returned to the frontend
        ↓
MapLibre GL JS renders features on a WebGL map
```

Results are also shown in a table below the search panel. Clicking any row highlights and flies the camera to that feature on the map.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Map rendering | [MapLibre GL JS 4.7.1](https://maplibre.org/) |
| Map tiles | [MapTiler Streets v2](https://www.maptiler.com/) |
| Frontend | HTML / Tailwind CSS / Vanilla JS |
| Backend | FastAPI hosted on [Vercel](https://vercel.com/) |
| NL → SQL | Google Gemini API |
| Database | Supabase + PostGIS |
| Hosting | [Netlify](https://www.netlify.com/) |

---

## Features

- **Natural language search** — no SQL knowledge required
- **WebGL map rendering** — smooth performance even with large result sets
- **Light & dark map themes** — toggle between MapTiler's Streets and Streets Dark styles
- **SQL inspector** — expand the panel to see the exact query the AI generated
- **Clickable results table** — click any row to zoom to and highlight that feature
- **Fully responsive** — desktop, tablet, and mobile including iOS safe areas

---

## Feature Rendering

Results are rendered as GPU-accelerated layers based on geometry type:

| Geometry | Rendering | Color |
|---|---|---|
| Point / MultiPoint | Circle layer | Blue |
| LineString / MultiLineString | Line layer | Amber |
| Polygon / MultiPolygon | Fill + outline layer | Purple |

Selected features are highlighted in red using MapLibre's `feature-state` API.

---

## Known Limitations

- **Mumbai only** — the database covers the Mumbai metropolitan region. Queries for other cities return no results.
- **Cold start delay** — the backend runs on Vercel's free tier and sleeps after inactivity. The first query after a period of no use can take up to 20 seconds. The UI shows a warm-up indicator while waiting.
- **AI accuracy** — NL→SQL conversion may occasionally misinterpret ambiguous queries. The generated SQL is always visible in the UI so results can be verified.
- **500 row cap** — results are limited to 500 features per query to keep rendering fast.

---

## Acknowledgements

- [OpenStreetMap contributors](https://www.openstreetmap.org/copyright) for the underlying map data
- [MapLibre GL JS](https://maplibre.org/) for the open-source WebGL renderer
- [MapTiler](https://www.maptiler.com/) for the map tile styles
- [Supabase](https://supabase.com/) for the hosted PostGIS database
