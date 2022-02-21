from typing import Optional

from pygame.math import Vector2

from .entity import Entity
from .intersection import Intersection


class IntersectionUtil:
    @staticmethod
    def find_intersections(
        point0: Vector2, point1: Vector2, entity: Entity
    ) -> list[Intersection]:
        intersections = []
        for (point2, point3) in entity.get_rectangle().all_sides:
            intersection_point = IntersectionUtil.find_intersection(
                point0, point1, point2, point3
            )
            if intersection_point is not None:
                intersections.append(Intersection(intersection_point, entity))
        return intersections

    @staticmethod
    def find_intersection(
        point0: Vector2, point1: Vector2, point2: Vector2, point3: Vector2
    ) -> Optional[Vector2]:
        s1 = point1 - point0  # pylint: disable=invalid-name
        s2 = point3 - point2  # pylint: disable=invalid-name
        divisor = s1.cross(s2)

        if divisor == 0:
            return None

        s = (  # pylint: disable=invalid-name
            -s1.y * (point0.x - point2.x) + s1.x * (point0.y - point2.y)
        ) / divisor  # pyre-ignore[58]
        t = (  # pylint: disable=invalid-name
            s2.x * (point0.y - point2.y) - s2.y * (point0.x - point2.x)
        ) / divisor  # pyre-ignore[58]

        if 0 <= s <= 1 and 0 <= t <= 1:
            return Vector2(point0.x + (t * s1.x), point0.y + (t * s1.y))

        return None
