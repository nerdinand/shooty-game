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
        my_random = MathUtil.__get_random_or_raise()

        return Vector2(
            my_random.uniform(minimum, maximum),
            my_random.uniform(minimum, maximum),
        )

    @staticmethod
    def random_direction_change() -> float:
        return MathUtil.__get_random_or_raise().uniform(-10.0, 10.0)

    @staticmethod
    def random_float() -> float:
        return MathUtil.__get_random_or_raise().random()

    @staticmethod
    def __get_random_or_raise() -> random.Random:
        my_random = MathUtil.RANDOM
        if my_random is None:
            raise ValueError(
                "MathUtil.RANDOM has not been initialized. Call MathUtil.seed to \
do that before trying to generate random numbers."
            )
        return my_random
