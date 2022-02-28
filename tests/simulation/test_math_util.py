from pygame.math import Vector2

from simulation.math_util import MathUtil

import pytest


class TestMathUtil:
    def setup_method(self) -> None:
        MathUtil.RANDOM = None

    def test_not_seeded(self) -> None:
        with pytest.raises(ValueError):
            MathUtil.random_float()
        with pytest.raises(ValueError):
            MathUtil.random_vector2()
        with pytest.raises(ValueError):
            MathUtil.random_direction_change()

    def test_random_seeding(self) -> None:
        MathUtil.seed(1337)
        assert MathUtil.random_float() == 0.6177528569514706
        assert MathUtil.random_vector2() == Vector2(0.533266, 0.365848)
        assert MathUtil.random_direction_change() == 1.7157470780454318
