import os
import unittest

import pytest
from box import Box, BoxError

from python_yaml_config.app_config import get_config_from_file_and_env
from test.test_utils.cleanup_env import cleanup_env


@pytest.fixture(autouse=True)
def setup_and_teardown():
    cleanup_env()
    yield
    cleanup_env()


@pytest.mark.parametrize("key,expected", [
    ('string', 'simpleString'),
    ('number', 123),
    ('bool1', True),
    ('bool2', True),
    ('bool3', False),
    ('simple_nonexistent_key', None)
])
def test_root_value(key, expected):
    config = get_config_from_file_and_env('config.yaml')
    assert config.get(key) == expected


@pytest.mark.parametrize("key,value,expected", [
    ('string', 'simpleString', 'simpleString'),
    ('number', '123', 123),
    ('bool1', 'true', True),
    ('bool2', 'True', True),
    ('bool3', 'false', False),
    ('empty', '', '')
])
def test_root_value_from_env(key, value, expected):
    os.environ[f'python_yaml_config_{key}'] = value

    config = get_config_from_file_and_env('empty.yaml')

    assert config.get(key) == expected


def test_nested_value():
    config = get_config_from_file_and_env('config.yaml')

    assert_nested_values(config)


def test_nested_value_from_env():
    os.environ['python_yaml_config_nested_value'] = 'nestedValue'
    os.environ['python_yaml_config_such_much_nested_value'] = 'suchMuchNestedValue'

    config = get_config_from_file_and_env('empty.yaml')

    assert_nested_values(config)


def assert_nested_values(config: Box):
    assert config.get('nested.value') == 'nestedValue'
    assert config.get('such.much.nested.value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested').get('value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested.value') == 'suchMuchNestedValue'
    assert config.such.much.nested.value == 'suchMuchNestedValue'


def test_immutability():
    config = get_config_from_file_and_env('config.yaml')
    assert config.i.am.immutable == 'immutable'
    with unittest.TestCase().assertRaises(BoxError):
        config.i.am.immutable = 'mutable'

def test_missing_key():
    config = get_config_from_file_and_env('config.yaml')
    assert config.get('missing.key') is None

def test_invalid_config_file():
    with unittest.TestCase().assertRaises(FileNotFoundError):
        get_config_from_file_and_env('non_existent.yaml')
