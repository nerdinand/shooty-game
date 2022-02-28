from __future__ import annotations  # to allow for forward type references

from typing import TYPE_CHECKING

from pygame.math import Vector2

from .entity import Entity

if TYPE_CHECKING:
    from .player import Player  # pragma: no cover


class Intersection:
    def __init__(self, position: Vector2, entity: Entity) -> None:
        self.position = position
        self.entity = entity


class NoneIntersection(Intersection):
    def __init__(self, player: Player) -> None:
        super().__init__(Vector2(), player)
