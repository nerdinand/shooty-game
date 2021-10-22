from typing import List

from .obstacle import Obstacle


class Map:
  WALL_THICKNESS = 0.01

  def __init__(self) -> None:
    self.obstacles: List[Obstacle] = []
    self.__add_edge_obstacles()

  def __add_edge_obstacles(self) -> None:
    # left wall
    self.obstacles.append(Obstacle(0, 0, Map.WALL_THICKNESS, 1.0))
    # top wall
    self.obstacles.append(Obstacle(0, 0, 1.0, Map.WALL_THICKNESS))
    # right wall
    self.obstacles.append(Obstacle(1.0 - Map.WALL_THICKNESS, 0.0, Map.WALL_THICKNESS, 1.0))
    # bottom wall
    self.obstacles.append(Obstacle(0.0, 1.0 - Map.WALL_THICKNESS, 1.0, Map.WALL_THICKNESS))

  def tick(self) -> None:
    pass
