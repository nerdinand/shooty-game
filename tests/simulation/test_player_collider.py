from pygame.math import Vector2

from simulation.agent import Agent
from simulation.simple_bot import SimpleBot
from simulation.pistol import Pistol
from simulation.obstacle import Obstacle
from simulation.player_collider import PlayerCollider


class TestPlayerCollider:
    def test_move(self) -> None:
        player = Agent(name="Agent", gun_class=Pistol)
        obstacle = Obstacle.fixed(
            name="Obstacle 1", left=0.0, top=0.0, width=0.1, height=0.1
        )
        bot1 = SimpleBot(name="Bot Wade", gun_class=Pistol, position=Vector2(0.4, 0.2))
        bot2 = SimpleBot(name="Bot Dead", gun_class=Pistol, position=Vector2(0.1, 0.3))
        bot2.is_dead = True
        obstacles = [player, obstacle, bot1, bot2]

        player_collider = PlayerCollider(obstacles)

        # collision with obstacle
        player.position = Vector2(0.2, 0.2)
        player.velocity = Vector2(-0.1, -0.1)
        player_collider.move(player)
        assert player.position == Vector2(0.1, 0.115)

        # collision with player
        player.position = Vector2(0.2, 0.2)
        player.velocity = Vector2(0.2, 0)
        player_collider.move(player)
        assert player.position == Vector2(0.37, 0.2)

        # no collision with dead player
        player.position = Vector2(0.2, 0.2)
        player.velocity = Vector2(-0.1, 0.1)
        player_collider.move(player)
        assert player.position == Vector2(0.1, 0.3)

        # no collision
        player.position = Vector2(0.2, 0.2)
        player.velocity = Vector2(0, 0.1)
        player_collider.move(player)
        assert player.position == Vector2(0.2, 0.3)
