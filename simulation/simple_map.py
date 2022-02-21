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
            Obstacle(
                "top left box", left_margin, top_margin, small_box_size, small_box_size
            )
        )
        self.obstacles.append(
            Obstacle(
                "bottom left box",
                left_margin,
                1 - bottom_margin - big_box_size,
                small_box_size,
                big_box_size,
            )
        )
        self.obstacles.append(
            Obstacle(
                "top right box",
                1 - right_margin - big_box_size,
                top_margin,
                big_box_size,
                small_box_size,
            )
        )
        self.obstacles.append(
            Obstacle(
                "bottom right box",
                1 - right_margin - small_box_size,
                1 - bottom_margin - small_box_size,
                small_box_size,
                small_box_size,
            )
        )
