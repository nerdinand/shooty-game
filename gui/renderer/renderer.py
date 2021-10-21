import pygame
from pygame.locals import Rect

from .colors import Colors
from .simulation_renderer import SimulationRenderer
from .font_renderer import FontRenderer


class Renderer:
  def __init__(self, resolution):
    self.screen_rect = Rect(0, 0, resolution[0], resolution[1])
    self.simulation_renderer = SimulationRenderer()

  def initialize(self):
    winstyle = 0  # full screen
    bestdepth = pygame.display.mode_ok(self.screen_rect.size, winstyle, 32)
    self.screen = pygame.display.set_mode(self.screen_rect.size, winstyle, bestdepth)
    FontRenderer.initialize()

  def render(self, simulation):
    self.screen.fill(Colors.BACKGROUND_COLOR)
    self.simulation_renderer.render(self.screen, simulation)
    FontRenderer.render(self.screen, f"Tick: {simulation.tick_count}", (10, 10))
    pygame.display.update()
