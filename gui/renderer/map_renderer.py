from typing import Sequence
from typing import Tuple

import pygame
from pygame.locals import Rect
from pygame.math import Vector2

from .colors import Colors
from simulation import Map
from simulation import Obstacle


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
        cls, screen_size: Tuple[int, int], obstacles: Sequence[Obstacle]
    ) -> Sequence[Rect]:
        return [
            MapRenderer.__to_screen_rect(screen_size, obstacle)
            for obstacle in obstacles
        ]

    @classmethod
    def __to_screen_rect(cls, screen_size: Tuple[int, int], obstacle: Obstacle) -> Rect:
        rectangle = obstacle.get_rectangle()
        left_top_transformed: Tuple[int, ...] = (
            rectangle.left_top.elementwise() * screen_size  # pyre-ignore[58]
        )
        width_transformed = rectangle.width * screen_size[0]
        height_transformed = rectangle.height * screen_size[1]
        return Rect(
            left_top_transformed[0],
            left_top_transformed[1],
            width_transformed,
            height_transformed,
        )
