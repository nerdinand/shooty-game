from collections import namedtuple

import unittest

from pygame.math import Vector2

from simulation.pistol import Pistol
from simulation.projectile_collider import ProjectileCollider


class TestGun:
    def test_reloading(self) -> None:
        pistol = Pistol(player=None)  # pyre-ignore[6]
        pistol.bullet_count -= 1

        assert pistol.bullet_count == 9
        assert pistol.is_reloading == False
        pistol.start_reload()

        for _ in range(pistol.reload_ticks):
            assert pistol.is_reloading == True
            pistol.tick(projectile_collider=None)  # pyre-ignore[6]

        assert pistol.is_reloading == False
        assert pistol.bullet_count == 10

    @unittest.mock.patch("simulation.projectile_collider.ProjectileCollider")
    def test_shooting_standing(
        self, mock_projectile_collider: unittest.mock.Mock
    ) -> None:
        # mock projectile collider so no collisions happen (projectiles live forever)
        mock_projectile_collider.apply_collision_effect.return_value = False

        Player = namedtuple(
            "Player", ["is_moving", "is_dead", "position", "look_direction"]
        )

        player = Player(
            is_moving=False,
            is_dead=False,
            position=Vector2(0.5, 0.5),
            look_direction=0.0,
        )

        pistol = Pistol(player=player)  # pyre-ignore[6]

        assert len(pistol.projectiles) == 0
        pistol.shoot()
        assert len(pistol.projectiles) == 1
        assert pistol.projectiles[0].gun == pistol
        assert pistol.projectiles[0].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[0].direction == -1.6584485464559542

        for _ in range(pistol.cooldown_ticks):
            pistol.shoot()  # not creating projectile due to cooldown
            assert len(pistol.projectiles) == 1
            pistol.tick(projectile_collider=mock_projectile_collider)

        pistol.shoot()
        assert len(pistol.projectiles) == 2
        assert pistol.projectiles[1].gun == pistol
        assert pistol.projectiles[1].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[1].direction == -1.5149685899647345

        for _ in range(pistol.cooldown_ticks):
            pistol.shoot()  # not creating projectile due to cooldown
            assert len(pistol.projectiles) == 2
            pistol.tick(projectile_collider=mock_projectile_collider)

        pistol.shoot()
        assert len(pistol.projectiles) == 3
        assert pistol.projectiles[2].gun == pistol
        assert pistol.projectiles[2].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[2].direction == 1.4033671465862105
