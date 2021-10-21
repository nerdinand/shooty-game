from .map_renderer import MapRenderer
from .player_renderer import PlayerRenderer


class SimulationRenderer:
  def __init__(self):
    self.map_renderer = MapRenderer()
    self.player_renderer = PlayerRenderer()

  def render(self, screen, simulation):
    self.map_renderer.render(screen, simulation.map)
    for player in simulation.players:
      self.player_renderer.render(screen, player)
