from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

from environment import Environment

import datetime

TIMESTEPS = 10000000
EXPERIMENT_ID: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
PARALLELISM: int = 4
RANDOM_SEED: int = 0


def main() -> None:
    """Run training in parallel."""
    subproc_vec_env = make_vec_env(Environment, n_envs=PARALLELISM, seed=RANDOM_SEED)

    # default: net_arch = [dict(pi=[64, 64], vf=[64, 64])]
    policy_kwargs = dict(net_arch=[64, 64, 64, 64, 64, 64, 64, 64, 64, 64])
    model = PPO(
        "MultiInputPolicy",
        subproc_vec_env,
        policy_kwargs=policy_kwargs,
        verbose=1,
        tensorboard_log="logs",
    )
    model.learn(
        total_timesteps=TIMESTEPS,
        reset_num_timesteps=False,
        tb_log_name=f"PPO_{EXPERIMENT_ID}",
    )
    model.save(f"models/PPO_{EXPERIMENT_ID}")


if __name__ == "__main__":
    main()
