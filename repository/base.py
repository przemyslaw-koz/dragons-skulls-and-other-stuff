from abc import ABC, abstractmethod


class WorldRepository(ABC):
    @abstractmethod
    def get_location(self, location_name: str) -> dict:
        """Get full location data - desc, options, npcs, items"""
        pass

    @abstractmethod
    def get_location_description(self, location_name: str) -> str:
        """Get location description by name"""
        pass


#
#    @abstractmethod
#    def get_location_movement_options(self, location_name: str):
#        """Get location movement options by it's name"""
#        pass
