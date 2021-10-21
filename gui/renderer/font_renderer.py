import pygame

from .colors import Colors


class FontRenderer:
  @staticmethod
  def initialize():
    FontRenderer.font = pygame.font.Font(pygame.font.get_default_font(), 12)

  def render(screen, text, position):
    font_surface = FontRenderer.font.render(text, True, Colors.TEXT_COLOR)
    screen.blit(font_surface, position)
