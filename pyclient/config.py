import yaml


class ConfigMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._config_file = "config.yml"

    @property
    def hostname(cls):
        return cls._get_config_by_key("hostname")

    @property
    def port(cls):
        return cls._get_config_by_key("port")

    def _get_config_by_key(cls, key: str):
        c = cls._get_config()
        if key in c:
            return c[key]

    def _get_config(cls):
        with open(cls._config_file, "r") as file:
            content = "\n".join(file.readlines())
            return yaml.load(content, Loader=yaml.Loader)


class Config(metaclass=ConfigMeta):
    pass

