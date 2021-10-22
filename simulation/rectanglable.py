from typing import Protocol

from .rectangle import Rectangle


class Rectanglable(Protocol):
  def get_rectangle(self) -> Rectangle:
    pass

  def apply_damage(self, amount: int) -> None:
    pass
