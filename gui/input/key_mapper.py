import pygame
from pygame.locals import *


class KeyMapper:
  QUIT = 'QUIT'
  UP = 'UP'
  LEFT = 'LEFT'
  DOWN = 'DOWN'
  RIGHT = 'RIGHT'
  RELOAD = 'RELOAD'

  KEY_MAP = {
    K_w: UP,     # type: ignore
    K_a: LEFT,   # type: ignore
    K_s: DOWN,   # type: ignore
    K_d: RIGHT,  # type: ignore
    K_r: RELOAD  # type: ignore
  }

  def map(self):
    if self.__quit_event():
      return [KeyMapper.QUIT]

    keystate = pygame.key.get_pressed()
    return [v for k, v in KeyMapper.KEY_MAP.items() if keystate[k]]

  def __quit_event(self):
    for event in pygame.event.get():
      if event.type == QUIT or \
          (event.type == KEYDOWN and event.key == K_ESCAPE):
          return True
    return False
