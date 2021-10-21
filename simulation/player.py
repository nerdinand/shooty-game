from .gun import Gun
from pygame.math import Vector2

from .obstacle import Obstacle


class Player:
  EXTENT = 0.03

  PLAYER_ACCELERATION = 0.00001
  PLAYER_ACCELERATION_DAMPENING = 0.9

  MAX_VELOCITY = 1e-4
  MAX_VELOCITY_SQUARED = MAX_VELOCITY * MAX_VELOCITY

  MAX_HEALTH = 100

  def __init__(self, player_type, position, gun_class):
    self.player_type = player_type
    self.position = position
    self.move_direction = Vector2(0, 0)
    self.velocity = Vector2(0.0, 0.0)
    self.look_direction = 0.0
    self.gun = gun_class(self)
    self.is_dead = False
    self.health = Player.MAX_HEALTH

  def extent(self):
    return Player.EXTENT

  def radius(self):
    return self.extent() / 2.0

  def update_look_direction(self, look_direction):
    if not self.is_dead:
      self.look_direction = look_direction

  def tick(self, player_collider, projectile_collider):
    if not self.is_dead:
      self.__update_velocity()
      player_collider.move(self)
    self.gun.tick(projectile_collider)

  def bounding_box(self):
    half_extent = self.extent() / 2.0
    top = self.position.x - half_extent
    left = self.position.y - half_extent
    return Obstacle(top, left, self.extent(), self.extent())

  def apply_damage(self, amount):
    self.health -= amount
    if self.health <= 0:
      self.is_dead = True

  def __update_velocity(self):
    if self.move_direction == Vector2(0.0, 0.0):
      self.velocity *= Player.PLAYER_ACCELERATION_DAMPENING
    else:
      self.velocity += self.move_direction * Player.PLAYER_ACCELERATION

    if self.velocity.length_squared() > Player.MAX_VELOCITY_SQUARED:
      self.velocity.scale_to_length(Player.MAX_VELOCITY)
