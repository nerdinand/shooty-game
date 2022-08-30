import pytest

from stable_baselines3.common.env_checker import check_env
from environment import Environment


@pytest.mark.integration
class TestEnvironment:
    def test_check_environment(self) -> None:
        check_env(Environment(random_seed=42))
