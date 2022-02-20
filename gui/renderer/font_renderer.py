from typing import Tuple

import pygame

from .colors import Colors


class FontRenderer:
    font: pygame.font.Font

    @staticmethod
    def initialize() -> None:
        FontRenderer.font = pygame.font.Font(pygame.font.get_default_font(), 12)

    @staticmethod
    def render(
        screen: pygame.surface.Surface, text: str, position: Tuple[int, int]
    ) -> None:
        font_surface = FontRenderer.font.render(text, True, Colors.TEXT_COLOR)
        screen.blit(font_surface, position)
