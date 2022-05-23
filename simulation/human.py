from typing import Type

from pygame.math import Vector2

from .gun import Gun
from .player import Player
from .player_type import PlayerType


class Human(Player):
    """A player that can be controlled through the keyboard."""

    def __init__(
        self, name: str, gun_class: Type[Gun], position: Vector2 = Vector2(0.5, 0.5)
    ) -> None:
        """Initialize the Human.

        Arguments:
            name (str): The name of the player.
            gun_class (Type[Gun]): The class to use to initialise this players gun with.
            position (optional, Vector2): The initial position of the player.
        """
        super().__init__(PlayerType.HUMAN, name, position, gun_class)
