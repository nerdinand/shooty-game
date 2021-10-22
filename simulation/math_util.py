import random
from pygame.math import Vector2


class MathUtil:
  @staticmethod
  def random_vector2(min: float = 0.0, max: float = 1.0) -> Vector2:
    return Vector2(random.uniform(min, max), random.uniform(min, max))

  @staticmethod
  def random_direction_change() -> float:
    return random.uniform(-10.0, 10.0)
