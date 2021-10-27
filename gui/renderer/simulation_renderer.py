import pygame

from .map_renderer import MapRenderer
from .player_renderer import PlayerRenderer
from .visibility_renderer import VisibilityRenderer
from simulation import Simulation


class SimulationRenderer:
  def __init__(self) -> None:
    self.map_renderer = MapRenderer()
    self.player_renderer = PlayerRenderer()
    self.visibility_renderer = VisibilityRenderer()

  def render(self, screen: pygame.surface.Surface, simulation: Simulation) -> None:
    self.map_renderer.render(screen, simulation.map)

    if simulation.human is not None:
      self.visibility_renderer.render(screen, simulation)

    for player in simulation.players:
      self.player_renderer.render(screen, player)
