import os
import sys

from tinydb import TinyDB

from game.world import world  # Importowanie mapy świata

game_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../game"))
sys.path.append(game_dir)


db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../db/world.json"))

db = TinyDB(db_path)

db.truncate()

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
