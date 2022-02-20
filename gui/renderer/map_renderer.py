from typing import Sequence
from typing import Tuple

import pygame
from pygame.locals import Rect

from .colors import Colors
from simulation import Entity
from simulation import Map


class MapRenderer:
    @classmethod
    def render(cls, screen: pygame.surface.Surface, my_map: Map) -> None:
        visible_objects = my_map.obstacles
        screen_obstacles = MapRenderer.__screen_obstacles(
            screen.get_size(), visible_objects
        )
        for screen_obstacle in screen_obstacles:
            pygame.draw.rect(screen, Colors.OBSTACLES_COLOR, screen_obstacle)

    @classmethod
    def __screen_obstacles(
        cls, screen_size: Tuple[int, int], entitys: Sequence[Entity]
    ) -> Sequence[Rect]:
        return [MapRenderer.__to_screen_rect(screen_size, entity) for entity in entitys]

    @classmethod
    def __to_screen_rect(cls, screen_size: Tuple[int, int], entity: Entity) -> Rect:
        rectangle = entity.get_rectangle()
        left_top_transformed = rectangle.left_top.elementwise() * screen_size
        width_transformed = rectangle.width * screen_size[0]
        height_transformed = rectangle.height * screen_size[1]
        return Rect(
            left_top_transformed.x,
            left_top_transformed.y,
            width_transformed,
            height_transformed,
        )
