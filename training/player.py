import os
import random

from environment import Configuration as EnvironmentConfiguration
from environment import Environment
from simulation import Configuration as SimulationConfiguration
from training.configuration import resolve_algorithm_class


class Player:
    def __init__(
        self,
        model_path: str,
        number_of_episodes: int,
        simulation_configuration: SimulationConfiguration,
        environment_configuration: EnvironmentConfiguration,
    ) -> None:
        self.model_path = model_path
        self.number_of_episodes = number_of_episodes
        self.simulation_configuration = simulation_configuration
        self.environment_configuration = environment_configuration

    def play(self) -> None:
        algorithm = os.path.basename(  # pylint: disable=unused-variable
            self.model_path
        ).split("_")[
            0
        ]  # TODO: fix resolution of algorithm name

        model = resolve_algorithm_class("PPO").load(self.model_path)

        for _episode in range(self.number_of_episodes):
            env = Environment(
                simulation_configuration=self.simulation_configuration,
                environment_configuration=self.environment_configuration,
                random_seed=random.randint(0, 1234567890),
            )
            observation = env.reset()
            done = False
            cumulated_reward = 0

            while not done:
                action, _states = model.predict(observation)
                observation, reward, done, _info = env.step(action)
                env.render()
                cumulated_reward += reward

            print(cumulated_reward)
