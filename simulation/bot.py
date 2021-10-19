from pygame.math import Vector2
from .player import Player
from .player_type import PlayerType
from .math_util import MathUtil


class Bot(Player):
  def __init__(self, position=Vector2(0.5, 0.5)):
    super().__init__(PlayerType.BOT, position)

  def tick(self, collider):
    self.move_direction += MathUtil.random_vector2(min=-1.0, max=1.0)
    self.look_direction += MathUtil.random_direction_change()
    super().tick(collider)
