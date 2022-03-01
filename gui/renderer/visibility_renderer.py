from typing import Type
from typing import Union

import pygame

from .colors import Colors
from .utils import Utils
from simulation import Agent
from simulation import Bot
from simulation import Human
from simulation import Player
from simulation import Obstacle
from simulation import Simulation
from simulation import Visibility


class VisibilityRenderer:
    COLOR_MAP: dict[Type[Obstacle], pygame.Color] = {
        Obstacle: Colors.OBSTACLES_COLOR,
        Bot: Colors.BOT_COLOR,
        Human: Colors.HUMAN_COLOR,
        Agent: Colors.HUMAN_COLOR,
    }

    @classmethod
    def render(
        cls, screen: pygame.surface.Surface, player: Player, obstacles: list[Obstacle]
    ) -> None:
        intersections = Visibility.get_intersections(obstacles, player)
        for intersection in intersections:
            screen_position = Utils.to_screen_position(
                screen.get_size(), intersection.position
            )
            pygame.draw.circle(
                screen,
                VisibilityRenderer.COLOR_MAP[intersection.obstacle.__class__],
                screen_position,
                1,
            )
