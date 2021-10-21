from .obstacle import Obstacle


class Map:
  WALL_THICKNESS = 0.01

  def __init__(self):
    self.obstacles = []
    self.__add_edge_obstacles()

  def __add_edge_obstacles(self):
    # left wall
    self.obstacles.append(Obstacle(0, 0, Map.WALL_THICKNESS, 1.0))
    # top wall
    self.obstacles.append(Obstacle(0, 0, 1.0, Map.WALL_THICKNESS))
    # right wall
    self.obstacles.append(Obstacle(1.0 - Map.WALL_THICKNESS, 0.0, Map.WALL_THICKNESS, 1.0))
    # bottom wall
    self.obstacles.append(Obstacle(0.0, 1.0 - Map.WALL_THICKNESS, 1.0, Map.WALL_THICKNESS))

  def tick(self):
    pass
