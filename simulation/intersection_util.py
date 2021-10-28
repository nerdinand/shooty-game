from typing import Optional

from pygame.math import Vector2

from .entity import Entity
from .intersection import Intersection


class IntersectionUtil:
  @staticmethod
  def find_intersections(
    p0: Vector2, p1: Vector2, entity: Entity
  ) -> list[Intersection]:
    intersections = []
    for (p2, p3) in entity.get_rectangle().all_sides:
      intersection_point = IntersectionUtil.find_intersection(p0, p1, p2, p3)
      if intersection_point is not None:
        intersections.append(Intersection(intersection_point, entity))
    return intersections

  @staticmethod
  def find_intersection(p0: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> Optional[Vector2]:
    s1 = p1 - p0
    s2 = p3 - p2
    divisor = s1.cross(s2)

    if divisor == 0:
      return None

    s = (-s1.y * (p0.x - p2.x) + s1.x * (p0.y - p2.y)) / divisor  # type: ignore[operator]
    t = (s2.x * (p0.y - p2.y) - s2.y * (p0.x - p2.x)) / divisor  # type: ignore[operator]

    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
      return Vector2(p0.x + (t * s1.x), p0.y + (t * s1.y))
    else:
      return None
