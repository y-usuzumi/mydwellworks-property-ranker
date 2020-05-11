import yaml

_CONFIG_DATA = None


def get_config():
    global _CONFIG_DATA

    if _CONFIG_DATA is None:
        with open('config.yaml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        _CONFIG_DATA = data
    return _CONFIG_DATA
