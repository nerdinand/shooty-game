from __future__ import annotations  # to allow for forward type references

from typing import TYPE_CHECKING

from pygame.math import Vector2

from .obstacle import Obstacle

if TYPE_CHECKING:
    from .player import Player  # pragma: no cover


class Intersection:
    def __init__(self, position: Vector2, obstacle: Obstacle) -> None:
        self.position = position
        self.obstacle = obstacle

    def __str__(self) -> str:
        return f"Intersection({self.obstacle.name})"


class NoneIntersection(Intersection):
    def __init__(self, player: Player) -> None:
        super().__init__(Vector2(), obstacle=player)

    def __str__(self) -> str:
        return "NoneIntersection"
