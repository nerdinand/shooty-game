import random

from pygame.math import Vector2


class MathUtil:
    @staticmethod
    def random_vector2(minimum: float = 0.0, maximum: float = 1.0) -> Vector2:
        return Vector2(
            random.uniform(minimum, maximum), random.uniform(minimum, maximum)
        )

    @staticmethod
    def random_direction_change() -> float:
        return random.uniform(-10.0, 10.0)
