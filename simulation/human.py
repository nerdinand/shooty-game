from typing import Type

from pygame.math import Vector2

from .player import Player
from .player_type import PlayerType


class Human(Player):
    def __init__(self, name: str, gun: Type, position: Vector2 = Vector2(0.5, 0.5)):
        super().__init__(PlayerType.HUMAN, name, position, gun)

    def update_move_direction(self, move_direction: Vector2) -> None:
        self.move_direction = move_direction
