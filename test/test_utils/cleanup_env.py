import os

prefix = 'python_config.'


def cleanup_env():
    for key, value in os.environ.items():
        if key.lower().startswith(prefix):
            del os.environ[key]
