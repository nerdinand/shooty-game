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
    """Main class of the Graphical User Interface (GUI)."""

    def __init__(
        self,
        render_every_tick_count: int = 10,
        key_target_player: Optional[Human] = None,
        resolution: Tuple[int, int] = (800, 600),
        render_settings: RenderSettings = RenderSettings(),
    ) -> None:
        """Initialize a new GUI.

        Args:
            render_every_tick_count (int): How often the GUI should be rendered.
            key_target_player (Optional[Human]): If set, determines the Player
                controlled by the keyboard and mouse.
            resolution: (Tuple[int, int]): What resolution to render the simulation in.
            render_settings (RenderSettings): The settings determining how the game is rendered.
        """
        self.tick_count = 0
        self.render_every_tick_count = render_every_tick_count
        self.key_target_player = key_target_player
        self.renderer = Renderer(resolution, render_settings)
        self.mouse_handler = MouseHandler(self.renderer.screen_rect)

    def initialize(self) -> None:
        """Initialize the necessary components of pygame."""
        pygame.display.init()
        pygame.font.init()
        self.renderer.initialize()

    def tick(self) -> None:
        """Advance the GUI by a tick."""
        self.tick_count += 1

    def render(self, simulation: Simulation) -> None:
        """Render the given simulation.

        Args:
            simulation (Simulation): The simulation containing the state to render.
        """
        self.renderer.render(simulation)
        self.tick_count = 0

    def handle_key_events(self) -> None:
        """Handle keyboard events.

        Handles the keyboard events for the `key_target_player`.
        """
        player = self.key_target_player
        if player is None:
            return
        key_events = KeyMapper.map()
        if KeyMapper.QUIT in key_events:
            return
        if KeyMapper.RELOAD in key_events:
            player.gun.start_reload()
        direction_vector = DirectionMapper.map(key_events)
        player.update_move_direction(direction_vector)

    def handle_mouse_events(self) -> None:
        """Handle mouse events.

        Handles the mouse events for the `key_target_player`.
        """
        if self.key_target_player is None:
            return
        self.mouse_handler.handle_mouse_events(self.key_target_player)

    @classmethod
    def should_quit(cls) -> bool:
        """Determine whether the GUI should quit.

        Can be used to figure out if the process hosting this GUI should exit.

        Returns:
            bool: Whether the GUI should quit.
        """
        return KeyMapper.QUIT in KeyMapper.map()

    def is_render_necessary(self) -> bool:
        """Determine whether rendering the GUI is necessary now.

        Returns:
            bool: Whether rendering is necessary.
        """
        return self.tick_count == self.render_every_tick_count
