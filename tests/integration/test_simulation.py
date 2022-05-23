import pytest

from pygame.math import Vector2

from simulation import Simulation


@pytest.mark.integration
class TestSimulation:
    def test_simulation(self) -> None:
        simulation = Simulation(seed=42)
        assert len(simulation.players) == 4
        assert simulation.players[0].position == Vector2(0.547599, 0.117508)
        assert simulation.players[0].move_direction == Vector2(0, 0)
        assert simulation.players[0].velocity == Vector2(0, 0)
        assert simulation.players[0].look_direction == 0.0
        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == False
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 30

        assert simulation.players[1].position == Vector2(0.292521, 0.256248)
        assert simulation.players[1].move_direction == Vector2(0, 0)
        assert simulation.players[1].velocity == Vector2(0, 0)
        assert simulation.players[1].look_direction == 0.0
        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == False
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 30

        assert simulation.players[2].position == Vector2(0.61553, 0.57369)
        assert simulation.players[2].move_direction == Vector2(0, 0)
        assert simulation.players[2].velocity == Vector2(0, 0)
        assert simulation.players[2].look_direction == 0.0
        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == False
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 30

        assert simulation.players[3].position == Vector2(0.724526, 0.160857)
        assert simulation.players[3].move_direction == Vector2(0, 0)
        assert simulation.players[3].velocity == Vector2(0, 0)
        assert simulation.players[3].look_direction == 0.0
        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == False
        assert simulation.players[3].health == 100
        assert simulation.players[3].gun.bullet_count == 30

        simulation.tick()

        assert simulation.players[0].position == Vector2(0.547599, 0.117508)
        assert simulation.players[0].move_direction == Vector2(-0.156156, -0.940406)
        assert simulation.players[0].velocity == Vector2(0, 0)
        assert simulation.players[0].look_direction == -5.627240503927933
        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == False
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 30

        assert simulation.players[1].position == Vector2(0.292511, 0.256241)
        assert simulation.players[1].move_direction == Vector2(-0.946928, -0.602325)
        assert simulation.players[1].velocity == Vector2(-9.46928e-06, -6.02325e-06)
        assert simulation.players[1].look_direction == 2.997688755590463
        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == True
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 30

        assert simulation.players[2].position == Vector2(0.61553, 0.57369)
        assert simulation.players[2].move_direction == Vector2(-0.559119, 0.178531)
        assert simulation.players[2].velocity == Vector2(0, 0)
        assert simulation.players[2].look_direction == 6.1886091335565325
        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == False
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 30

        assert simulation.players[3].position == Vector2(0.724526, 0.160857)
        assert simulation.players[3].move_direction == Vector2(0.611639, 0.396279)
        assert simulation.players[3].velocity == Vector2(0, 0)
        assert simulation.players[3].look_direction == -3.1949896696401625
        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == False
        assert simulation.players[3].health == 100
        assert simulation.players[3].gun.bullet_count == 30

        for i in range(1000):
            simulation.tick()

        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 29
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == True
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 28
        assert len(simulation.players[1].gun.projectiles) == 1

        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 30
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 30
        assert len(simulation.players[3].gun.projectiles) == 0

        for i in range(1000):
            simulation.tick()

        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 28
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == True
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 26
        assert len(simulation.players[1].gun.projectiles) == 1

        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 30
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 29
        assert len(simulation.players[3].gun.projectiles) == 0

        for i in range(1000):
            simulation.tick()

        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 27
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == True
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 23
        assert len(simulation.players[1].gun.projectiles) == 1

        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 29
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 28
        assert len(simulation.players[3].gun.projectiles) == 0

        for i in range(1000):
            simulation.tick()

        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 27
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].is_dead == False
        assert simulation.players[1].is_moving == True
        assert simulation.players[1].health == 100
        assert simulation.players[1].gun.bullet_count == 23
        assert len(simulation.players[1].gun.projectiles) == 0

        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 29
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 27
        assert len(simulation.players[3].gun.projectiles) == 1

        for i in range(5000):
            simulation.tick()

        assert simulation.players[0].position == Vector2(0.31497, 0.0475575)
        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 25
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].position == Vector2(0.165, 0.830102)
        assert simulation.players[1].is_dead == True
        assert simulation.players[1].is_moving == False
        assert simulation.players[1].health == -8
        assert simulation.players[1].gun.bullet_count == 20
        assert len(simulation.players[1].gun.projectiles) == 0

        assert simulation.players[2].position == Vector2(0.975, 0.463979)
        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 27
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].position == Vector2(0.0710402, 0.481686)
        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 21
        assert len(simulation.players[3].gun.projectiles) == 0

        while not simulation.is_over():
            simulation.tick()

        assert simulation.tick_count == 18000

        assert simulation.players[0].position == Vector2(0.025, 0.025)
        assert simulation.players[0].is_dead == False
        assert simulation.players[0].is_moving == True
        assert simulation.players[0].health == 100
        assert simulation.players[0].gun.bullet_count == 22
        assert len(simulation.players[0].gun.projectiles) == 0

        assert simulation.players[1].position == Vector2(0.165, 0.830102)
        assert simulation.players[1].is_dead == True
        assert simulation.players[1].is_moving == False
        assert simulation.players[1].health == -8
        assert simulation.players[1].gun.bullet_count == 20
        assert len(simulation.players[1].gun.projectiles) == 0

        assert simulation.players[2].position == Vector2(0.975, 0.307579)
        assert simulation.players[2].is_dead == False
        assert simulation.players[2].is_moving == True
        assert simulation.players[2].health == 100
        assert simulation.players[2].gun.bullet_count == 18
        assert len(simulation.players[2].gun.projectiles) == 0

        assert simulation.players[3].position == Vector2(0.025, 0.975)
        assert simulation.players[3].is_dead == False
        assert simulation.players[3].is_moving == True
        assert simulation.players[3].health == 6
        assert simulation.players[3].gun.bullet_count == 13
        assert len(simulation.players[3].gun.projectiles) == 0
