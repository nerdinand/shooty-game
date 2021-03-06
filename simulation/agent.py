from typing import Tuple
from typing import Type

from pygame.math import Vector2

from .gun import Gun
from .player import Player
from .player_type import PlayerType


class Agent(Player):
    """Represents an AI agent in the Simulation (a type of Player)."""

    def __init__(
        self,
        name: str,
        gun_class: Type[Gun],
        position: Tuple[float, float] = (0.5, 0.5),
    ) -> None:
        """Initialize the Agent."""
        super().__init__(PlayerType.AGENT, name, Vector2(*position), gun_class)
