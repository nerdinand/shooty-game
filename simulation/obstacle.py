from pygame.math import Vector2

# TODO: since obstacles are immutable, we can memoize results of all these methods, speeding it up.
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

  def left_bottom(self):
    return Vector2(self.left(), self.bottom())

  def right_top(self):
    return Vector2(self.right(), self.top())

  def right_bottom(self):
    return Vector2(self.right(), self.bottom())

  def left_side(self):
    return (self.left_top, self.left_bottom())

  def right_side(self):
    return (self.right_top(), self.right_bottom())

  def top_side(self):
    return (self.left_top, self.right_top())

  def bottom_side(self):
    return (self.left_bottom(), self.right_bottom())

  def all_sides(self):
    return [self.left_side(), self.right_side(), self.top_side(), self.bottom_side()]

  def __str__(self):
    return f"(left_top: {self.left_top}, width: {self.width}, height: {self.height})"
