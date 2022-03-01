from __future__ import annotations  # to allow for forward type references

from typing import TYPE_CHECKING

from pygame.math import Vector2

from .projectile import Projectile

if TYPE_CHECKING:
    from .intersection import Intersection


class Collision:
    def __init__(self, projectile: Projectile, intersection: Intersection) -> None:
        self.projectile = projectile
        self.intersection = intersection

    def distance_from(self, vector: Vector2) -> float:
        return self.intersection.position.distance_to(vector)

    def apply_effect(self) -> None:
        self.intersection.obstacle.hit(self)
