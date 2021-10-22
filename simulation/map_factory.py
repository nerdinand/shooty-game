from .simple_map import SimpleMap
from .map import Map


class MapFactory:
  def simple_map(self) -> Map:
    return SimpleMap()
