import sys

from stable_baselines3 import PPO

from environment import Environment

import random


def main() -> None:
    """Play some episodes using a trained model."""
    model = sys.argv[1]

    episodes = 10

    model = PPO.load(model)

    for _episode in range(episodes):
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


if __name__ == "__main__":
    main()
