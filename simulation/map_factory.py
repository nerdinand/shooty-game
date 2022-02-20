from .map import Map
from .simple_map import SimpleMap


class MapFactory:
    @classmethod
    def simple_map(cls) -> Map:
        return SimpleMap()
