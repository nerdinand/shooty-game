from pygame.math import Vector2

from .projectile import Projectile

class Gun:
  def __init__(self, player, cooldown_ticks, magazine_size, damage, spray_pattern, reload_ticks):
    self.player = player
    self.cooldown_ticks = cooldown_ticks
    self.magazine_size = magazine_size
    self.damage = damage
    self.spray_pattern = spray_pattern
    self.reload_ticks = reload_ticks
    self.tick_count = 0
    self.spray_sequence = 0
    self.projectiles = []
    self.reload_tick_count = reload_ticks
    self.bullet_count = magazine_size
    self.is_reloading = False

  def tick(self, projectile_collider):
    self.tick_count -= 1

    self.__reload_tick()

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

  def start_reload(self):
    if self.is_reloading:
      return
    self.is_reloading = True

  def __reload_tick(self):
    if self.is_reloading:
      self.reload_tick_count -= 1
      if self.reload_tick_count == 0:
        self.is_reloading = False
        self.bullet_count = self.magazine_size
        self.reload_tick_count = self.reload_ticks

  def __can_shoot(self):
    return not self.player.is_dead and self.tick_count <= 0 and self.bullet_count > 0 and not self.is_reloading
