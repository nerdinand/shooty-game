from typing import List

import pygame


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
    pygame.K_w: UP,
    pygame.K_a: LEFT,
    pygame.K_s: DOWN,
    pygame.K_d: RIGHT,
    pygame.K_r: RELOAD,
  }

  TOGGLE_KEYS = {
    pygame.K_m: TOGGLE_SHOW_MAP,
    pygame.K_b: TOGGLE_SHOW_BOTS
  }

  def map(self) -> List[str]:
    key_events = []

    for event in pygame.event.get():
      if event.type == pygame.QUIT or self.__is_key_pressed(event, pygame.K_ESCAPE):
        return [KeyMapper.QUIT]

      for k, v in KeyMapper.TOGGLE_KEYS.items():
        if self.__is_key_pressed(event, k):
          key_events.append(v)

    keystate = pygame.key.get_pressed()
    for k, v in KeyMapper.KEY_MAP.items():
      if keystate[k]:
        key_events.append(v)

    return key_events

  def __is_key_pressed(self, event: pygame.event.Event, key: int) -> bool:
    return event.type == pygame.KEYDOWN and event.key == key
