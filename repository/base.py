from abc import ABC, abstractmethod


class WorldRepository(ABC):
    @abstractmethod
    def get_location(self, location_name: str):
        """Get full location data - desc, options, npcs, items"""
        pass
