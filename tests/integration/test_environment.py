import pytest

from stable_baselines3.common.env_checker import check_env
from environment import Environment
from simulation import Configuration as SimulationConfiguration
from environment import Configuration as EnvironmentConfiguration


@pytest.mark.integration
class TestEnvironment:
    def simulation_configuration(self) -> SimulationConfiguration:
        conf_file = open("tests/fixtures/simulation_conf.yaml")
        return SimulationConfiguration.from_file(conf_file)

    def environment_configuration(self) -> EnvironmentConfiguration:
        conf_file = open("tests/fixtures/environment_conf.yaml")
        return EnvironmentConfiguration.from_file(conf_file)

    def test_check_environment(self) -> None:
        check_env(
            Environment(
                simulation_configuration=self.simulation_configuration(),
                environment_configuration=self.environment_configuration(),
                random_seed=42,
            )
        )
