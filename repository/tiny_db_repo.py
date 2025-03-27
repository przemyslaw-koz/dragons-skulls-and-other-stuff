from tinydb import Query, TinyDB

from repository.base import WorldRepository


class TinyDBWorldRepository(WorldRepository):
    def __init__(self, db_path: str):
        self.db = TinyDB(db_path)
        self.query = Query()

    def get_location(self, location_id: int) -> dict:
        result = self.db.get(doc_id=location_id)
        if result:
            return dict(result)  # type:ignore
        return {}

    # def get_location_description(self, location_name: str) -> str:
    #     location = self.get_location(location_name)
    #     return location.get("description", "Nie znaleziono opisu...")

    def get_npcs(self, location_id: int) -> dict:
        location = self.get_location(location_id)
        if location:
            return location.get("npcs", {})
        return {}


#    @abstractmethod
#    def get_location_movement_options(self, location_name: str):
#        """Get location movement options by it's name"""
#        pass

if __name__ == "__main__":
    repo = TinyDBWorldRepository("db/world.json")
    loc = repo.get_location(1)
    print("YOYOYO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(loc)
    npcs = repo.get_npcs(1)
    print("DRUGA TURA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(npcs)
