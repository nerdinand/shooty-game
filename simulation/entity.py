from __future__ import annotations  # to allow for forward type references
from typing import Protocol, runtime_checkable, TYPE_CHECKING

if TYPE_CHECKING:
  from .rectangle import Rectangle
  from .collision import Collision


@runtime_checkable
class Entity(Protocol):
  def get_rectangle(self) -> Rectangle:
    pass

  def hit(self, collision: Collision) -> None:
    pass

  def get_name(self) -> str:
    pass
