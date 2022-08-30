from shutil import rmtree
from os.path import exists
import pytest

from training import Training, Configuration


@pytest.mark.integration
class TestTraining:
    def training_configuration(self) -> Configuration:
        conf_file = open("tests/fixtures/training_conf.yaml")
        return Configuration.from_file(conf_file)

    def test_training(self) -> None:
        training = Training(self.training_configuration())
        experiment_id = training.train()

        model_path = f"models/{experiment_id}/"
        log_path = f"logs/{experiment_id}_1/"

        assert exists(f"{model_path}/rl_model_1000_steps.zip")
        assert exists(log_path)

        rmtree(model_path)
        rmtree(log_path)
