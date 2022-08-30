import datetime
import io
import typing
from dataclasses import dataclass

import yaml
from stable_baselines3 import A2C
from stable_baselines3 import PPO
from stable_baselines3.common.base_class import BaseAlgorithm


@dataclass
class TimestepsConfiguration:
    train_for: int
    save_every: int


ALGORITHM_CLASS_MAPPING: typing.Dict[str, typing.Type[BaseAlgorithm]] = {
    "PPO": PPO,
    "A2C": A2C,
}


def resolve_algorithm_class(algorithm: str) -> typing.Type[BaseAlgorithm]:
    return ALGORITHM_CLASS_MAPPING[algorithm]


@dataclass
class Configuration:
    algorithm: str
    timesteps: TimestepsConfiguration
    parallelism: int
    random_seed: int
    net_arch: list[int | dict[str, list[int]]]
    experiment_timestamp: str = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")

    @classmethod
    def from_file(cls, conf_file: io.TextIOBase) -> "Configuration":
        parsed_configuration = yaml.safe_load(conf_file)
        configuration = Configuration(**parsed_configuration)
        configuration.timesteps = TimestepsConfiguration(
            **parsed_configuration["timesteps"]
        )
        return configuration

    def algorithm_class(self) -> typing.Type[BaseAlgorithm]:
        return resolve_algorithm_class(self.algorithm)

    def experiment_id(self) -> str:
        return f"{self.algorithm}_{self.experiment_timestamp}"
