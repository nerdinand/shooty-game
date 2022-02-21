from typing import Tuple
from typing import Type

from pygame.math import Vector2

from .gun import Gun
from .player import Player
from .player_type import PlayerType


class Agent(Player):
    def __init__(
        self, name: str, gun: Type[Gun], position: Tuple[float, float] = (0.5, 0.5)
    ) -> None:
        super().__init__(PlayerType.AGENT, name, Vector2(*position), gun)

    def update_move_direction(self, move_direction: Vector2) -> None:
        self.move_direction = move_direction