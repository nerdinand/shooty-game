import typing
from collections import OrderedDict
from typing import Optional
from typing import Tuple
from typing import Union

import gym
import numpy as np
import numpy.typing as npt
from gym import spaces
from pygame.math import Vector2

from gui import Gui
from simulation import Agent
from simulation import Configuration
from simulation import Intersection
from simulation import NoneIntersection
from simulation import Player
from simulation import PlayerFactory
from simulation import Simulation
from simulation import Visibility

Observation = OrderedDict[str, Union[npt.NDArray, int]]


class Environment(gym.Env):  # pylint: disable=too-many-instance-attributes
    """Custom OpenAI gym that wraps the shooty-game simulation."""

    metadata = {"render.modes": ["human"]}

    def __init__(
        self, configuration: Configuration, random_seed: Optional[int] = None
    ) -> None:
        """Initialize a new Environment, defining the action and observation spaces."""
        super().__init__()

        if random_seed is None:
            self.seed(configuration.random_seed)
        else:
            self.seed(random_seed)

        self.configuration = configuration

        self.gui: Optional[Gui] = None
        self.agent: Agent = None  # pyre-ignore[8]
        self.simulation: Simulation = None  # pyre-ignore[8]

        # W, A, S, D, R, Mouse1, look-, look+
        buttons_space = spaces.MultiBinary(8)
        self.action_space: spaces.multi_binary.MultiBinary = buttons_space

        position_space = spaces.Box(low=0.0, high=1.0, shape=[2], dtype=np.float32)
        visibility_positions_space = spaces.Box(
            low=0.0, high=1.0, shape=[Visibility.NUMBER_OF_RAYS * 2], dtype=np.float32
        )
        visibility_types_space = spaces.MultiDiscrete([3] * Visibility.NUMBER_OF_RAYS)
        self.observation_space = spaces.Dict(
            {
                "position": position_space,
                "health": spaces.Discrete(101),  # maximum health (+1 for zero)
                "bullets": spaces.Discrete(31),  # maximum magazine size (+1 for zero)
                "is_reloading": spaces.Discrete(2),
                "visibility_positions": visibility_positions_space,
                "visibility_types": visibility_types_space,
            }
        )

        self.player_factory = PlayerFactory()

    def seed(self, seed: Optional[int] = None) -> None:
        self.__seed = seed  # pylint: disable=unused-private-member

    def reset(self) -> Observation:
        """Reset the environment.

        Returns:
            Observation: An initial observation.
        """

        self.agent = self.player_factory.agent()
        self.simulation = Simulation(self.configuration, agent=self.agent)
        # print(f"reset env {self.__seed}: {self.simulation.tick_count}")
        return self.__get_observation()

    def step(
        self, action: npt.NDArray
    ) -> Tuple[Observation, int, bool, typing.Dict[str, str]]:
        """Simulate a step in the environment.

        Args:
            action (npt.NDArray): The action to take in the environment.

        Returns:
            Tuple: A tuple of: observation, reward, done, info.
        """
        self.__take_action(action)
        self.simulation.tick()
        done = self.simulation.is_over()
        reward = self.__calculate_reward()
        observation = self.__get_observation()

        # print(f"step env {self.__seed} {self.simulation.tick_count}: {reward} {done}")

        return observation, reward, done, {}

    def render(self, mode: str = "human") -> None:
        """Render the environment in a graphical interface."""
        if mode == "human":
            gui = self.gui
            if gui is None:
                gui = Gui()
                self.gui = gui
                gui.initialize()

            gui.tick()
            if gui.is_render_necessary():
                gui.render(self.simulation)
        else:
            super().render(mode=mode)

    def __take_action(self, action: npt.NDArray) -> None:
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

        if action[4] == 1:
            self.agent.gun.start_reload()

        if action[5] == 1:
            self.agent.gun.shoot()

        look_direction = self.agent.look_direction
        if action[6] == 1:
            look_direction = look_direction - 1
        if action[7] == 1:
            look_direction = look_direction + 1
        self.agent.update_look_direction(look_direction)

    def __calculate_reward(self) -> int:
        reward = -(sum(b.health for b in self.simulation.bots))
        reward += self.simulation.dead_bots_count() * 1000
        # if self.agent.is_dead:
        #     reward = -100000

        return reward

    def __get_observation(self) -> Observation:
        intersections = Visibility.get_intersections(
            self.simulation.get_obstacles(), self.agent
        )

        observation = OrderedDict(
            [
                (
                    "position",
                    np.array(
                        [self.agent.position.x, self.agent.position.y], dtype=np.float32
                    ),
                ),
                ("health", self.agent.health),
                ("bullets", self.agent.gun.bullet_count),
                ("is_reloading", 1 if self.agent.gun.is_reloading else 0),
                (
                    "visibility_positions",
                    np.array(
                        [(i.position.x, i.position.y) for i in intersections],
                        dtype=np.float32,
                    ).flatten(),
                ),
                (
                    "visibility_types",
                    np.array([Environment.__map_entity_type(i) for i in intersections]),
                ),
            ]
        )
        return observation

    @classmethod
    def __map_entity_type(cls, intersection: Intersection) -> int:
        if intersection is NoneIntersection:
            return -1
        if intersection.obstacle is Player:
            return 0

        return 1
