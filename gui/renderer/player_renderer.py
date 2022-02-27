from typing import Tuple

import pygame
from pygame.locals import Rect
from pygame.math import Vector2

from .colors import Colors
from .font_renderer import FontRenderer
from .gun_renderer import GunRenderer
from .utils import Utils
from simulation import Player
from simulation import PlayerType


class PlayerRenderer:
    RELOAD_INDICATOR = "*"

    PLAYER_COLORS: dict[PlayerType, pygame.Color] = {
        PlayerType.HUMAN: Colors.HUMAN_COLOR,
        PlayerType.AGENT: Colors.HUMAN_COLOR,
        PlayerType.BOT: Colors.BOT_COLOR,
    }

    @classmethod
    def render(cls, screen: pygame.surface.Surface, player: Player) -> None:
        screen_rect = PlayerRenderer.__to_screen_rect(screen.get_size(), player)
        color = PlayerRenderer.PLAYER_COLORS[player.player_type]

        if player.player_type in (PlayerType.HUMAN, PlayerType.AGENT):
            PlayerRenderer.__render_fov_angles(screen, player)

        pygame.draw.ellipse(screen, color, screen_rect, width=1)
        FontRenderer.render(
            screen, str(player.health), (screen_rect.right + 2, screen_rect.top)
        )
        if player.gun.is_reloading:
            bullet_indicator = PlayerRenderer.RELOAD_INDICATOR
        else:
            bullet_indicator = str(player.gun.bullet_count)
        FontRenderer.render(
            screen, bullet_indicator, (screen_rect.right + 2, screen_rect.top + 10)
        )

        if player.is_dead:
            pygame.draw.line(
                screen,
                color,
                (screen_rect.left, screen_rect.top),
                (screen_rect.right, screen_rect.bottom),
            )
            pygame.draw.line(
                screen,
                color,
                (screen_rect.left, screen_rect.bottom),
                (screen_rect.right, screen_rect.top),
            )

        GunRenderer.render(screen, player)

    @classmethod
    def __to_screen_rect(cls, screen_size: Tuple[int, int], player: Player) -> Rect:
        player_screen_extent = Vector2(screen_size) * player.extent
        left_top = Utils.to_screen_position(screen_size, player.position) - (
            player_screen_extent / 2.0
        )
        return Rect(
            left_top.x, left_top.y, player_screen_extent.x, player_screen_extent.y
        )

    @classmethod
    def __render_fov_angles(
        cls, screen: pygame.surface.Surface, player: Player
    ) -> None:
        for angle in [player.get_left_fov_angle(), player.get_right_fov_angle()]:
            ray_start_point = player.position
            vector = Vector2()
            vector.from_polar((2.0, angle))
            ray_end_point = ray_start_point + vector

            ray_start_point = Utils.to_screen_position(
                screen.get_size(), ray_start_point
            )
            ray_end_point = Utils.to_screen_position(screen.get_size(), ray_end_point)

            pygame.draw.line(screen, Colors.FOV_BORDER, ray_start_point, ray_end_point)
