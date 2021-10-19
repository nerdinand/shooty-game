import pygame
from pygame.math import Vector2
from .key_mapper import KeyMapper

class DirectionMapper:
  DIRECTIONS = {
    KeyMapper.UP:     Vector2(0, -1), 
    KeyMapper.LEFT:   Vector2(-1, 0), 
    KeyMapper.DOWN:   Vector2(0, 1), 
    KeyMapper.RIGHT:  Vector2(1, 0)
  }

  def map(self, directions):
    direction_vector = Vector2()
    for direction in directions:
      direction_vector += DirectionMapper.DIRECTIONS[direction]

    if direction_vector.length_squared() != 0.0:
      direction_vector.normalize_ip()

    return direction_vector
