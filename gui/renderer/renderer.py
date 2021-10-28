from typing import Tuple

import pygame
from pygame.locals import Rect

from .colors import Colors
from .simulation_renderer import SimulationRenderer
from .font_renderer import FontRenderer
from .render_settings import RenderSettings
from simulation import Simulation


class Renderer:
  def __init__(self, resolution: Tuple[int, int]):
    self.screen_rect = Rect(0, 0, resolution[0], resolution[1])
    self.simulation_renderer = SimulationRenderer()
    self.render_settings = RenderSettings()

  def initialize(self) -> None:
    winstyle = 0  # full screen
    bestdepth = pygame.display.mode_ok(self.screen_rect.size, winstyle, 32)
    self.screen = pygame.display.set_mode(self.screen_rect.size, winstyle, bestdepth)
    FontRenderer.initialize()

  def render(self, simulation: Simulation) -> None:
    self.screen.fill(Colors.BACKGROUND_COLOR)
    self.simulation_renderer.render(self.screen, self.render_settings, simulation)
    FontRenderer.render(self.screen, f"Tick: {simulation.tick_count}", (10, 10))
    pygame.display.update()
