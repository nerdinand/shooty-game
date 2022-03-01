from pygame.math import Vector2

from simulation.agent import Agent
from simulation.bot import Bot
from simulation.pistol import Pistol
from simulation.obstacle import Obstacle
from simulation.projectile_collider import ProjectileCollider
from simulation.projectile import Projectile


class TestProjectileCollider:
    def test_move(self) -> None:
        player = Agent(name="Agent", gun_class=Pistol)
        obstacle = Obstacle.fixed(
            name="Obstacle 1", left=0.0, top=0.0, width=0.1, height=0.1
        )
        bot = Bot(name="Bot Wade", gun_class=Pistol, position=Vector2(0.4, 0.2))
        dead_bot = Bot(name="Bot Dead", gun_class=Pistol, position=Vector2(0.1, 0.3))
        dead_bot.is_dead = True
        obstacles = [player, obstacle, bot, dead_bot]

        projectile_collider = ProjectileCollider(obstacles)

        # can't shoot myself
        projectile = Projectile(gun=player.gun, position=player.position, direction=0.0)
        projectile.last_position = player.position
        assert projectile_collider.apply_collision_effect(projectile) == False

        # can't shoot dead players
        projectile = Projectile(
            gun=player.gun, position=dead_bot.position, direction=0.0
        )
        projectile.last_position = player.position
        assert projectile_collider.apply_collision_effect(projectile) == False

        # shooting an obstacle
        projectile = Projectile(
            gun=player.gun, position=Vector2(0.05, 0.05), direction=0.0
        )
        projectile.last_position = player.position
        assert projectile_collider.apply_collision_effect(projectile) == True

        # shooting another player
        projectile = Projectile(gun=player.gun, position=bot.position, direction=0.0)
        projectile.last_position = player.position
        assert projectile_collider.apply_collision_effect(projectile) == True
        assert bot.health == 33
