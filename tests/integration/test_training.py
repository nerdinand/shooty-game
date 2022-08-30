from shutil import rmtree
from os.path import exists
import pytest

from training import Training
from training import Configuration as TrainingConfiguration
from simulation import Configuration as SimulationConfiguration


@pytest.mark.integration
class TestTraining:
    def training_configuration(self) -> TrainingConfiguration:
        conf_file = open("tests/fixtures/training_conf.yaml")
        return TrainingConfiguration.from_file(conf_file)

    def simulation_configuration(self) -> SimulationConfiguration:
        conf_file = open("tests/fixtures/simulation_conf.yaml")
        return SimulationConfiguration.from_file(conf_file)

    def test_training(self) -> None:
        training = Training(
            self.training_configuration(), self.simulation_configuration()
        )
        experiment_id = training.train()

        model_path = f"models/{experiment_id}/"
        log_path = f"logs/{experiment_id}_1/"

        assert exists(f"{model_path}/rl_model_1000_steps.zip")
        assert exists(log_path)

        rmtree(model_path)
        rmtree(log_path)
