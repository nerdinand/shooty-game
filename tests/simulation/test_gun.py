from collections import namedtuple

import unittest
import pytest

from pygame.math import Vector2

from simulation.pistol import Pistol
from simulation.projectile_collider import ProjectileCollider

from typing import List, Tuple


class TestGun:
    testdata: List[Tuple[bool, List[float]]] = [
        # is_moving, expected_directions
        (False, [0.0, -1.6584485464559542, -1.5149685899647345, 1.4033671465862105]),
        (True, [0.0, -6.633794185823817, -6.059874359858938, 5.613468586344842]),
    ]

    def test_reloading(self) -> None:
        pistol = Pistol(player=None)  # pyre-ignore[6]
        pistol.bullet_count -= 1

        assert pistol.bullet_count == 9
        assert pistol.is_reloading == False
        pistol.start_reload()
        assert pistol.is_reloading == True
        pistol.start_reload()
        assert pistol.is_reloading == True

        for _ in range(pistol.reload_ticks):
            assert pistol.is_reloading == True
            pistol.tick(projectile_collider=None)  # pyre-ignore[6]

        assert pistol.is_reloading == False
        assert pistol.bullet_count == 10

    def test_dead_player_doesnt_shoot(self) -> None:
        Player = namedtuple(
            "Player", ["is_moving", "is_dead", "position", "look_direction"]
        )

        dead_player = Player(
            is_moving=False,
            is_dead=True,
            position=Vector2(0.5, 0.5),
            look_direction=0.0,
        )

        pistol = Pistol(player=dead_player)  # pyre-ignore[6]
        assert len(pistol.projectiles) == 0
        pistol.shoot()
        assert len(pistol.projectiles) == 0

    @pytest.mark.parametrize("is_moving,expected_directions", testdata)
    @unittest.mock.patch("simulation.projectile_collider.ProjectileCollider")
    def test_shooting(
        self,
        mock_projectile_collider: unittest.mock.Mock,
        is_moving: bool,
        expected_directions: List[float],
    ) -> None:
        # mock projectile collider so no collisions happen (projectiles live forever)
        mock_projectile_collider.apply_collision_effect.return_value = False

        Player = namedtuple(
            "Player", ["is_moving", "is_dead", "position", "look_direction"]
        )

        player = Player(
            is_moving=is_moving,
            is_dead=False,
            position=Vector2(0.5, 0.5),
            look_direction=0.0,
        )

        pistol = Pistol(player=player)  # pyre-ignore[6]

        assert len(pistol.projectiles) == 0
        pistol.shoot()  # not spraying
        assert len(pistol.projectiles) == 1
        assert pistol.projectiles[0].gun == pistol
        assert pistol.projectiles[0].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[0].direction == expected_directions[0]

        for _ in range(pistol.cooldown_ticks):
            pistol.shoot()  # not creating projectile due to cooldown
            assert len(pistol.projectiles) == 1
            pistol.tick(projectile_collider=mock_projectile_collider)

        pistol.shoot()  # spraying
        assert len(pistol.projectiles) == 2
        assert pistol.projectiles[1].gun == pistol
        assert pistol.projectiles[1].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[1].direction == expected_directions[1]

        for _ in range(pistol.cooldown_ticks):
            pistol.shoot()  # not creating projectile due to cooldown
            assert len(pistol.projectiles) == 2
            pistol.tick(projectile_collider=mock_projectile_collider)

        pistol.shoot()  # spraying
        assert len(pistol.projectiles) == 3
        assert pistol.projectiles[2].gun == pistol
        assert pistol.projectiles[2].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[2].direction == expected_directions[2]

        for _ in range(pistol.cooldown_ticks + 1):
            pistol.tick(projectile_collider=mock_projectile_collider)

        pistol.shoot()  # not spraying
        assert len(pistol.projectiles) == 4
        assert pistol.projectiles[3].gun == pistol
        assert pistol.projectiles[3].position == Vector2(0.5, 0.5)
        assert pistol.projectiles[3].direction == expected_directions[0]
