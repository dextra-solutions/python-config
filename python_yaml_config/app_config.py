import os

import yaml
from box import Box

from python_yaml_config.utils.convert import try_convert_string

PYTHON_CONFIG_ENV_PREFIX: str = 'python_yaml_config_'


def get_config_from_file_and_env(config_file: str) -> Box:
    """
    Get the configuration as a Box object.
    The file is taken as default and any values found in the environment variables will be overridden
    Args:
        config_file (str): Path to the configuration file.
    Returns:
        Box: The configuration as a Box object, with dot notation and frozen state.
    """

    with open(config_file, 'r') as file:
        content = yaml.safe_load(file)
        config_from_file = Box(content if content is not None else {}, box_dots=True, default_box=True)
    config_with_env = __override_with_env_variables(config_from_file)
    return Box(config_with_env, box_dots=True, frozen_box=True)


def __override_with_env_variables(config: Box) -> Box:
    """
    Override configuration with any environment variables.
    Args:
        config (Box): The configuration as a Box object.
    Returns:
        Box: The configuration as a Box object, with overrides from environment variables.
    """
    env_vars = {key[len(PYTHON_CONFIG_ENV_PREFIX):].lower().replace('_', '.'): value
                for key, value in os.environ.items() if key.lower().startswith(PYTHON_CONFIG_ENV_PREFIX)}
    for key in env_vars.keys():
        evaluated = try_convert_string(env_vars[key])
        config[key] = evaluated
    return config
