from __future__ import annotations  # to allow for forward type references

from typing import TYPE_CHECKING

from pygame.math import Vector2

from .projectile import Projectile

if TYPE_CHECKING:
    from .intersection import Intersection


class Collision:
    """Represents a collision of a projectile."""

    def __init__(self, projectile: Projectile, intersection: Intersection) -> None:
        """Initialize a new Collision.

        Arguments:
            projectile (Projectile): The projectile that is colliding.
            intersection (Intersection): The place where it is colliding.
        """
        self.projectile = projectile
        self.intersection = intersection

    def distance_from(self, vector: Vector2) -> float:
        """Calculate the distance between a vector and the collision.

        Arguments:
            vector (Vector2): The vector from where to calculate the distance.

        Returns:
            (float) The distance between the vector and this collision.
        """
        return self.intersection.position.distance_to(vector)

    def apply_effect(self) -> None:
        """Apply the effect of this collision."""
        self.intersection.obstacle.hit(self)
