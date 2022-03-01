from .map import Map
from .obstacle import Obstacle


class SimpleMap(Map):
    def __init__(self) -> None:
        super().__init__()

        small_box_size = 0.05
        big_box_size = 0.3
        left_margin = 0.1
        top_margin = 0.1
        right_margin = 0.1
        bottom_margin = 0.1

        self.obstacles.append(
            Obstacle.fixed(
                name="top left box",
                left=left_margin,
                top=top_margin,
                width=small_box_size,
                height=small_box_size,
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="bottom left box",
                left=left_margin,
                top=1 - bottom_margin - big_box_size,
                width=small_box_size,
                height=big_box_size,
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="top right box",
                left=1 - right_margin - big_box_size,
                top=top_margin,
                width=big_box_size,
                height=small_box_size,
            )
        )
        self.obstacles.append(
            Obstacle.fixed(
                name="bottom right box",
                left=1 - right_margin - small_box_size,
                top=1 - bottom_margin - small_box_size,
                width=small_box_size,
                height=small_box_size,
            )
        )
