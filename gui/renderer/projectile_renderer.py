import pygame

from .colors import Colors
from .utils import Utils
from simulation import Projectile


class ProjectileRenderer:
    @classmethod
    def render(cls, screen: pygame.surface.Surface, projectile: Projectile) -> None:
        screen_position = Utils.to_screen_position(
            screen.get_size(), projectile.position
        )
        pygame.draw.circle(screen, Colors.PROJECTILES_COLOR, screen_position, 2)
