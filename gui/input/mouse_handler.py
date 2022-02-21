from typing import Tuple

import pygame
from pygame.math import Vector2

from simulation import Player


class MouseHandler:
    def __init__(self, screen_rect: pygame.rect.Rect) -> None:
        self.screen_rect = screen_rect

    def handle_mouse_events(self, player: Player) -> None:
        player.update_look_direction(self.look_direction(player.position))

        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            player.gun.shoot()

    def look_direction(self, player_position: Vector2) -> float:
        mouse_position = pygame.mouse.get_pos()
        return self.__position_to_direction(player_position, mouse_position)

    def __position_to_direction(
        self, player_position: Vector2, mouse_position: Tuple[int, int]
    ) -> float:
        return (self.__to_game_position(mouse_position) - player_position).as_polar()[1]

    def __to_game_position(self, screen_position: Tuple[int, int]) -> Vector2:
        return Vector2(screen_position).elementwise() / Vector2(
            self.screen_rect.width, self.screen_rect.height
        )
