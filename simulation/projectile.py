from pygame.math import Vector2

class Projectile:
  VELOCITY = 1e-3

  def __init__(self, position, direction):
    self.position = position
    self.direction = direction
    self.is_dead = False
    self.last_position = position

  def tick(self, collider):
    self.last_position = Vector2(self.position)
    v = Vector2()
    v.from_polar((Projectile.VELOCITY, self.direction))
    self.position += v

    if collider.projectile_collided(self):
      self.is_dead = True

