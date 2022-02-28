import unittest

from pygame.math import Vector2

from simulation.agent import Agent
from simulation.pistol import Pistol
from simulation.math_util import MathUtil
from simulation.player_type import PlayerType
from simulation.player import Player


class TestPlayer:
    class NonCollidingPlayerCollider:
        def move(self, player: Player) -> None:
            dx = player.velocity.x  # pylint: disable=invalid-name
            dy = player.velocity.y  # pylint: disable=invalid-name
            player.position.x += dx
            player.position.y += dy

    @unittest.mock.patch("simulation.projectile_collider.ProjectileCollider")
    def test_tick(self, projectile_collider: unittest.mock.Mock) -> None:
        MathUtil.seed(42)

        player_collider = TestPlayer.NonCollidingPlayerCollider()

        player = Agent(name="Agent", gun_class=Pistol, position=Vector2(0, 0))

        assert player.position == Vector2(0, 0)
        assert player.move_direction == Vector2(0, 0)
        assert player.look_direction == 0.0

        player.update_move_direction(Vector2(1, 1))
        player.update_look_direction(-0.5)

        player.tick(player_collider, projectile_collider)  # pyre-ignore[6]

        assert player.position == Vector2(1e-05, 1e-05)
        assert player.move_direction == Vector2(1, 1)
        assert player.look_direction == -0.5

        player.tick(player_collider, projectile_collider)  # pyre-ignore[6]

        assert player.position == Vector2(3e-05, 3e-05)
        assert player.move_direction == Vector2(1, 1)
        assert player.look_direction == -0.5
