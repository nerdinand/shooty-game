import random
from pygame.math import Vector2


class MathUtil:
  def random_vector2(min=0.0, max=1.0):
    return Vector2(random.uniform(min, max), random.uniform(min, max))  
  
  def random_direction_change():
    return random.uniform(-10.0, 10.0)
