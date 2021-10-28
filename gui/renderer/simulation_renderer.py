import pygame

from .map_renderer import MapRenderer
from .player_renderer import PlayerRenderer
from .visibility_renderer import VisibilityRenderer
from .render_settings import RenderSettings
from simulation import Simulation


class SimulationRenderer:
  def __init__(self) -> None:
    self.map_renderer = MapRenderer()
    self.player_renderer = PlayerRenderer()
    self.visibility_renderer = VisibilityRenderer()

  def render(
    self, screen: pygame.surface.Surface, render_settings: RenderSettings, simulation: Simulation
  ) -> None:
    if render_settings.show_map:
      self.map_renderer.render(screen, simulation.map)

    if simulation.human is not None:
      self.visibility_renderer.render(screen, simulation)

    for player in simulation.players:
      if player.is_human() or player.is_dead or render_settings.show_bots:
        self.player_renderer.render(screen, player)
