import pygame
from pygame.math import Vector2

from .colors import Colors
from .projectile_renderer import ProjectileRenderer
from .utils import Utils
from simulation import Player


class GunRenderer:
    GUN_LENGTH = 15  # FIXME: Should scale with player size # pylint: disable=fixme

    @classmethod
    def render(cls, screen: pygame.surface.Surface, player: Player) -> None:
        screen_position = Utils.to_screen_position(screen.get_size(), player.position)
        pygame.draw.line(
            screen,
            Colors.GUN_COLOR,
            screen_position,
            screen_position + GunRenderer.__gun_tip(player.look_direction),
        )
        for projectile in player.gun.projectiles:
            ProjectileRenderer.render(screen, projectile)

    @classmethod
    def __gun_tip(cls, player_look_direction: float) -> Vector2:
        vector = pygame.math.Vector2()
        vector.from_polar((GunRenderer.GUN_LENGTH, player_look_direction))
        return vector
