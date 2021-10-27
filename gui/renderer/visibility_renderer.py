import pygame

from simulation import Simulation, Visibility, Obstacle, Bot, Human
from .utils import Utils
from .colors import Colors


class VisibilityRenderer:
  COLOR_MAP = {
    Obstacle: Colors.OBSTACLES_COLOR,
    Bot: Colors.BOT_COLOR,
    Human: Colors.HUMAN_COLOR
  }

  def __init__(self) -> None:
    self.visibility = Visibility()

  def render(self, screen: pygame.surface.Surface, simulation: Simulation) -> None:
    visible_points = self.visibility.get_visible_points(simulation, simulation.human)
    for visible_point in visible_points:
      screen_position = Utils.to_screen_position(
        screen.get_size(), visible_point.position
      )
      pygame.draw.circle(
        screen,
        VisibilityRenderer.COLOR_MAP[visible_point.rectanglable.__class__],
        screen_position,
        1
      )
