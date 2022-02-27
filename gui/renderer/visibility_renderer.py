from typing import Type
from typing import Union

import pygame

from .colors import Colors
from .utils import Utils
from simulation import Agent
from simulation import Bot
from simulation import Entity
from simulation import Human
from simulation import Obstacle
from simulation import Simulation
from simulation import Visibility


class VisibilityRenderer:
    COLOR_MAP: dict[Type[Entity], pygame.Color] = {
        Obstacle: Colors.OBSTACLES_COLOR,
        Bot: Colors.BOT_COLOR,
        Human: Colors.HUMAN_COLOR,
        Agent: Colors.HUMAN_COLOR,
    }

    @classmethod
    def render(cls, screen: pygame.surface.Surface, simulation: Simulation) -> None:
        human = simulation.human

        if human is None:
            return

        visible_points = Visibility.get_visible_points(simulation, human)
        for visible_point in visible_points:
            screen_position = Utils.to_screen_position(
                screen.get_size(), visible_point.position
            )
            pygame.draw.circle(
                screen,
                VisibilityRenderer.COLOR_MAP[visible_point.entity.__class__],
                screen_position,
                1,
            )
