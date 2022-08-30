import pytest

from stable_baselines3.common.env_checker import check_env
from environment import Environment
from simulation import Configuration


@pytest.mark.integration
class TestEnvironment:
    def simulation_configuration(self) -> Configuration:
        conf_file = open("tests/fixtures/simulation_conf.yaml")
        return Configuration.from_file(conf_file)

    def test_check_environment(self) -> None:
        check_env(Environment(self.simulation_configuration(), random_seed=42))
