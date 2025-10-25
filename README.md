# 🗺️ OSMumbai Client: Natural Language to Map CLI

The **OSMumbai Client** is a command-line interface (CLI) for interacting with the [OSMumbai API](https://osmumbai.onrender.com) — an **Agentic AI system** that converts **natural language queries** into **PostGIS SQL** commands to fetch real-time spatial data from **Mumbai’s OpenStreetMap dataset**.

Powered by **Google Gemini AI**, the system autonomously interprets user queries like *"cafes in Bandra"* or *"fire stations in South Mumbai"*, executes them on a geospatial database, and returns both **data tables** and **interactive maps**.

---

## 🚀 Features

- **🤖 Agentic AI Backend Integration**  
  Connects directly to the live OSMumbai backend (`https://osmumbai.onrender.com`) which uses Gemini AI to process natural language queries into SQL.

- **🧩 Data Presentation**  
  Displays query results in a https://github.com/darsh32774/OSMumbai-Client **clean, formatted table** using [`tabulate`](https://pypi.org/project/tabulate/).

- **🗺️ Interactive Map Generation**  
  Automatically saves a **Folium HTML map** locally for visualization in your browser.

- **🔗 Zero Config**  
  Backend URL is hardcoded — just run and query!

---

## ⚙️ Setup & Installation

### 1. Requirements

- Python 3.8+  
- Internet access (for backend API communication)

### 2. Installation Steps

```bash
# Clone the repository
git clone https://github.com/YourUsername/OSMumbai-client.git
cd OSMumbai-client

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
# .\venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

No additional configuration is needed — the API endpoint is **predefined** in `main_app.py`.

To start the client:

```bash
python main_app.py
```

You’ll see:

```
========================================
  Mumbai OSM Query (client)
========================================

Enter your query (or 'quit' to exit):
```

Type in natural language queries such as:

```
hospitals near vile parle
schools in andheri
cafes in bandra
fire stations in south mumbai
```

---

## 🧾 Output

Each query returns **three key components**:

1. **Generated SQL** – The backend-translated PostGIS query.  
2. **Tabular Results** – Cleanly formatted data output (e.g., name, area).  
3. **Map File** – An interactive HTML map (e.g., `map_cafes_in_bandra.html`) viewable in your browser.

---

## 📂 Example Output

```
========================================
Generated SQL:
SELECT name, amenity, ST_AsText(geom) FROM osm_points WHERE amenity='cafe' AND area='Bandra';

----------------------------------------
| Name             | Amenity | Area    |
----------------------------------------
| Blue Tokai Cafe  | cafe    | Bandra  |
| Starbucks        | cafe    | Bandra  |
----------------------------------------

✅ Map saved as: map_cafes_in_bandra.html
```

---

## 🧠 How It Works (Under the Hood)

1. User enters a **natural language query** in the CLI.  
2. The client sends the query to the **OSMumbai backend**.  
3. The backend (using **Gemini API + PostGIS**) converts it to an SQL query.  
4. The backend executes the query on the **Mumbai OSM database**.  
5. Results are sent back, displayed in the terminal, and mapped via **Folium**.

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| AI Engine | Google Gemini |
| Backend Framework | FastAPI |
| Database | PostgreSQL + PostGIS |
| Client | Python (CLI) |
| Visualization | Folium |
| Table Formatting | Tabulate |

---

## 🧑‍💻 Author

**Darsh Kukreja**  
Engineering Student • Builder of AI-driven Geospatial Tools  
[GitHub](https://github.com/YourUsername)

---

## 🪪 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

### 💡 Example Command Summary

| Command | Description |
|----------|--------------|
| `python main_app.py` | Launch the CLI client |
| `quit` | Exit the program |
| Any text query (e.g. “parks in Dadar”) | Generates results + map |

---

🧭 **Query Mumbai. Get Maps. Build Smarter.**
