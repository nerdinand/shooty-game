from typing import Sequence, Tuple

import pygame
from pygame.locals import Rect

from .colors import Colors
from simulation import Obstacle
from simulation import Rectangle
from simulation import Map
from simulation import Entity


class MapRenderer:
  def render(self, screen: pygame.surface.Surface, map: Map) -> None:
    visible_objects = map.obstacles
    screen_obstacles = self.__screen_obstacles(screen.get_size(), visible_objects)
    for screen_obstacle in screen_obstacles:
        pygame.draw.rect(screen, Colors.OBSTACLES_COLOR, screen_obstacle)

  def __screen_obstacles(
    self, screen_size: Tuple[int, int], entitys: Sequence[Entity]
  ) -> Sequence[Rect]:
    return [self.__to_screen_rect(screen_size, entity) for entity in entitys]

  def __to_screen_rect(self, screen_size: Tuple[int, int], entity: Entity) -> Rect:
    rectangle = entity.get_rectangle()
    left_top_transformed = rectangle.left_top.elementwise() * screen_size  # type: ignore[operator]
    width_transformed = rectangle.width * screen_size[0]
    height_transformed = rectangle.height * screen_size[1]
    return Rect(
      left_top_transformed.x,
      left_top_transformed.y,
      width_transformed,
      height_transformed
    )
