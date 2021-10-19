import pygame

from .utils import Utils
from .colors import Colors
from .projectile_renderer import ProjectileRenderer

class GunRenderer:
  GUN_LENGTH = 15 # FIXME: Should scale with player size

  def __init__(self):
    self.projectile_renderer = ProjectileRenderer()

  def render(self, screen, player):
    screen_position = Utils.to_screen_position(screen.get_size(), player.position)
    pygame.draw.line(screen, Colors.GUN_COLOR, screen_position, screen_position + self.gun_tip(player.look_direction))
    for projectile in player.gun.projectiles:
      self.projectile_renderer.render(screen, projectile)

  def gun_tip(self, player_look_direction):
    v = pygame.math.Vector2()
    v.from_polar((GunRenderer.GUN_LENGTH, player_look_direction))
    return v
