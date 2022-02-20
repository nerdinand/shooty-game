from typing import Optional
from typing import Tuple

import pygame

from .input import DirectionMapper
from .input import KeyMapper
from .input import MouseHandler
from .renderer import Renderer
from .renderer.render_settings import RenderSettings
from simulation import Human
from simulation import Simulation


class Gui:
    def __init__(
        self,
        render_every_tick_count: int = 10,
        key_target_player: Optional[Human] = None,
        resolution: Tuple[int, int] = (800, 600),
        render_settings=RenderSettings(),
    ):
        self.tick_count = 0
        self.render_every_tick_count = render_every_tick_count
        self.key_target_player = key_target_player
        self.renderer = Renderer(resolution, render_settings)
        self.mouse_handler = MouseHandler(self.renderer.screen_rect)

    def initialize(self) -> None:
        pygame.display.init()
        pygame.font.init()
        self.renderer.initialize()

    def tick(self) -> None:
        self.tick_count += 1

    def render(self, simulation: Simulation) -> None:
        self.renderer.render(simulation)
        self.tick_count = 0

    def handle_key_events(self) -> None:
        if self.key_target_player is None:
            return
        key_events = KeyMapper.map()
        if KeyMapper.QUIT in key_events:
            return
        if KeyMapper.RELOAD in key_events:
            self.key_target_player.gun.start_reload()
        if KeyMapper.TOGGLE_SHOW_MAP in key_events:
            self.renderer.render_settings.show_map = (
                not self.renderer.render_settings.show_map
            )
        if KeyMapper.TOGGLE_SHOW_BOTS in key_events:
            self.renderer.render_settings.show_bots = (
                not self.renderer.render_settings.show_bots
            )
        direction_vector = DirectionMapper.map(key_events)
        self.key_target_player.update_move_direction(direction_vector)

    def handle_mouse_events(self) -> None:
        if self.key_target_player is None:
            return
        self.mouse_handler.handle_mouse_events(self.key_target_player)

    @classmethod
    def should_quit(cls) -> bool:
        return KeyMapper.QUIT in KeyMapper.map()

    def is_render_necessary(self) -> bool:
        return self.tick_count == self.render_every_tick_count
