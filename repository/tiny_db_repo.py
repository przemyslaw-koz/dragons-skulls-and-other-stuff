from tinydb import Query, TinyDB

from repository.base import WorldRepository


class TinyDBWorldRepository(WorldRepository):
    def __init__(self, db_path: str):
        self.db = TinyDB(db_path)
        self.query = Query()

    def get_location(self, location_name: str) -> dict:
        result = self.db.search(self.query[location_name].exists())
        return result[0][location_name] if result else {}

    def get_location_description(self, location_name: str) -> str:
        location = self.get_location(location_name)
        return location.get("description", "Nie znaleziono opisu...")


#    @abstractmethod
#    def get_location_movement_options(self, location_name: str):
#        """Get location movement options by it's name"""
#        pass
