from stable_baselines3.common.callbacks import CheckpointCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv

from .configuration import Configuration as TrainingConfiguration
from environment import Environment
from simulation import Configuration as SimulationConfiguration


class Training:
    def __init__(
        self,
        training_configuration: TrainingConfiguration,
        simulation_configuration: SimulationConfiguration,
    ) -> None:
        self.training_configuration = training_configuration
        self.simulation_configuration = simulation_configuration

    def train(self) -> str:
        """Run training in parallel."""
        subproc_vec_env = make_vec_env(
            Environment,
            n_envs=self.training_configuration.parallelism,
            seed=self.training_configuration.random_seed,
            vec_env_cls=SubprocVecEnv,
            env_kwargs={"configuration": self.simulation_configuration},
        )

        checkpoint_callback = CheckpointCallback(
            save_freq=self.training_configuration.timesteps.save_every,
            save_path=f"./models/{self.training_configuration.experiment_id()}",
        )

        model = self.training_configuration.algorithm_class()(  # pyre-ignore[20]
            "MultiInputPolicy",
            subproc_vec_env,
            policy_kwargs={"net_arch": self.training_configuration.net_arch},
            verbose=1,
            tensorboard_log="logs",
        )

        model.learn(
            total_timesteps=self.training_configuration.timesteps.train_for,
            tb_log_name=self.training_configuration.experiment_id(),
            callback=checkpoint_callback,
        )

        return self.training_configuration.experiment_id()
