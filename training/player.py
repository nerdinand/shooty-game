import os
import random

from environment import Environment
from training.configuration import resolve_algorithm_class


class Player:
    def __init__(self, model_path: str, number_of_episodes: int) -> None:
        self.model_path = model_path
        self.number_of_episodes = number_of_episodes

    def play(self) -> None:
        algorithm = os.path.basename(self.model_path).split("_")[0]

        model = resolve_algorithm_class(algorithm).load(self.model_path)

        for _episode in range(self.number_of_episodes):
            env = Environment(random_seed=random.randint(0, 1234567890))
            observation = env.reset()
            done = False
            cumulated_reward = 0

            while not done:
                action, _states = model.predict(observation)  # pyre-ignore[6]
                observation, reward, done, _info = env.step(action)
                env.render()
                cumulated_reward += reward

            print(cumulated_reward)
