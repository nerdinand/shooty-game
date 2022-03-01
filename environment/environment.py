import typing
from collections import OrderedDict
from typing import Optional
from typing import Tuple

import gym
import numpy as np
import numpy.typing as npt
from gym import spaces
from pygame.math import Vector2

from gui import Gui
from simulation import Agent
from simulation import Intersection
from simulation import NoneIntersection
from simulation import PlayerFactory
from simulation import Simulation
from simulation import Visibility


Observation = OrderedDict[str, npt.NDArray]


class Environment(gym.Env):
    """Custom OpenAI gym that wraps the shooty-game simulation."""

    metadata = {"render.modes": ["human"]}

    def __init__(self) -> None:
        """Initialize a new Environment, defining the action and observation spaces."""
        super().__init__()

        self.gui: Optional[Gui] = None
        self.agent: Agent = None  # pyre-ignore[8]
        self.simulation: Simulation = None  # pyre-ignore[8]

        # W, A, S, D, R, Mouse1, look-, look+
        buttons_space = spaces.MultiBinary(8)
        self.action_space: spaces.multi_binary.MultiBinary = buttons_space

        positions_space = spaces.Box(
            low=0.0, high=1.0, shape=(Visibility.NUMBER_OF_RAYS, 2), dtype=np.float32
        )
        types_space = spaces.MultiBinary(Visibility.NUMBER_OF_RAYS)
        self.observation_space = spaces.Dict(
            {"positions": positions_space, "types": types_space}
        )

        self.player_factory = PlayerFactory()

    def reset(self) -> Observation:
        """Reset the environment.

        Returns:
            Observation: An initial observation.
        """

        self.agent = self.player_factory.agent()
        self.simulation = Simulation(agent=self.agent)
        return self.__get_observation()

    def step(
        self, action: npt.NDArray
    ) -> Tuple[OrderedDict[str, npt.NDArray], int, bool, typing.Dict[str, str]]:
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

    def __calculate_reward(self) -> int:
        reward = -(self.simulation.alive_players_count() + 1)
        if self.agent.is_dead:
            reward = -10000

        return reward

    def __get_observation(self) -> Observation:
        visible_points = Visibility.get_visible_points(
            self.simulation.get_obstacles(), self.agent
        )
        if len(visible_points) != Visibility.NUMBER_OF_RAYS:
            print("\a")
            import pdb  # pylint: disable=import-outside-toplevel

            pdb.set_trace()  # pylint: disable=multiple-statements, disable=forgotten-debug-statement

        return OrderedDict(
            [
                (
                    "positions",
                    np.array([(p.position.x, p.position.y) for p in visible_points]),
                ),
                (
                    "types",
                    np.array(
                        [Environment.__map_entity_type(p) for p in visible_points]
                    ),
                ),
            ]
        )

    @classmethod
    def __map_entity_type(cls, intersection: Intersection) -> int:
        if intersection is NoneIntersection:
            return -1

        return intersection.entity.get_entity_type().value
