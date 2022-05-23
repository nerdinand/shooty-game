from stable_baselines3 import A2C

from environment import Environment

import datetime

TIMESTEPS = 10000
EXPERIMENT_ID: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def main() -> None:
    """Run training with A2C."""
    env = Environment()
    env.reset()

    # default: net_arch = [dict(pi=[64, 64], vf=[64, 64])]
    # policy_kwargs = dict(net_arch=[64, 64, 64, 64, 64, 64, 64, 64, 64, 64])
    model = A2C(
        "MultiInputPolicy",
        env,
        # policy_kwargs=policy_kwargs,
        verbose=1,
        tensorboard_log="logs",
    )

    for i in range(1000):
        model.learn(
            total_timesteps=TIMESTEPS,
            reset_num_timesteps=False,
            tb_log_name=f"A2C_{EXPERIMENT_ID}",
        )
        model.save(f"models/A2C_{EXPERIMENT_ID}_{TIMESTEPS * (i+1)}")


if __name__ == "__main__":
    main()
