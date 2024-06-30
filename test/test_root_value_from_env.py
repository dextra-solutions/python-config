import os

import pytest

from python_config.app_config import AppConfig
from test.test_utils.cleanup_env import cleanup_env


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Code to run before each test
    cleanup_env()
    os.environ['python_config.simple_string'] = 'simpleString'
    os.environ['python_config.simple_number'] = '123'
    os.environ['python_config.simple_bool_lower'] = 'true'
    os.environ['python_config.simple_bool_upper'] = 'True'
    os.environ['python_config.simple_bool_false'] = 'false'

    yield

    # Code to run after each test
    cleanup_env()


def test_root_value_from_env():
    config = AppConfig('empty.yaml').config()

    assert config.get('simple_string') == 'simpleString'
    assert config.get('simple_number') == 123
    assert config.get('simple_bool_lower') is True
    assert config.get('simple_bool_upper') is True
    assert config.get('simple_bool_false') is False
    assert config.get('simple_nonexistent_key') is None
