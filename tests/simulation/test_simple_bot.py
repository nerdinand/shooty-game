import unittest

from pygame.math import Vector2

from simulation.simple_bot import SimpleBot
from simulation.pistol import Pistol
from simulation.math_util import MathUtil


class TestSimpleBot:
    @unittest.mock.patch("simulation.projectile_collider.ProjectileCollider")
    @unittest.mock.patch("simulation.player_collider.PlayerCollider")
    def test_tick(
        self,
        player_collider: unittest.mock.Mock,
        projectile_collider: unittest.mock.Mock,
    ) -> None:
        MathUtil.seed(42)

        bot = SimpleBot(name="Bot Fergus", gun_class=Pistol)

        assert bot.position == Vector2(0.5, 0.5)
        assert bot.move_direction == Vector2(0, 0)
        assert bot.look_direction == 0.0

        bot.tick(player_collider, projectile_collider)

        assert bot.position == Vector2(0.5, 0.5)
        assert bot.move_direction == Vector2(0.278854, -0.949978)
        assert bot.look_direction == -4.499413632617615

        bot.tick(player_collider, projectile_collider)

        assert bot.position == Vector2(0.5, 0.5)
        assert bot.move_direction == Vector2(0.751796, -0.59658)
        assert bot.look_direction == 3.3441777214792934
