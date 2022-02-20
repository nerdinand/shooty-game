import random
from typing import Type

from pygame.math import Vector2

from .math_util import MathUtil
from .player import Player
from .player_collider import PlayerCollider
from .player_type import PlayerType
from .projectile_collider import ProjectileCollider


class Bot(Player):
    def __init__(self, name: str, gun: Type, position: Vector2 = Vector2(0.5, 0.5)):
        super().__init__(PlayerType.BOT, name, position, gun)

    def tick(
        self, player_collider: PlayerCollider, projectile_collider: ProjectileCollider
    ) -> None:
        if not self.is_dead:
            self.move_direction += MathUtil.random_vector2(minimum=-1.0, maximum=1.0)
            self.look_direction += MathUtil.random_direction_change()

            if random.random() < 0.001:
                self.gun.shoot()

        super().tick(player_collider, projectile_collider)
