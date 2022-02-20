from typing import List

import pygame


class KeyMapper:
    QUIT = "QUIT"
    UP = "UP"
    LEFT = "LEFT"
    DOWN = "DOWN"
    RIGHT = "RIGHT"
    RELOAD = "RELOAD"
    TOGGLE_SHOW_MAP = "TOGGLE_SHOW_MAP"
    TOGGLE_SHOW_BOTS = "TOGGLE_SHOW_BOTS"

    KEY_MAP = {
        pygame.K_w: UP,  # pylint: disable=no-member
        pygame.K_a: LEFT,  # pylint: disable=no-member
        pygame.K_s: DOWN,  # pylint: disable=no-member
        pygame.K_d: RIGHT,  # pylint: disable=no-member
        pygame.K_r: RELOAD,  # pylint: disable=no-member
    }

    TOGGLE_KEYS = {
        pygame.K_m: TOGGLE_SHOW_MAP,
        pygame.K_b: TOGGLE_SHOW_BOTS,
    }  # pylint: disable=no-member

    @classmethod
    def map(cls) -> List[str]:
        key_events = []

        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or KeyMapper.__is_key_pressed(  # pylint: disable=no-member
                    event, pygame.K_ESCAPE  # pylint: disable=no-member
                )
            ):
                return [KeyMapper.QUIT]

            for key, value in KeyMapper.TOGGLE_KEYS.items():
                if KeyMapper.__is_key_pressed(event, key):
                    key_events.append(value)

        keystate = pygame.key.get_pressed()
        for key, value in KeyMapper.KEY_MAP.items():
            if keystate[key]:
                key_events.append(value)

        return key_events

    @classmethod
    def __is_key_pressed(cls, event: pygame.event.Event, key: int) -> bool:
        return (
            event.type == pygame.KEYDOWN and event.key == key
        )  # pylint: disable=no-member
