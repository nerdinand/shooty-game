from typing import Tuple

import pygame
from pygame.locals import Rect

from .colors import Colors
from .font_renderer import FontRenderer
from .render_settings import RenderSettings
from .simulation_renderer import SimulationRenderer
from simulation import Simulation


class Renderer:
    def __init__(
        self, resolution: Tuple[int, int], render_settings: RenderSettings
    ) -> None:
        self.screen_rect = Rect(0, 0, resolution[0], resolution[1])
        self.render_settings = render_settings
        self.screen: pygame.display.Surface = None  # pyre-ignore[8]

    def initialize(self) -> None:
        winstyle = 0  # full screen
        bestdepth = pygame.display.mode_ok(self.screen_rect.size, winstyle, 32)
        self.screen = pygame.display.set_mode(
            self.screen_rect.size, winstyle, bestdepth
        )
        FontRenderer.initialize()

    def render(self, simulation: Simulation) -> None:
        self.screen.fill(Colors.BACKGROUND_COLOR)
        SimulationRenderer.render(self.screen, self.render_settings, simulation)
        FontRenderer.render(self.screen, f"Tick: {simulation.tick_count}", (10, 10))
        pygame.display.update()
