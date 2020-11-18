import yaml
import os
from os.path import expanduser
from shutil import copyfile


class ConfigMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cls._config_file = None

    @property
    def config_file(cls):
        if cls._config_file is not None:
            return cls._config_file
        else:
            return cls._find_config_file()

    def _find_config_file(cls):
        script_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(expanduser("~"), ".espclient")
        if os.path.exists(os.path.join(script_path,  "config.yml")):
            cls._config_file = os.path.join(script_path, "config.yml")
        else:
            config_file = os.path.join(config_path, "config.yml")
            if not os.path.exists(config_file):
                os.makedirs(config_path, exist_ok=True)
                copyfile(os.path.join(script_path, "config.yml.dist"),
                         config_file)
                print(f"New config file created. Check {config_file}")
            cls._config_file = config_file
        return cls._config_file



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
        with open(cls.config_file, "r") as file:
            content = "\n".join(file.readlines())
            return yaml.load(content, Loader=yaml.Loader)


class Config(metaclass=ConfigMeta):
    pass

