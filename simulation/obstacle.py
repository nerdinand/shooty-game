from .collision import Collision
from .entity import EntityType
from .rectangle import Rectangle


class Obstacle:
    def __init__(
        self, name: str, left: float, top: float, width: float, height: float
    ):  # pylint: disable=too-many-arguments
        self.name = name
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def get_rectangle(self) -> Rectangle:
        return Rectangle(self.left, self.top, self.width, self.height)

    def get_name(self) -> str:
        return self.name

    def hit(self, collision: Collision) -> None:
        pass

    def type(self) -> EntityType:  # pylint: disable=no-self-use
        return EntityType.OBSTACLE
