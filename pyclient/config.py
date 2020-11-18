import yaml

class config_meta(type):
    def __init__(cls, *args, **kwargs):
        cls._config_file = "config.yml"

    @property
    def hostname(cls):
        return cls._get_config_by_key("hostname")

    def _get_config_by_key(cls, key: str):
        config = cls._get_config()
        if key in config:
            return config[key] 

    def _get_config(cls):
        with open(cls._config_file, "r") as file:
            content = "\n".join(file.readlines())
            return yaml.load(content, Loader=yaml.Loader)


class config(metaclass=config_meta):
    pass

