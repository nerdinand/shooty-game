import pygame

from .colors import Colors
from .utils import Utils


class ProjectileRenderer:
  def render(self, screen, projectile):
    screen_position = Utils.to_screen_position(screen.get_size(), projectile.position)
    pygame.draw.circle(screen, Colors.PROJECTILES_COLOR, screen_position, 2)
