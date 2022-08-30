from .map import Map
from .simple_map import SimpleMap
from .simplest_map import SimplestMap


class MapFactory:
    @classmethod
    def map(cls, map_name: str) -> Map:
        match map_name:
            case "SimpleMap":
                return cls.__simple_map()
            case "SimplestMap":
                return cls.__simplest_map()
            case _:
                raise ValueError(f"'{map_name}' is not a valid map.")

    @classmethod
    def __simple_map(cls) -> Map:
        return SimpleMap()

    @classmethod
    def __simplest_map(cls) -> Map:
        return SimplestMap()
