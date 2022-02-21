from __future__ import annotations  # to allow for forward type references

from typing import TYPE_CHECKING

from pygame.math import Vector2

if TYPE_CHECKING:
    from .gun import Gun
    from .projectile_collider import ProjectileCollider


class Projectile:
    VELOCITY = 1e-3

    def __init__(self, gun: Gun, position: Vector2, direction: float) -> None:
        self.gun = gun
        self.position = position
        self.direction = direction
        self.is_dead = False
        self.last_position = position

    def tick(self, collider: ProjectileCollider) -> None:
        self.last_position = Vector2(self.position)
        vector = Vector2()
        vector.from_polar((Projectile.VELOCITY, self.direction))
        self.position += vector

        if collider.apply_collision_effect(self):
            self.is_dead = True

    def maximum_damage(self) -> int:
        return self.gun.maximum_damage
