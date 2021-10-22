from pygame.math import Vector2

from .projectile import Projectile
from .rectanglable import Rectanglable


class Collision:
  def __init__(self, projectile: Projectile, rectanglable: Rectanglable, intersection: Vector2):
    self.projectile = projectile
    self.rectanglable = rectanglable
    self.intersection = intersection

  def distance_from(self, vector: Vector2) -> float:
    return self.intersection.distance_to(vector)

  def apply_effect(self) -> None:
    self.rectanglable.apply_damage(self.projectile.damage())
