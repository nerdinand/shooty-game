from typing import Optional

from pygame.math import Vector2

from .intersection import Intersection
from .obstacle import Obstacle


class IntersectionUtil:
    """Intersection algorithm for line sections and obstacles."""

    @staticmethod
    def find_intersections(
        point0: Vector2, point1: Vector2, obstacle: Obstacle
    ) -> list[Intersection]:
        """Find intersections between a line section and an obstacle.

        Arguments:
            point0 (Vector2): The first point of the line section.
            point1 (Vector2): The second point of the line section.
            obstacle (Obstacle): The obstacle to check for intersections with.

        Returns:
            list[Intersection]: A list of intersections between the line section and the obstacle.
        """
        intersections = []
        for (point2, point3) in obstacle.get_rectangle().all_sides:
            intersection_point = IntersectionUtil.find_intersection(
                point0, point1, point2, point3
            )
            if intersection_point is not None:
                intersections.append(Intersection(intersection_point, obstacle))
        return intersections

    @staticmethod
    def find_intersection(
        point0: Vector2, point1: Vector2, point2: Vector2, point3: Vector2
    ) -> Optional[Vector2]:
        """Find the intersection between two line sections.

        Arguments:
            point0 (Vector2): The first point of the first line section.
            point1 (Vector2): The second point of the first line section.
            point2 (Vector2): The first point of the second line section.
            point3 (Vector2): The second point of the second line section.

        Returns:
            Optional[Vector2]: A Vector2 indicating the intersection point
                if there is one, None otherwise.
        """
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
