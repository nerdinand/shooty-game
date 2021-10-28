from pygame.math import Vector2

from .projectile import Projectile
from .intersection import Intersection


class Collision:
  def __init__(self, projectile: Projectile, intersection: Intersection):
    self.projectile = projectile
    self.intersection = intersection

  def distance_from(self, vector: Vector2) -> float:
    return self.intersection.position.distance_to(vector)

  def apply_effect(self) -> None:
    self.intersection.entity.hit(self)
