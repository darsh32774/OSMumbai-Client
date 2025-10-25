OSMumbai Client: Natural Language to Map CLI

This repository contains the command-line interface (CLI) client for the OSMumbai API, a backend service deployed on Render. This service functions as an Agentic AI system, utilizing the Gemini API to process natural language queries and autonomously translate them into structured PostGIS SQL queries for execution against Mumbai OpenStreetMap data.

HThe backend URL is hardcoded directly in main_app.py for connectivity.

Features

API Integration: Connects directly to the live, remote backend API at https://osmumbai.onrender.com.

Data Presentation: Displays database results in a clear, formatted table using tabulate.

Map Generation: Saves the returned Folium HTML map for local browser viewing.

Setup and Installation

1. Requirements

The client requires a Python environment and access to the public internet.

2. Installation

Clone the repository and install the required dependencies using pip.

git clone [https://github.com/darsh32774/OSMumbai-Client.git](https://github.com/darsh32774/OSMumbai-Client.git)
cd OSMumbai-Client
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# .\venv\Scripts\activate  # Windows

pip install -r requirements.txt



Execution

No separate configuration step is required as the API endpoint is hardcoded. Execute the main application file:

python main_app.py



The application will prompt for natural language input:

========================================
  Mumbai OSM Query (client)
========================================

Enter your query (or 'quit' to exit): 



Example Queries

hospitals near vile parle

schools in andheri

cafes in bandra

fire stations in south mumbai

Output

A successful query returns three components:

Generated SQL: The specific PostGIS query created by the backend.

Tabular Results: A formatted list of data points (name, area).

Map File: An HTML file saved locally (e.g., map_cafes_in_bandra.html) containing the interactive Folium map.
