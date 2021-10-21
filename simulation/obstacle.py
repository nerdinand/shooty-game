from pygame.math import Vector2


class Obstacle:
  def __init__(self, left, top, width, height):
    self.left_top = Vector2(left, top)
    self.width = width
    self.height = height
    self.all_sides = self.__all_sides()

  def apply_damage(self, amount):  # TODO: find cleaner solution
    pass

  def bounding_box(self):  # TODO: find cleaner solution
    return self

  def top(self):
    return self.left_top.y

  def left(self):
    return self.left_top.x

  def bottom(self):
    return self.top() + self.height

  def right(self):
    return self.left() + self.width

  def __left_bottom(self):
    return Vector2(self.left(), self.bottom())

  def __right_top(self):
    return Vector2(self.right(), self.top())

  def __right_bottom(self):
    return Vector2(self.right(), self.bottom())

  def __left_side(self):
    return (self.left_top, self.__left_bottom())

  def __right_side(self):
    return (self.__right_top(), self.__right_bottom())

  def __top_side(self):
    return (self.left_top, self.__right_top())

  def __bottom_side(self):
    return (self.__left_bottom(), self.__right_bottom())

  def __all_sides(self):
    return [
      self.__left_side(),
      self.__right_side(),
      self.__top_side(),
      self.__bottom_side()
    ]

  def __str__(self):
    return f"(left_top: {self.left_top}, \
width: {self.width}, height: {self.height})"
