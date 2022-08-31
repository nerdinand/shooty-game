from shutil import rmtree
from os.path import exists
import pytest

from training import Training
from training import Configuration as TrainingConfiguration
from simulation import Configuration as SimulationConfiguration
from environment import Configuration as EnvironmentConfiguration


@pytest.mark.integration
class TestTraining:
    def training_configuration(self) -> TrainingConfiguration:
        conf_file = open("tests/fixtures/training_conf.yaml")
        return TrainingConfiguration.from_file(conf_file)

    def simulation_configuration(self) -> SimulationConfiguration:
        conf_file = open("tests/fixtures/simulation_conf.yaml")
        return SimulationConfiguration.from_file(conf_file)

    def environment_configuration(self) -> EnvironmentConfiguration:
        conf_file = open("tests/fixtures/environment_conf.yaml")
        return EnvironmentConfiguration.from_file(conf_file)

    def test_training(self) -> None:
        training = Training(
            training_configuration=self.training_configuration(),
            simulation_configuration=self.simulation_configuration(),
            environment_configuration=self.environment_configuration(),
        )
        experiment_id = training.train()

        model_path = f"models/{experiment_id}/"
        log_path = f"logs/{experiment_id}_1/"

        assert exists(f"{model_path}/rl_model_1000_steps.zip")
        assert exists(log_path)

        rmtree(model_path)
        rmtree(log_path)
