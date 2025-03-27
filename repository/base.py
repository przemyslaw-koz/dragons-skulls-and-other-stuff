from abc import ABC, abstractmethod
from typing import Optional


class WorldRepository(ABC):
    @abstractmethod
    def get_location(self, location_id: int) -> Optional[dict]:
        """Get full location data - desc, options, npcs, items"""
        pass


#    @abstractmethod
#    def get_location_description(self, location_name: str) -> str:
#        """Get location description by name"""
#        pass
#
#    @abstractmethod
#    def get_npcs(self, location_id: int) -> dict:
#        """Get npcs available in location"""
#        pass


#
#    @abstractmethod
#    def get_location_movement_options(self, location_name: str):
#        """Get location movement options by it's name"""
#        pass
