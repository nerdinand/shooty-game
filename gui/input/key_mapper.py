from typing import List

import pygame


class KeyMapper:
    QUIT = "QUIT"
    UP = "UP"
    LEFT = "LEFT"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    RELOAD = "RELOAD"

    KEY_MAP: dict[int, str] = {
        pygame.K_w: UP,
        pygame.K_a: LEFT,
        pygame.K_s: DOWN,
        pygame.K_d: RIGHT,
        pygame.K_r: RELOAD,
    }

    @classmethod
    def map(cls) -> List[str]:
        key_events = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT or KeyMapper.__is_key_pressed(
                event, pygame.K_ESCAPE
            ):
                return [KeyMapper.QUIT]

        keystate = pygame.key.get_pressed()
        for key, value in KeyMapper.KEY_MAP.items():
            if keystate[key]:
                key_events.append(value)

        return key_events

    @classmethod
    def __is_key_pressed(cls, event: pygame.event.Event, key: int) -> bool:
        return event.type == pygame.KEYDOWN and event.key == key
