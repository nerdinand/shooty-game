from typing import List

import pygame
from pygame.locals import *


class KeyMapper:
  QUIT = 'QUIT'
  UP = 'UP'
  LEFT = 'LEFT'
  DOWN = 'DOWN'
  RIGHT = 'RIGHT'
  RELOAD = 'RELOAD'
  TOGGLE_SHOW_MAP = 'TOGGLE_SHOW_MAP'
  TOGGLE_SHOW_BOTS = 'TOGGLE_SHOW_BOTS'

  KEY_MAP = {
    K_w: UP,                # type: ignore[name-defined]
    K_a: LEFT,              # type: ignore[name-defined]
    K_s: DOWN,              # type: ignore[name-defined]
    K_d: RIGHT,             # type: ignore[name-defined]
    K_r: RELOAD,            # type: ignore[name-defined]
    K_m: TOGGLE_SHOW_MAP,   # type: ignore[name-defined]
    K_b: TOGGLE_SHOW_BOTS   # type: ignore[name-defined]
  }

  def map(self) -> List[str]:
    if self.__quit_event():
      return [KeyMapper.QUIT]

    keystate = pygame.key.get_pressed()
    return [v for k, v in KeyMapper.KEY_MAP.items() if keystate[k]]

  def __quit_event(self) -> bool:
    for event in pygame.event.get():
      if event.type == QUIT or self.__is_esc_pressed(event):  # type: ignore[name-defined]
          return True
    return False

  def __is_esc_pressed(self, event: pygame.event.Event) -> bool:
    return event.type == KEYDOWN and event.key == K_ESCAPE  # type: ignore[name-defined]
