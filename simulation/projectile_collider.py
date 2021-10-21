from pygame.math import Vector2

from .collision import Collision


class ProjectileCollider:
  def __init__(self, simulation):
    self.simulation = simulation

  def apply_collision_effect(self, projectile):
    collisions = self.__projectile_collisions(projectile)
    if len(collisions) == 0:
      return False

    first_collision = sorted(
      collisions,
      key=lambda collision: collision.distance_from(projectile.last_position)
    )[0]
    first_collision.apply_effect()
    return True

  def __projectile_collisions(self, projectile):
    collisions = []
    for player in self.simulation.players:
      # can't shoot myself or dead players
      if player == projectile.gun.player or player.is_dead:
        continue
      collisions += self.__find_collisions(projectile, player)

    for obstacle in self.simulation.map.obstacles:
      collisions += self.__find_collisions(projectile, obstacle)

    return collisions

  def __find_collisions(self, projectile, obstacle):
    collisions = []
    line_start = projectile.last_position
    line_end = projectile.position
    for (p2, p3) in obstacle.bounding_box().all_sides:
      intersection = self.__intersection(line_start, line_end, p2, p3)
      if intersection is not None:
        collisions.append(Collision(projectile, obstacle, intersection))

    return collisions

  def __intersection(self, p0, p1, p2, p3):
    s1 = p1 - p0
    s2 = p3 - p2
    divisor = s1.cross(s2)

    if divisor == 0:
      return None

    s = (-s1.y * (p0.x - p2.x) + s1.x * (p0.y - p2.y)) / divisor
    t = (s2.x * (p0.y - p2.y) + s2.y * (p0.x - p2.x)) / divisor

    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
      return Vector2(p0.x + (t * s1.x), p0.y + (t * s1.y))
    else:
      return None
