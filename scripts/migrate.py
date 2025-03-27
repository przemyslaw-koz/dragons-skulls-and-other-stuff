import json
import os
import sys

from tinydb import Query, TinyDB

# Uzyskanie bezwzględnej ścieżki do katalogu 'game'
game_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../game"))
sys.path.append(game_dir)

from game.world import world  # Importowanie mapy świata

# Ścieżka do pliku JSON
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../db/world.json"))

# Inicjalizacja bazy danych TinyDB
db = TinyDB(db_path)

# Usunięcie istniejących danych w bazie (jeśli jakieś istnieją)
db.truncate()

# Migracja danych do TinyDB
for location_name, location_data in world.items():
    location_entry = {
        "name": location_name,
        "desc": location_data.get("desc", ""),
        "options": location_data.get("options", {}),
        "npcs": location_data.get("npcs", {}),
        "items": location_data.get("items", {}),
    }
    db.insert(location_entry)

print("Dane zostały zaimportowane do TinyDB.")
