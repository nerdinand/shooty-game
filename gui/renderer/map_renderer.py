from typing import Sequence
from typing import Tuple

import pygame
from pygame.locals import Rect
from pygame.math import Vector2

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
        cls, screen_size: Tuple[int, int], entities: Sequence[Entity]
    ) -> Sequence[Rect]:
        return [
            MapRenderer.__to_screen_rect(screen_size, entity) for entity in entities
        ]

    @classmethod
    def __to_screen_rect(cls, screen_size: Tuple[int, int], entity: Entity) -> Rect:
        rectangle = entity.get_rectangle()
        left_top_transformed: Vector2 = (  # pyre-ignore[9]
            rectangle.left_top.elementwise() * screen_size  # pyre-ignore[58]
        )
        width_transformed = rectangle.width * screen_size[0]
        height_transformed = rectangle.height * screen_size[1]
        return Rect(
            left_top_transformed.x,
            left_top_transformed.y,
            width_transformed,
            height_transformed,
        )
