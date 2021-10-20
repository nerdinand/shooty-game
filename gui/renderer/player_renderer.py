import pygame
from pygame.locals import Rect
from pygame.math import Vector2

from .colors import Colors
from simulation import PlayerType
from .gun_renderer import GunRenderer
from .utils import Utils

class PlayerRenderer:
  PLAYER_COLORS = {
    PlayerType.HUMAN: Colors.HUMAN_COLOR,
    PlayerType.BOT: Colors.BOT_COLOR
  }

  def __init__(self):
    self.gun_renderer = GunRenderer()

  def render(self, screen, player):
    screen_rect = self.__to_screen_rect(screen.get_size(), player)
    color = PlayerRenderer.PLAYER_COLORS[player.player_type]

    pygame.draw.ellipse(screen, color, screen_rect, width=1)

    if player.is_dead:
      pygame.draw.line(screen, color, (screen_rect.left, screen_rect.top), (screen_rect.right, screen_rect.bottom))
      pygame.draw.line(screen, color, (screen_rect.left, screen_rect.bottom), (screen_rect.right, screen_rect.top))

    self.gun_renderer.render(screen, player)

  def __to_screen_rect(self, screen_size, player):
    player_screen_extent = Vector2(screen_size) * player.extent()
    left_top = Utils.to_screen_position(screen_size, player.position) - (player_screen_extent / 2.0)
    return Rect(left_top.x, left_top.y, player_screen_extent.x, player_screen_extent.y)
