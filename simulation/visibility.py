from typing import Optional

from pygame.math import Vector2

from .simulation import Simulation
from .intersection import Intersection
from .player import Player
from .intersection_util import IntersectionUtil


class Visibility:
  RAY_INTERVAL = 1.0
  RAY_LENGTH = 2.0

  def get_visible_points(self, simulation: Simulation, player: Player) -> list[Intersection]:
    ray_angle = player.get_left_fov_angle()
    right_fov_angle = player.get_right_fov_angle()
    visible_points: list[Intersection] = []

    while ray_angle <= right_fov_angle:
      visible_point = self.__cast_ray(ray_angle, simulation, player)
      if visible_point is not None:
        visible_points.append(visible_point)
      ray_angle += Visibility.RAY_INTERVAL

    return visible_points

  def __cast_ray(
    self, ray_angle: float, simulation: Simulation, player: Player
  ) -> Optional[Intersection]:
    ray_start_point = player.position
    v = Vector2()
    v.from_polar((Visibility.RAY_LENGTH, ray_angle))
    ray_end_point = ray_start_point + v

    intersections = []
    for obstacle in (simulation.map.obstacles + simulation.players):  # type: ignore[operator]
      if obstacle == player:
        continue
      intersections += IntersectionUtil.find_intersections(ray_start_point, ray_end_point, obstacle)

    if len(intersections) == 0:
      return None

    first_intersection = sorted(
      intersections,
      key=lambda intersection: intersection.position.distance_to(ray_start_point)
    )[0]

    return first_intersection
