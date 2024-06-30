import os

import yaml
from box import Box

from python_config.singleton_meta import SingletonMeta
from python_config.utils.convert import try_convert_string


class AppConfig(metaclass=SingletonMeta):
    __env_prefix: str = 'python_config.'
    __initialized: bool = False

    def __init__(self, config_file: str) -> None:
        """
        Initialize the AppConfig instance.

        Args:
            config_file (str): Path to the configuration file.
        """
        if not self.__initialized:
            self.__initialize(config_file)

    def config(self) -> Box:
        """
        Get the configuration as a Box object.

        Returns:
            Box: The configuration as a Box object, with dot notation and frozen state.
        """
        return Box(self._config, box_dots=True, frozen_box=True)

    def __initialize(self, config_file: str) -> None:
        with open(config_file, 'r') as file:
            content = yaml.safe_load(file)
            self._config = Box(content if content is not None else {}, box_dots=True, default_box=True)
        self.__override_with_env_variables()
        self.__initialized = True

    def __override_with_env_variables(self) -> None:
        env_vars = {key[len(self.__env_prefix):].lower(): value
                    for key, value in os.environ.items() if key.lower().startswith(self.__env_prefix)}
        for key in env_vars.keys():
            self.__set_nested_config(key, env_vars[key])

    def __set_nested_config(self, key, value):
        evaluated = try_convert_string(value)
        self._config[key] = evaluated
