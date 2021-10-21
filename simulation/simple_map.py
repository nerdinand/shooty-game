from .map import Map
from .obstacle import Obstacle


class SimpleMap(Map):
  def __init__(self):
    super().__init__()

    small_box_size = 0.05
    big_box_size = 0.3
    left_margin = 0.1
    top_margin = 0.1
    right_margin = 0.1
    bottom_margin = 0.1

    # top left box
    self.obstacles.append(
      Obstacle(
        left_margin,
        top_margin,
        small_box_size,
        small_box_size
      )
    )
    # bottom left box
    self.obstacles.append(
      Obstacle(
        left_margin,
        1 - bottom_margin - big_box_size,
        small_box_size,
        big_box_size
      )
    )
    # top right box
    self.obstacles.append(
      Obstacle(
        1 - right_margin - big_box_size,
        top_margin,
        big_box_size,
        small_box_size
      )
    )
    # bottom right box
    self.obstacles.append(
      Obstacle(
        1 - right_margin - small_box_size,
        1 - bottom_margin - small_box_size,
        small_box_size,
        small_box_size
      )
    )
