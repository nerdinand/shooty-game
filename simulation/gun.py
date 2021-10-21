from pygame.math import Vector2

from .projectile import Projectile

class Gun:
  def __init__(self, player, cooldown_ticks, bullet_count, damage, spray_pattern):
    self.player = player
    self.cooldown_ticks = cooldown_ticks
    self.bullet_count = bullet_count
    self.damage = damage
    self.spray_pattern = spray_pattern
    self.tick_count = 0
    self.spray_sequence = 0
    self.projectiles = []

  def tick(self, projectile_collider):
    self.tick_count -= 1
    for projectile in self.projectiles:
      projectile.tick(projectile_collider)
      if projectile.is_dead:
        self.projectiles.remove(projectile)

  def shoot(self):
    if self.__can_shoot():
      if self.tick_count == 0: # spraying
        self.spray_sequence += 1
      else: # not spraying, reset sequence
        self.spray_sequence = 0

      self.projectiles.append(
        Projectile(
          self, 
          Vector2(self.player.position), 
          self.player.look_direction + self.spray_pattern.offsets[self.spray_sequence]
        )
      )
      self.tick_count = self.cooldown_ticks
      self.bullet_count -= 1

  def __can_shoot(self):
    return self.tick_count <= 0 and self.bullet_count > 0
