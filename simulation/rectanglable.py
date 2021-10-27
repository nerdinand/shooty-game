from typing import Protocol, runtime_checkable

from .rectangle import Rectangle


@runtime_checkable
class Rectanglable(Protocol):
  def get_rectangle(self) -> Rectangle:
    pass

  def apply_damage(self, amount: int) -> None:
    pass

  def get_name(self) -> str:
    pass
