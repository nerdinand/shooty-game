from __future__ import annotations  # to allow for forward type references
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
  from .projectile import Projectile
  from .simulation import Simulation
from .entity import Entity
from .collision import Collision
from .intersection_util import IntersectionUtil


class ProjectileCollider:
  def __init__(self, simulation: Simulation):
    self.simulation = simulation

  def apply_collision_effect(self, projectile: Projectile) -> bool:
    collisions = self.__projectile_collisions(projectile)
    if len(collisions) == 0:
      return False

    first_collision = sorted(
      collisions,
      key=lambda collision: collision.distance_from(projectile.last_position)
    )[0]
    first_collision.apply_effect()
    return True

  def __projectile_collisions(self, projectile: Projectile) -> List[Collision]:
    collisions = []
    for player in self.simulation.players:
      # can't shoot myself or dead players
      if player == projectile.gun.player or player.is_dead:
        continue
      collisions += self.__find_collisions(projectile, player)

    for obstacle in self.simulation.map.obstacles:
      collisions += self.__find_collisions(projectile, obstacle)

    return collisions

  def __find_collisions(
    self, projectile: Projectile, game_object: Entity
  ) -> List[Collision]:
    line_start = projectile.last_position
    line_end = projectile.position
    intersections = IntersectionUtil.find_intersections(line_start, line_end, game_object)
    return [Collision(projectile, intersection) for intersection in intersections]
