from pygame.math import Vector2

class Projectile:
  VELOCITY = 1e-3

  def __init__(self, position, direction):
    self.position = position
    self.direction = direction

  def tick(self):
    v = Vector2()
    v.from_polar((Projectile.VELOCITY, self.direction))
    self.position += v

  def is_dead(self):
    return False # TODO: implement properly