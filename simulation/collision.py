class Collision:
  def __init__(self, projectile, body, intersection):
    self.projectile = projectile
    self.body = body
    self.intersection = intersection
  
  def distance_from(self, vector):
    return self.intersection.distance_to(vector)

  def apply_effect(self):
    self.body.apply_damage(self.projectile.damage())
