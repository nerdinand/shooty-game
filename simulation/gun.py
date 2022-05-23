from __future__ import annotations  # to allow for forward type references

from typing import List
from typing import TYPE_CHECKING

from pygame.math import Vector2

from .projectile import Projectile

if TYPE_CHECKING:
    from .player import Player  # pragma: no cover
    from .projectile_collider import ProjectileCollider  # pragma: no cover


class Gun:  # pylint: disable=too-many-instance-attributes
    """A gun (held by a player) that can shoot projectiles."""

    SPRAY_PATTERN_MODIFIER_STANDING = 2.0
    SPRAY_PATTERN_MODIFIER_MOVING = 8.0

    def __init__(  # pylint: disable=too-many-arguments
        self,
        player: Player,
        cooldown_ticks: int,
        magazine_size: int,
        maximum_damage: int,
        spray_pattern: List[float],
        reload_ticks: int,
    ) -> None:
        """Initialize a new Gun.

        Arguments:
            player (Player): The player holding the gun.
            cooldown_ticks (int): How many ticks a the gun takes until the next shot.
            magazine_size (int): How many bullets fit in a magazine.
            maximum_damage (int): The maximum amount of damage a bullet from this gun will do.
            spray_pattern (List[float]): The pattern of direction offsets when
                spraying (continuously shooting).
            reload_ticks (int): How long a reload takes (in ticks).
        """
        self.player = player
        self.cooldown_ticks = cooldown_ticks
        self.magazine_size = magazine_size
        self.maximum_damage = maximum_damage
        self.spray_pattern = spray_pattern
        self.reload_ticks = reload_ticks
        self.tick_count = -1
        self.spray_sequence = 0
        self.projectiles: List[Projectile] = []
        self.reload_tick_count = reload_ticks
        self.bullet_count = magazine_size
        self.is_reloading = False

    def tick(self, projectile_collider: ProjectileCollider) -> None:
        """Simulate a single "tick" (quantum of time).

        Arguments:
            projectile_collider (ProjectileCollider): The collider object to calculate collisions
                between projectiles and obstacles.
        """
        self.tick_count -= 1

        self.__reload_tick()

        for projectile in self.projectiles:
            projectile.tick(projectile_collider)
            if projectile.is_dead:
                self.projectiles.remove(projectile)

    def shoot(self) -> None:
        """Shoot the gun (if you can)."""
        if self.__can_shoot():
            self.__handle_spray_sequence()

            if self.player.is_moving:
                modifier = Gun.SPRAY_PATTERN_MODIFIER_MOVING
            else:
                modifier = Gun.SPRAY_PATTERN_MODIFIER_STANDING

            self.projectiles.append(
                Projectile(
                    self,
                    Vector2(self.player.position),
                    self.player.look_direction
                    + modifier * self.spray_pattern[self.spray_sequence],
                )
            )
            self.tick_count = self.cooldown_ticks
            self.bullet_count -= 1

    def start_reload(self) -> None:
        """Initiate reloading."""
        if self.is_reloading:
            return
        self.is_reloading = True

    def __handle_spray_sequence(self) -> None:
        if self.tick_count == 0:  # spraying
            self.spray_sequence += 1
        else:  # not spraying, reset sequence
            self.spray_sequence = 0

    def __reload_tick(self) -> None:
        if self.is_reloading:
            self.reload_tick_count -= 1
            if self.reload_tick_count == 0:
                self.is_reloading = False
                self.bullet_count = self.magazine_size
                self.reload_tick_count = self.reload_ticks

    def __can_shoot(self) -> bool:
        return (
            not self.player.is_dead  # pylint: disable=chained-comparison
            and self.tick_count <= 0
            and self.bullet_count > 0
            and not self.is_reloading
        )
