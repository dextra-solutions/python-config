from python_config.app_config import AppConfig


def test_root_value():
    config = AppConfig('config.yaml').config()

    assert config.get('simple_string') == 'simpleString'
    assert config.get('simple_number') == 123
    assert config.get('simple_bool_lower') is True
    assert config.get('simple_bool_upper') is True
    assert config.get('simple_bool_false') is False
    assert config.get('simple_nonexistent_key') is None
