from pygame.math import Vector2

class Obstacle:
  def __init__(self, left, top, width, height):
    self.left_top = Vector2(left, top)
    self.width = width
    self.height = height

  def top(self):
    return self.left_top.y

  def left(self):
    return self.left_top.x

  def bottom(self):
    return self.top() + self.height

  def right(self):
    return self.left() + self.width

  def __str__(self):
    return f"(left_top: {self.left_top}, width: {self.width}, height: {self.height})"
