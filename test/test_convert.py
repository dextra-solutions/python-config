from python_yaml_config.utils.convert import try_convert_string


def test_try_convert_string_for_boolean_true():
    result = try_convert_string('true')
    assert isinstance(result, bool) 
    assert result == True


def test_try_convert_string_for_boolean_false():
    result = try_convert_string('false')
    assert isinstance(result, bool)
    assert result == False


def test_try_convert_string_for_integer():
    result = try_convert_string('123')
    assert isinstance(result, int)
    assert result == 123


def test_try_convert_string_for_float():
    result = try_convert_string('123.45')
    assert isinstance(result, float)
    assert result == 123.45


def test_try_convert_string_for_list():
    result = try_convert_string('[1, 2, 3]')
    assert isinstance(result, list)
    assert result == [1, 2, 3]


def test_try_convert_string_for_unconvertible_string():
    result = try_convert_string('something')
    assert isinstance(result, str)
    assert result == 'something'
