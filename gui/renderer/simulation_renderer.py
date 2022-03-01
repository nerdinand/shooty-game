import pygame

from .map_renderer import MapRenderer
from .player_renderer import PlayerRenderer
from .render_settings import RenderSettings
from .visibility_renderer import VisibilityRenderer
from simulation import Simulation


class SimulationRenderer:
    @classmethod
    def render(
        cls,
        screen: pygame.surface.Surface,
        render_settings: RenderSettings,
        simulation: Simulation,
    ) -> None:
        if render_settings.show_map:
            MapRenderer.render(screen, simulation.map)

        if render_settings.show_visibility and simulation.human is not None:
            VisibilityRenderer.render(
                screen, simulation.human, simulation.get_obstacles()
            )

        for player in simulation.players:
            if player.is_human() or player.is_dead or render_settings.show_bots:
                PlayerRenderer.render(screen, player)
