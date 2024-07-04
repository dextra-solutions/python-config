import os

from python_yaml_config.app_config import PYTHON_CONFIG_ENV_PREFIX

prefix = PYTHON_CONFIG_ENV_PREFIX


def cleanup_env():
    for key, value in os.environ.items():
        if key.lower().startswith(prefix):
            del os.environ[key]
