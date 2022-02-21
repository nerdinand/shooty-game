from __future__ import annotations  # to allow for forward type references

from enum import Enum
from typing import Protocol
from typing import runtime_checkable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .rectangle import Rectangle
    from .collision import Collision


class EntityType(Enum):
    OBSTACLE = 1
    PLAYER = 1


@runtime_checkable
class Entity(Protocol):
    def get_rectangle(self) -> Rectangle:
        raise NotImplementedError

    def hit(self, collision: Collision) -> None:
        raise NotImplementedError

    def get_name(self) -> str:
        raise NotImplementedError

    def get_entity_type(self) -> EntityType:
        raise NotImplementedError
