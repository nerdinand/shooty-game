import io
from dataclasses import dataclass

import yaml


@dataclass
class BotConfiguration:
    kind: str


@dataclass
class Configuration:
    map: str
    bots: list[BotConfiguration]
    random_seed: int
    with_human: bool

    @classmethod
    def from_file(cls, conf_file: io.TextIOBase) -> "Configuration":
        parsed_configuration = yaml.safe_load(conf_file)
        configuration = Configuration(**parsed_configuration)
        configuration.bots = [
            BotConfiguration(**bot) for bot in parsed_configuration["bots"]
        ]
        return configuration
