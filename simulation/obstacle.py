from .rectangle import Rectangle
from .collision import Collision


class Obstacle:
  def __init__(self, name: str, left: float, top: float, width: float, height: float):
    self.name = name
    self.left = left
    self.top = top
    self.width = width
    self.height = height

  def get_rectangle(self) -> Rectangle:
    return Rectangle(self.left, self.top, self.width, self.height)

  def get_name(self) -> str:
    return self.name

  def hit(self, collision: Collision) -> None:
    pass
