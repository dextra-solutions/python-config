import os

import pytest

from python_config.app_config import AppConfig
from test.test_utils.cleanup_env import cleanup_env

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Code to run before each test
    cleanup_env()
    os.environ['python_config.nested.value'] = 'nestedValue'
    os.environ['python_config.such.much.nested.value'] = 'suchMuchNestedValue'

    yield

    # Code to run after each test
    cleanup_env()


def test_nested_value_from_env():
    config = AppConfig('empty.yaml').config()

    assert config.get('nested.value') == 'nestedValue'
    assert config.get('such.much.nested.value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested').get('value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested.value') == 'suchMuchNestedValue'
    assert config.such.much.nested.value == 'suchMuchNestedValue'

    cleanup_env()
