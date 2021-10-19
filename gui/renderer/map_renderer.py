import pygame
from pygame.locals import Rect

from .colors import Colors

class MapRenderer:
  def render(self, screen, map):
    for screen_obstacle in self.__screen_obstacles(screen.get_size(), map.obstacles):
      pygame.draw.rect(screen, Colors.OBSTACLES_COLOR, screen_obstacle)

  def __screen_obstacles(self, screen_size, obstacles):
    return [self.__to_screen_rect(screen_size, obstacle) for obstacle in obstacles]

  def __to_screen_rect(self, screen_size, obstacle):
    left_top_transformed = obstacle.left_top.elementwise() * screen_size
    width_transformed = obstacle.width * screen_size[0]
    height_transformed = obstacle.height * screen_size[1]
    return Rect(left_top_transformed.x, left_top_transformed.y, width_transformed, height_transformed)
