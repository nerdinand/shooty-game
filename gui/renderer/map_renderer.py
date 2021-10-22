from typing import List, Tuple

import pygame
from pygame.locals import Rect

from .colors import Colors
from simulation import Obstacle
from simulation import Rectangle
from simulation import Map


class MapRenderer:
  def render(self, screen: pygame.surface.Surface, map: Map) -> None:
    for screen_obstacle in self.__screen_obstacles(screen.get_size(), map.obstacles):
      pygame.draw.rect(screen, Colors.OBSTACLES_COLOR, screen_obstacle)

  def __screen_obstacles(
    self, screen_size: Tuple[int, int], obstacles: List[Obstacle]
  ) -> List[Rect]:
    return [self.__to_screen_rect(screen_size, obstacle) for obstacle in obstacles]

  def __to_screen_rect(self, screen_size: Tuple[int, int], obstacle: Obstacle) -> Rect:
    rectangle = obstacle.get_rectangle()
    left_top_transformed = rectangle.left_top.elementwise() * screen_size  # type: ignore[operator]
    width_transformed = rectangle.width * screen_size[0]
    height_transformed = rectangle.height * screen_size[1]
    return Rect(
      left_top_transformed.x,
      left_top_transformed.y,
      width_transformed,
      height_transformed
    )
