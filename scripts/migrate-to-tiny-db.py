import os
import sys

from tinydb import TinyDB

# Dodaj ścieżkę do bieżącego katalogu projektu do sys.path
sys.path.append(os.getcwd())

from game.world import world


def migrate_to_tinydb(db_path: str):
    db = TinyDB(db_path)
    for location_name, location_data in world.items():
        db.insert({location_name: location_data})

    print(f"Data migrated to {db_path}")


if __name__ == "__main__":
    migrate_to_tinydb("db/world.json")
