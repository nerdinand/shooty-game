from pygame.math import Vector2

from simulation.collision import Collision
from simulation.intersection_util import IntersectionUtil
from simulation.rectangle import Rectangle
from simulation.obstacle import Obstacle


class TestIntersectionUtil:
    OBSTACLE: Obstacle = Obstacle.fixed("Test obstacle", 2.0, 2.0, 2.0, 1.0)

    def test_find_intersections_ray_vertically_down_middle(self) -> None:
        obstacle = TestIntersectionUtil.OBSTACLE
        intersections = IntersectionUtil.find_intersections(
            Vector2(3.0, 0.0), Vector2(3.0, 5.0), obstacle
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(3.0, 2.0)
        assert intersections[1].position == Vector2(3.0, 3.0)
        assert intersections[0].obstacle is obstacle
        assert intersections[1].obstacle is obstacle

    def test_find_intersections_ray_vertically_down_left_side(self) -> None:
        obstacle = TestIntersectionUtil.OBSTACLE
        intersections = IntersectionUtil.find_intersections(
            Vector2(2.0, 0.0), Vector2(2.0, 5.0), obstacle
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 2.0)
        assert intersections[1].position == Vector2(2.0, 3.0)
        assert intersections[0].obstacle is obstacle
        assert intersections[1].obstacle is obstacle

    def test_find_intersections_ray_horizontally_across_middle(self) -> None:
        obstacle = TestIntersectionUtil.OBSTACLE
        intersections = IntersectionUtil.find_intersections(
            Vector2(0.0, 2.5), Vector2(5.0, 2.5), obstacle
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 2.5)
        assert intersections[1].position == Vector2(4.0, 2.5)
        assert intersections[0].obstacle is obstacle
        assert intersections[1].obstacle is obstacle

    def test_find_intersections_ray_horizontally_across_bottom(self) -> None:
        obstacle = TestIntersectionUtil.OBSTACLE
        intersections = IntersectionUtil.find_intersections(
            Vector2(0.0, 3.0), Vector2(5.0, 3.0), obstacle
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 3.0)
        assert intersections[1].position == Vector2(4.0, 3.0)
        assert intersections[0].obstacle is obstacle
        assert intersections[1].obstacle is obstacle
