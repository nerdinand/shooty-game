import random
from typing import Type

from pygame.math import Vector2

from .player import Player
from .human import Human
from .player_type import PlayerType
from .math_util import MathUtil
from .gun import Gun
from .player_collider import PlayerCollider
from .projectile_collider import ProjectileCollider


class Agent(Player):
  def __init__(self, name: str, gun: Type, position: Vector2 = Vector2(0.5, 0.5)):
    super().__init__(PlayerType.AGENT, name, position, gun)

  def update_move_direction(self, move_direction: Vector2) -> None:
    self.move_direction = move_direction

  def tick(self, player_collider: PlayerCollider, projectile_collider: ProjectileCollider) -> None:
    super().tick(player_collider, projectile_collider)
