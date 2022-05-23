from stable_baselines3 import PPO

from environment import Environment

import datetime

TIMESTEPS = 10000
EXPERIMENT_ID: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def main() -> None:
    """Run training with PPO."""
    env = Environment()
    env.reset()

    # default: net_arch = [dict(pi=[64, 64], vf=[64, 64])]
    policy_kwargs = dict(net_arch=[64, 64, 64, 64, 64, 64, 64, 64, 64, 64])
    model = PPO(
        "MultiInputPolicy",
        env,
        policy_kwargs=policy_kwargs,
        verbose=1,
        tensorboard_log="logs",
    )

    for i in range(1000):
        model.learn(
            total_timesteps=TIMESTEPS,
            reset_num_timesteps=False,
            tb_log_name=f"PPO_{EXPERIMENT_ID}",
        )
        model.save(f"models/PPO_{EXPERIMENT_ID}_{TIMESTEPS * (i+1)}")


if __name__ == "__main__":
    main()
