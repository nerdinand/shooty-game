from typing import List
from typing import Tuple

from pygame.math import Vector2


class Rectangle:
    def __init__(self, left: float, top: float, width: float, height: float):
        self.left_top = Vector2(left, top)
        self.width = width
        self.height = height
        self.all_sides = self.__all_sides()

    def top(self) -> float:
        return self.left_top.y

    def left(self) -> float:
        return self.left_top.x

    def bottom(self) -> float:
        return self.top() + self.height

    def right(self) -> float:
        return self.left() + self.width

    def __left_bottom(self) -> Vector2:
        return Vector2(self.left(), self.bottom())

    def __right_top(self) -> Vector2:
        return Vector2(self.right(), self.top())

    def __right_bottom(self) -> Vector2:
        return Vector2(self.right(), self.bottom())

    def __left_side(self) -> Tuple[Vector2, Vector2]:
        return (self.left_top, self.__left_bottom())

    def __right_side(self) -> Tuple[Vector2, Vector2]:
        return (self.__right_top(), self.__right_bottom())

    def __top_side(self) -> Tuple[Vector2, Vector2]:
        return (self.left_top, self.__right_top())

    def __bottom_side(self) -> Tuple[Vector2, Vector2]:
        return (self.__left_bottom(), self.__right_bottom())

    def __all_sides(self) -> List[Tuple[Vector2, Vector2]]:
        return [
            self.__left_side(),
            self.__right_side(),
            self.__top_side(),
            self.__bottom_side(),
        ]

    def __str__(self) -> str:
        return f"(left_top: {self.left_top}, \
width: {self.width}, height: {self.height})"
