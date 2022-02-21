from pygame.math import Vector2

from simulation.collision import Collision
from simulation.intersection_util import IntersectionUtil
from simulation.rectangle import Rectangle
from simulation.entity import Entity


class TestIntersectionUtil:
    class TestEntity(Entity):
        def get_rectangle(self) -> Rectangle:
            return Rectangle(2.0, 2.0, 2.0, 1.0)

        def hit(self, collision: Collision) -> None:
            pass

        def get_name(self) -> str:
            return "Test entity"

    def test_find_intersections_ray_vertically_down_middle(self) -> None:
        entity = TestIntersectionUtil.TestEntity()
        intersections = IntersectionUtil.find_intersections(
            Vector2(3.0, 0.0), Vector2(3.0, 5.0), entity
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(3.0, 2.0)
        assert intersections[1].position == Vector2(3.0, 3.0)
        assert intersections[0].entity is entity
        assert intersections[1].entity is entity

    def test_find_intersections_ray_vertically_down_left_side(self) -> None:
        entity = TestIntersectionUtil.TestEntity()
        intersections = IntersectionUtil.find_intersections(
            Vector2(2.0, 0.0), Vector2(2.0, 5.0), entity
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 2.0)
        assert intersections[1].position == Vector2(2.0, 3.0)
        assert intersections[0].entity is entity
        assert intersections[1].entity is entity

    def test_find_intersections_ray_horizontally_across_middle(self) -> None:
        entity = TestIntersectionUtil.TestEntity()
        intersections = IntersectionUtil.find_intersections(
            Vector2(0.0, 2.5), Vector2(5.0, 2.5), entity
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 2.5)
        assert intersections[1].position == Vector2(4.0, 2.5)
        assert intersections[0].entity is entity
        assert intersections[1].entity is entity

    def test_find_intersections_ray_horizontally_across_bottom(self) -> None:
        entity = TestIntersectionUtil.TestEntity()
        intersections = IntersectionUtil.find_intersections(
            Vector2(0.0, 3.0), Vector2(5.0, 3.0), entity
        )
        assert len(intersections) == 2
        assert intersections[0].position == Vector2(2.0, 3.0)
        assert intersections[1].position == Vector2(4.0, 3.0)
        assert intersections[0].entity is entity
        assert intersections[1].entity is entity
