from pygame.math import Vector2

from .entity import Entity


class Intersection:
    def __init__(self, position: Vector2, entity: Entity):
        self.position = position
        self.entity = entity
