import unittest

from pygame.math import Vector2

from simulation.agent import Agent
from simulation.bot import Bot
from simulation.pistol import Pistol
from simulation.obstacle import Obstacle
from simulation.visibility import Visibility
from simulation.intersection import Intersection, NoneIntersection


class TestVisibility:
    def test_get_intersections(self) -> None:
        player = Agent(name="Agent", gun_class=Pistol)
        player.update_look_direction(-135)
        obstacle = Obstacle.fixed(
            name="Obstacle 1", left=0.0, top=0.0, width=0.1, height=0.1
        )
        bot = Bot(name="Bot Boris", gun_class=Pistol, position=Vector2(0.3, 0.2))
        obstacles = [obstacle, bot, player]

        intersections = Visibility.get_intersections(obstacles, player)

        expected_classes = [
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            NoneIntersection,
            NoneIntersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            Intersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
            NoneIntersection,
        ]

        expected_obstacles = [
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            obstacle,
            player,
            player,
            bot,
            bot,
            bot,
            bot,
            bot,
            bot,
            bot,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
            player,
        ]

        expected_positions = [
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0.016314, 0.1),
            Vector2(0.0328794, 0.1),
            Vector2(0.0487935, 0.1),
            Vector2(0.064103, 0.1),
            Vector2(0.0788501, 0.1),
            Vector2(0.0930735, 0.1),
            Vector2(0.1, 0.0930735),
            Vector2(0.1, 0.0788501),
            Vector2(0.1, 0.064103),
            Vector2(0.1, 0.0487935),
            Vector2(0.1, 0.0328794),
            Vector2(0.1, 0.016314),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0.288037, 0.215),
            Vector2(0.29554, 0.215),
            Vector2(0.302862, 0.215),
            Vector2(0.310011, 0.215),
            Vector2(0.315, 0.211887),
            Vector2(0.315, 0.200709),
            Vector2(0.315, 0.188891),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
            Vector2(0, 0),
        ]

        assert len(intersections) == 61
        assert list(map(lambda i: i.__class__, intersections)) == expected_classes
        assert list(map(lambda i: i.obstacle, intersections)) == expected_obstacles
        assert list(map(lambda i: i.position, intersections)) == expected_positions