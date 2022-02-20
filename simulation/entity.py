from __future__ import annotations  # to allow for forward type references

from enum import Enum
from typing import Protocol
from typing import runtime_checkable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rectangle import Rectangle
    from .collision import Collision


class EntityType(Enum):
    NONE, OBSTACLE, PLAYER = range(3)


@runtime_checkable
class Entity(Protocol):
    def get_rectangle(self) -> Rectangle:
        pass

    def hit(self, collision: Collision) -> None:
        pass

    def get_name(self) -> str:
        pass

    def type(self) -> EntityType:
        pass
