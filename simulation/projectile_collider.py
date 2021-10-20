from pygame.math import Vector2

class ProjectileCollider:
  def __init__(self, simulation):
    self.simulation = simulation

  def projectile_collided(self, projectile):
    line_start = projectile.last_position
    line_end = projectile.position

    for player in self.simulation.players:
      if player == projectile.gun.player: # can't shoot myself
        continue
      for (p2, p3) in player.bounding_box().all_sides:
        if self.__do_intersect(line_start, line_end, p2, p3):
          return True

    for obstacle in self.simulation.map.obstacles:
      for (p2, p3) in obstacle.all_sides:
        if self.__do_intersect(line_start, line_end, p2, p3):
          return True

  def __do_intersect(self, p0, p1, p2, p3):
    s1 = p1 - p0
    s2 = p3 - p2
    divisor = s1.cross(s2)

    if divisor == 0:
      return None

    s = (-s1.y * (p0.x - p2.x) + s1.x * (p0.y - p2.y)) / divisor
    t = ( s2.x * (p0.y - p2.y) + s2.y * (p0.x - p2.x)) / divisor

    if s >= 0 and s <= 1 and t >= 0 and t <= 1:
      return Vector2(p0.x + (t * s1.x), p0.y + (t * s1.y))
    else:
      return None

