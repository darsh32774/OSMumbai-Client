# client/main_app.py
import os
import sys
import requests
from tabulate import tabulate

SERVER_URL = "https://osmumbai.onrender.com"

def ask_server_for_map(user_query: str, geom_key_hint: str = None, max_rows: int = 500):
    # 1. FIX: Change 'user_prompt' to 'query' to match server expectation
    payload = {
        "query": user_query, 
        "geom_key_hint": geom_key_hint,
        "max_rows": max_rows
    }
    resp = requests.post(f"{SERVER_URL}/nl-to-map", json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()

def save_map_html(map_html: str, query: str):
    safe_name = "".join(c if c.isalnum() else "_" for c in query)[:40]
    filename = f"map_{safe_name}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(map_html)
    return filename

def main():
    print("="*40)
    print("  Mumbai OSM Query (client)")
    print("="*40)
    while True:
        try:
            query = input("\nEnter your query (or 'quit' to exit): ").strip()
            if query.lower() in ("quit", "exit", "q"):
                break
            if not query:
                print("Please enter a query.")
                continue

            print("Sending query to backend...")
            try:
                data = ask_server_for_map(query)
            except requests.exceptions.HTTPError as he:
                # Handle 4xx/5xx responses specifically (e.g., from JSONResponse error)
                try:
                    error_data = he.response.json()
                    print(f"Server returned an error: {error_data.get('error', 'Unknown HTTP Error')}")
                except Exception:
                    print(f"Server error: {he}")
                continue
            except Exception as e:
                print(f"Connection/request error: {e}")
                continue

            # Keys now match the server's response:
            sql = data.get("sql")
            rows_count = data.get("rows_count", 0)
            headers = data.get("headers", [])
            display_rows = data.get("display_rows", [])
            map_html = data.get("map_html")

            print(f"\nGenerated SQL:\n{sql}\n")
            print(f"Found {rows_count} results.\n")
            if display_rows and headers:
                print(tabulate(display_rows, headers=headers, tablefmt="psql"))
            else:
                print("No tabular result to display.")

            # Map generation section is now robust due to consistent key 'map_html'
            if map_html:
                filename = save_map_html(map_html, query)
                print(f"\nMap saved to '{filename}'. Open it in your browser to view.")
            else:
                print("No map generated for this query.")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            import traceback; traceback.print_exc()
            continue

    print("Goodbye!")

if __name__ == "__main__":
    main()
