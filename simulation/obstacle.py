from .rectangle import Rectangle


class Obstacle:
  def __init__(self, left: float, top: float, width: float, height: float):
    self.left = left
    self.top = top
    self.width = width
    self.height = height

  def get_rectangle(self) -> Rectangle:
    return Rectangle(self.left, self.top, self.width, self.height)

  def apply_damage(self, damage: int) -> None:
    pass
