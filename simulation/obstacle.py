from typing import Optional

from .collision import Collision
from .rectangle import Rectangle


class Obstacle:
    def __init__(self, name: str, rectangle: Optional[Rectangle] = None) -> None:
        self.name = name
        self.rectangle = rectangle

    @classmethod
    def fixed(  # pylint: disable=too-many-arguments
        cls, name: str, left: float, top: float, width: float, height: float
    ) -> "Obstacle":
        rectangle = Rectangle(left, top, width, height)
        return cls(name, rectangle)

    def get_rectangle(self) -> Rectangle:
        if self.rectangle is None:
            raise ValueError("self.rectangle is not supposed to be None here!")
        return self.rectangle

    def hit(self, collision: Collision) -> None:
        pass

    def get_name(self) -> str:
        return self.name
