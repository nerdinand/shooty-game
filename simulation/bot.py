from pygame.math import Vector2
import random

from .player import Player
from .player_type import PlayerType
from .math_util import MathUtil


class Bot(Player):
  def __init__(self, gun, position=Vector2(0.5, 0.5)):
    super().__init__(PlayerType.BOT, position, gun)

  def tick(self, player_collider, projectile_collider):
    if not self.is_dead:
      self.move_direction += MathUtil.random_vector2(min=-1.0, max=1.0)
      self.look_direction += MathUtil.random_direction_change()

      if random.random() < 0.001:
        self.gun.shoot()

    super().tick(player_collider, projectile_collider)
