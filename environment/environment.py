from collections import OrderedDict
from typing import Optional
from typing import Tuple
import typing

import gym
import numpy as np
import numpy.typing as npt
from gym import spaces
from pygame.math import Vector2

from gui import Gui
from simulation import Agent
from simulation import PlayerFactory
from simulation import Simulation
from simulation import Visibility


Observation = OrderedDict[str, npt.NDArray]


class Environment(gym.Env):
    metadata = {"render.modes": ["human"]}

    def __init__(self) -> None:
        super().__init__()

        self.gui: Optional[Gui] = None
        self.agent: Optional[Agent] = None
        self.simulation: Optional[Simulation] = None

        # W, A, S, D, R, Mouse1, look-, look+
        buttons_space = spaces.MultiBinary(8)
        self.action_space: spaces.multi_binary.MultiBinary = buttons_space

        positions_space = spaces.Box(low=0.0, high=1.0, shape=(61, 2), dtype=np.float32)
        types_space = spaces.MultiBinary(61)
        self.observation_space = spaces.Dict(
            {"positions": positions_space, "types": types_space}
        )

        self.player_factory = PlayerFactory()

    def reset(self) -> Observation:
        self.agent = self.player_factory.agent()
        self.simulation = Simulation(agent=self.agent)
        return self.__get_observation()

    def step(
        self, action: spaces.multi_binary.MultiBinary
    ) -> Tuple[OrderedDict[str, npt.NDArray], int, bool, typing.Dict[str, str]]:
        direction_vector = Vector2()

        if action[0] == 1:
            direction_vector += Vector2(0, -1)
        if action[1] == 1:
            direction_vector += Vector2(-1, 0)
        if action[2] == 1:
            direction_vector += Vector2(0, 1)
        if action[3] == 1:
            direction_vector += Vector2(1, 0)

        if direction_vector.length_squared() != 0.0:
            direction_vector.normalize_ip()

        self.agent.update_move_direction(direction_vector)

        # if action[4] == 1:
        #     self.agent.gun.start_reload()

        if action[5] == 1:
            self.agent.gun.shoot()

        look_direction = self.agent.look_direction
        if action[6] == 1:
            look_direction = look_direction - 1
        if action[7] == 1:
            look_direction = look_direction + 1
        self.agent.update_look_direction(look_direction)

        for _ in range(10):
            self.simulation.tick()

        done = self.simulation.is_over()

        reward = -(self.simulation.alive_players_count() + 1)
        if self.agent.is_dead:
            reward = -10000

        observation = self.__get_observation()
        return observation, reward, done, {}

    def render(self, mode: str = "human"):
        if mode == "human":
            if self.gui is None:
                self.gui = Gui(key_target_player=self.simulation.human)
                self.gui.initialize()
            self.gui.tick()
            self.gui.handle_key_events()
            self.gui.handle_mouse_events()
            if self.gui.is_render_necessary():
                self.gui.render(self.simulation)
        else:
            super().render(mode=mode)

    def __get_observation(self) -> Observation:
        visible_points = Visibility.get_visible_points(self.simulation, self.agent)
        if len(visible_points) != 61:
            print("\a")
            import pdb  # pylint: disable=import-outside-toplevel

            pdb.set_trace()  # pylint: disable=multiple-statements, disable=forgotten-debug-statement

        return OrderedDict(
            [
                (
                    "positions",
                    np.array([(p.position.x, p.position.y) for p in visible_points]),
                ),
                ("types", np.array([p.entity.type().value for p in visible_points])),
            ]
        )
