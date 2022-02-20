from typing import Tuple

from pygame.math import Vector2


class Utils:
    @staticmethod
    def to_screen_position(screen_size: Tuple[int, int], position: Vector2) -> Vector2:
        return position.elementwise() * screen_size
