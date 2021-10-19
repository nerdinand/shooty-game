import pygame
from pygame.locals import Rect

from .colors import Colors
from .simulation_renderer import SimulationRenderer

class Renderer:
  def __init__(self, resolution):
    self.screen_rect = Rect(0, 0, resolution[0], resolution[1])
    self.simulation_renderer = SimulationRenderer()

  def initialize(self):
    winstyle = 0  # full screen
    bestdepth = pygame.display.mode_ok(self.screen_rect.size, winstyle, 32)
    self.screen = pygame.display.set_mode(self.screen_rect.size, winstyle, bestdepth)
    self.font = pygame.font.Font(pygame.font.get_default_font(), 12)

  def render(self, simulation):
    self.screen.fill(Colors.BACKGROUND_COLOR)
    self.simulation_renderer.render(self.screen, simulation)
    font_surface = self.font.render(f"Tick: {simulation.tick_count}", True, Colors.TEXT_COLOR)
    self.screen.blit(font_surface, (0, 0))
    pygame.display.update()
