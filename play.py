import sys

from stable_baselines3 import PPO

from environment import Environment


def main():
    model = sys.argv[1]

    episodes = 10

    model = PPO.load(model)

    env = Environment()
    for _episode in range(episodes):
        observation = env.reset()
        done = False
        cumulated_reward = 0

        while not done:
            action, _states = model.predict(observation)
            observation, reward, done, _info = env.step(action)
            env.render()
            cumulated_reward += reward

        print(cumulated_reward)


if __name__ == "__main__":
    main()
