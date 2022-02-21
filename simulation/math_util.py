import random
from typing import Optional

from pygame.math import Vector2


class MathUtil:
    RANDOM: Optional[random.Random] = None

    @staticmethod
    def seed(seed: Optional[int]) -> None:
        MathUtil.RANDOM = random.Random(seed)

    @staticmethod
    def random_vector2(minimum: float = 0.0, maximum: float = 1.0) -> Vector2:
        my_random = MathUtil.RANDOM
        if my_random is None:
            raise ValueError

        return Vector2(
            my_random.uniform(minimum, maximum),
            my_random.uniform(minimum, maximum),
        )

    @staticmethod
    def random_direction_change() -> float:
        my_random = MathUtil.RANDOM
        if my_random is None:
            raise ValueError

        return my_random.uniform(-10.0, 10.0)

    @staticmethod
    def random_float() -> float:
        my_random = MathUtil.RANDOM
        if my_random is None:
            raise ValueError

        return my_random.random()
