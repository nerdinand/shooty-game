from stable_baselines3 import PPO
from environment import Environment
import sys

def main():
  model_timesteps = sys.argv[1]

  episodes = 10

  model = PPO.load(f"models/PPO_{model_timesteps}")

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
