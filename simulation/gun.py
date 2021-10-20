from pygame.math import Vector2

from .projectile import Projectile

class Gun:
  def __init__(self, player, cooldown_ticks=115):
    self.player = player
    self.cooldown_ticks = cooldown_ticks
    self.tick_count = 0
    self.projectiles = []

  def tick(self, projectile_collider):
    self.tick_count -= 1
    self.shoot() # TODO: just for testing
    for projectile in self.projectiles:
      projectile.tick(projectile_collider)
      if projectile.is_dead:
        self.projectiles.remove(projectile)

  def shoot(self):
    if self.__can_shoot():
      self.projectiles.append(Projectile(self, Vector2(self.player.position), self.player.look_direction))
      self.tick_count = self.cooldown_ticks

  def __can_shoot(self):
    return self.tick_count <= 0
