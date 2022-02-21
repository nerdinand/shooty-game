from simulation.math_util import MathUtil
from pygame.math import Vector2


class TestMathUtil:
    def test_random_seeding(self) -> None:
        MathUtil.seed(1337)
        assert MathUtil.random_float() == 0.6177528569514706
        assert MathUtil.random_vector2() == Vector2(0.533266, 0.365848)
        assert MathUtil.random_direction_change() == 1.7157470780454318
