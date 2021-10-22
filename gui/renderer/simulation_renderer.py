import pygame

from .map_renderer import MapRenderer
from .player_renderer import PlayerRenderer
from simulation import Simulation


class SimulationRenderer:
  def __init__(self) -> None:
    self.map_renderer = MapRenderer()
    self.player_renderer = PlayerRenderer()

  def render(self, screen: pygame.surface.Surface, simulation: Simulation) -> None:
    self.map_renderer.render(screen, simulation.map)
    for player in simulation.players:
      self.player_renderer.render(screen, player)
