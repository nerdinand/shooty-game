from pygame.math import Vector2
from .player import Player
from .player_type import PlayerType

class Human(Player):
  def __init__(self, gun, position=Vector2(0.5, 0.5)):
    super().__init__(PlayerType.HUMAN, position, gun)

  def update_move_direction(self, move_direction):
    self.move_direction = move_direction

  def tick(self, player_collider, projectile_collider):
    super().tick(player_collider, projectile_collider)
