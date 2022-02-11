import gym
from stable_baselines3 import PPO
from environment import Environment

def main() -> None:
  env = Environment(with_gui=False)
  env.reset()

  model = PPO('MultiInputPolicy', env, verbose=1)
  model.learn(total_timesteps=10000)

  episodes = 10

  env = Environment(with_gui=True)
  for ep in range(episodes):
    obs = env.reset()
    done = False
    cumulated_reward = 0

    while not done:
      action, _states = model.predict(obs)
      obs, reward, done, info = env.step(action)
      env.render()
      cumulated_reward += reward

    print(cumulated_reward)


if __name__ == '__main__':
  main()
