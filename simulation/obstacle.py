from .collision import Collision
from .entity import Entity
from .entity import EntityType
from .rectangle import Rectangle


class Obstacle(Entity):
    def __init__(  # pylint: disable=too-many-arguments
        self, name: str, left: float, top: float, width: float, height: float
    ) -> None:
        super().__init__()
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

    def get_entity_type(self) -> EntityType:
        return EntityType.OBSTACLE
