from pygame.math import Vector2

from simulation.rectangle import Rectangle
from simulation.intersection_util import IntersectionUtil


class TestIntersectionUtil:
  class TestRectanglable:
    def get_rectangle(self) -> Rectangle:
      return Rectangle(2.0, 2.0, 2.0, 1.0)

    def apply_damage(self, amount: int) -> None:
      pass

    def get_name(self) -> str:
      return "Test rectanglable"

  def test_find_intersections_ray_vertically_down_middle(self) -> None:
    rectanglable = TestIntersectionUtil.TestRectanglable()
    intersections = IntersectionUtil.find_intersections(
      Vector2(3.0, 0.0), Vector2(3.0, 5.0), rectanglable
    )
    assert(len(intersections) == 2)
    assert(intersections[0].position == Vector2(3.0, 2.0))
    assert(intersections[1].position == Vector2(3.0, 3.0))
    assert(intersections[0].rectanglable is rectanglable)
    assert(intersections[1].rectanglable is rectanglable)

  def test_find_intersections_ray_vertically_down_left_side(self) -> None:
    rectanglable = TestIntersectionUtil.TestRectanglable()
    intersections = IntersectionUtil.find_intersections(
      Vector2(2.0, 0.0), Vector2(2.0, 5.0), rectanglable
    )
    assert(len(intersections) == 2)
    assert(intersections[0].position == Vector2(2.0, 2.0))
    assert(intersections[1].position == Vector2(2.0, 3.0))
    assert(intersections[0].rectanglable is rectanglable)
    assert(intersections[1].rectanglable is rectanglable)

  def test_find_intersections_ray_horizontally_across_middle(self) -> None:
    rectanglable = TestIntersectionUtil.TestRectanglable()
    intersections = IntersectionUtil.find_intersections(
      Vector2(0.0, 2.5), Vector2(5.0, 2.5), rectanglable
    )
    assert(len(intersections) == 2)
    assert(intersections[0].position == Vector2(2.0, 2.5))
    assert(intersections[1].position == Vector2(4.0, 2.5))
    assert(intersections[0].rectanglable is rectanglable)
    assert(intersections[1].rectanglable is rectanglable)

  def test_find_intersections_ray_horizontally_across_bottom(self) -> None:
    rectanglable = TestIntersectionUtil.TestRectanglable()
    intersections = IntersectionUtil.find_intersections(
      Vector2(0.0, 3.0), Vector2(5.0, 3.0), rectanglable
    )
    assert(len(intersections) == 2)
    assert(intersections[0].position == Vector2(2.0, 3.0))
    assert(intersections[1].position == Vector2(4.0, 3.0))
    assert(intersections[0].rectanglable is rectanglable)
    assert(intersections[1].rectanglable is rectanglable)
