import unittest

from box import BoxError

from python_config.app_config import AppConfig


def test_immutability():
    config = AppConfig('config.yaml').config()
    assert config.i.am.immutable == 'immutable'
    with unittest.TestCase().assertRaises(BoxError):
        config.i.am.immutable = 'mutable'
