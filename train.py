from stable_baselines3 import PPO
from environment import Environment

TIMESTEPS = 10000

def main() -> None:
  env = Environment(with_gui=False)
  env.reset()

  model = PPO('MultiInputPolicy', env, verbose=1, tensorboard_log='logs')

  for i in range(1000):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"models/PPO_{TIMESTEPS * (i+1)}")

if __name__ == '__main__':
  main()
