from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv

from environment import Environment

import datetime

TRAIN_FOR_TIMESTEPS = 100_000_000
SAVE_EVERY_TIMESTEPS = 100_000

ALGORITHM_CLASS = PPO
PARALLELISM: int = 6
RANDOM_SEED: int = 0

EXPERIMENT_ID: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")


def main() -> None:
    """Run training in parallel."""
    subproc_vec_env = make_vec_env(
        Environment, n_envs=PARALLELISM, seed=RANDOM_SEED, vec_env_cls=SubprocVecEnv
    )

    # default: net_arch = [dict(pi=[64, 64], vf=[64, 64])]
    # policy_kwargs = dict(net_arch=[64, 64, 64, 64, 64, 64, 64, 64, 64, 64])
    model = ALGORITHM_CLASS(
        "MultiInputPolicy",
        subproc_vec_env,
        # policy_kwargs=policy_kwargs,
        verbose=1,
        tensorboard_log="logs",
    )
    # model.load('models/PPO_2022-05-26_170132.zip')
    for i in range(int(TRAIN_FOR_TIMESTEPS / SAVE_EVERY_TIMESTEPS)):
        model.learn(
            total_timesteps=SAVE_EVERY_TIMESTEPS,
            reset_num_timesteps=False,
            tb_log_name=f"{ALGORITHM_CLASS.__name__}_{EXPERIMENT_ID}",
        )
        file_name = f"models/{ALGORITHM_CLASS.__name__}_{EXPERIMENT_ID}_{SAVE_EVERY_TIMESTEPS * (i+1)}"
        model.save(file_name)
        print(f"Model saved as {file_name}.zip")


if __name__ == "__main__":
    main()
