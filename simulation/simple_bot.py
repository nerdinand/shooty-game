from typing import Type

from pygame.math import Vector2

from .bot import Bot
from .gun import Gun
from .math_util import MathUtil
from .player_collider import PlayerCollider
from .player_type import PlayerType
from .projectile_collider import ProjectileCollider


class SimpleBot(Bot):
    """A bot that behaves really stupidly."""

    def __init__(
        self, name: str, gun_class: Type[Gun], position: Vector2 = Vector2(0.5, 0.5)
    ) -> None:
        super().__init__(PlayerType.BOT, name, position, gun_class)

    def tick(
        self, player_collider: PlayerCollider, projectile_collider: ProjectileCollider
    ) -> None:
        if not self.is_dead:
            self.move_direction += MathUtil.random_vector2(minimum=-1.0, maximum=1.0)
            self.look_direction += MathUtil.random_direction_change()

            if MathUtil.random_float() < 0.001:
                self.gun.shoot()

        super().tick(player_collider, projectile_collider)
