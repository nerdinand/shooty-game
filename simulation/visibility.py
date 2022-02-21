from typing import cast
from typing import Optional

from pygame.math import Vector2

from .intersection import Intersection
from .intersection import NoneIntersection
from .intersection_util import IntersectionUtil
from .obstacle import Obstacle
from .player import Player
from .simulation import Simulation


class Visibility:
    RAY_INTERVAL = 1.0
    RAY_LENGTH = 2.0
    NUMBER_OF_RAYS = 61

    @classmethod
    def get_visible_points(
        cls, simulation: Simulation, player: Player
    ) -> list[Intersection]:
        left_angle = player.get_left_fov_angle()
        visible_points: list[Intersection] = []

        angle_interval = Player.FOV_ANGLE / Visibility.NUMBER_OF_RAYS

        for i in range(Visibility.NUMBER_OF_RAYS):
            ray_angle = left_angle + i * angle_interval
            visible_point = Visibility.__cast_ray(ray_angle, simulation, player)
            if visible_point is not None:
                visible_points.append(visible_point)
            else:
                visible_points.append(NoneIntersection(player))

        return visible_points

    @classmethod
    def __cast_ray(
        cls, ray_angle: float, simulation: Simulation, player: Player
    ) -> Optional[Intersection]:
        ray_start_point = player.position
        vector = Vector2()
        vector.from_polar((Visibility.RAY_LENGTH, ray_angle))
        ray_end_point = ray_start_point + vector

        intersections = []
        obstacles: list[Obstacle] = simulation.map.obstacles + cast(
            list[Obstacle], simulation.players
        )
        for obstacle in obstacles:
            if obstacle == player:
                continue
            intersections += IntersectionUtil.find_intersections(
                ray_start_point, ray_end_point, obstacle
            )

        if len(intersections) == 0:
            return None

        first_intersection = sorted(
            intersections,
            key=lambda intersection: intersection.position.distance_to(ray_start_point),
        )[0]

        return first_intersection
