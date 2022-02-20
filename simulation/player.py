from typing import Type

from pygame.math import Vector2

from .collision import Collision
from .entity import EntityType
from .player_collider import PlayerCollider
from .player_type import PlayerType
from .projectile_collider import ProjectileCollider
from .rectangle import Rectangle


class Player:  # pylint: disable=too-many-instance-attributes
    EXTENT = 0.03

    PLAYER_ACCELERATION = 0.00001
    PLAYER_ACCELERATION_DAMPENING = 0.9

    MAX_VELOCITY = 1e-4
    MAX_VELOCITY_SQUARED = MAX_VELOCITY * MAX_VELOCITY
    MIN_VELOCITY_THRESHOLD = 0.00001
    MIN_VELOCITY_THRESHOLD_SQUARED = MIN_VELOCITY_THRESHOLD * MIN_VELOCITY_THRESHOLD

    MAX_HEALTH = 100

    FOV_ANGLE = 60

    def __init__(self, player_type: str, name: str, position: Vector2, gun_class: Type):
        self.player_type = player_type
        self.name = name
        self.position = position
        self.gun = gun_class(self)
        self.move_direction = Vector2(0, 0)
        self.velocity = Vector2(0.0, 0.0)
        self.look_direction = 0.0
        self.is_dead = False
        self.is_moving = False
        self.health = Player.MAX_HEALTH
        self.extent = Player.EXTENT
        self.radius = self.extent / 2.0

    def get_name(self) -> str:
        return self.name

    def get_left_fov_angle(self) -> float:
        return self.look_direction - Player.FOV_ANGLE / 2

    def get_right_fov_angle(self) -> float:
        return self.look_direction + Player.FOV_ANGLE / 2

    def get_rectangle(self) -> Rectangle:
        half_extent = self.extent / 2.0
        top = self.position.x - half_extent
        left = self.position.y - half_extent
        return Rectangle(top, left, self.extent, self.extent)

    def update_look_direction(self, look_direction: float) -> None:
        if not self.is_dead:
            self.look_direction = look_direction

    def tick(
        self, player_collider: PlayerCollider, projectile_collider: ProjectileCollider
    ) -> None:
        if not self.is_dead:
            self.__update_velocity()
            player_collider.move(self)
        self.gun.tick(projectile_collider)

    def hit(self, collision: Collision) -> None:
        factor = self.radius / collision.distance_from(self.position)
        damage = int(collision.projectile.maximum_damage() * (factor**2))
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True

    def is_human(self) -> bool:
        return self.player_type == PlayerType.HUMAN

    def __update_velocity(self) -> None:
        self.is_moving = True
        if self.move_direction == Vector2(0.0, 0.0):
            self.velocity *= Player.PLAYER_ACCELERATION_DAMPENING
        else:
            self.velocity += self.move_direction * Player.PLAYER_ACCELERATION

        length_squared = self.velocity.length_squared()
        if length_squared > Player.MAX_VELOCITY_SQUARED:
            self.velocity.scale_to_length(Player.MAX_VELOCITY)
        elif length_squared < Player.MIN_VELOCITY_THRESHOLD_SQUARED:
            self.velocity = Vector2(0.0, 0.0)
            self.is_moving = False

    def type(self) -> EntityType:  # pylint: disable=no-self-use
        return EntityType.PLAYER
