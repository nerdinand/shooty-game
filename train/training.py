from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv

from environment import Environment
from train import Configuration


class Training:
    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration

    def train(self) -> None:
        """Run training in parallel."""
        subproc_vec_env = make_vec_env(
            Environment,
            n_envs=self.configuration.parallelism,
            seed=self.configuration.random_seed,
            vec_env_cls=SubprocVecEnv,
        )

        checkpoint_callback = CheckpointCallback(
            save_freq=self.configuration.timesteps.save_every,
            save_path="./models/",
            name_prefix=self.configuration.experiment_id(),
        )

        model = self.configuration.algorithm_class()(  # pyre-ignore[20]
            "MultiInputPolicy",
            subproc_vec_env,
            policy_kwargs={"net_arch": self.configuration.net_arch},
            verbose=1,
            tensorboard_log="logs",
        )

        model.learn(
            total_timesteps=self.configuration.timesteps.train_for,
            tb_log_name=self.configuration.experiment_id(),
            callback=checkpoint_callback,
        )
