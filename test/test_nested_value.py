from python_config.app_config import AppConfig


def test_nested_value():
    config = AppConfig('config.yaml').config()

    assert config.get('nested.value') == 'nestedValue'
    assert config.get('such.much.nested.value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested').get('value') == 'suchMuchNestedValue'
    assert config.get('such.much').get('nested.value') == 'suchMuchNestedValue'
    assert config.such.much.nested.value == 'suchMuchNestedValue'
