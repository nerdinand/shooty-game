from typing import Type

from pygame.math import Vector2

from .bot import Bot
from .gun import Gun
from .player_type import PlayerType


class StaticBot(Bot):
    """A bot that just does nothing."""

    def __init__(
        self, name: str, gun_class: Type[Gun], position: Vector2 = Vector2(0.5, 0.5)
    ) -> None:
        super().__init__(PlayerType.BOT, name, position, gun_class)
