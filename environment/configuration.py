import io
from dataclasses import dataclass

import yaml


@dataclass
class Configuration:
    allow_reload: bool

    @classmethod
    def from_file(cls, conf_file: io.TextIOBase) -> "Configuration":
        parsed_configuration = yaml.safe_load(conf_file)
        configuration = Configuration(**parsed_configuration)
        return configuration
