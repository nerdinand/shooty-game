from pygame.math import Vector2

from .rectanglable import Rectanglable


class Intersection:
  def __init__(self, position: Vector2, rectanglable: Rectanglable):
    self.position = position
    self.rectanglable = rectanglable
