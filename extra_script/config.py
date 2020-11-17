import os
import yaml
import logging

logger = logging.getLogger("")

config_file = "config.yml"

extra_config = {
    "wifi": {
        "file_path": os.path.join("src", "wifi.cpp"),
        "line_handle": "WiFi.begin",
        "line_f_string": "    WiFi.begin(\"{wifi_ssid}\", \"{wifi_pass}\");\n",
    },
    "OTA": {
        "file_path": os.path.join("src", "ota.cpp"),
        "line_handle": "ArduinoOTA.setPassword",
        "line_f_string": "    ArduinoOTA.setPassword(\"{ota_password}\");\n",
    },
}
tmp_suffix = ".tmp"


def get_config():
    """
    get config from yaml file
    :return: dict with config variables
    """
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            file_contents = "\n".join(file.readlines())
        config: dict = yaml.load(file_contents, Loader=yaml.Loader)
        for key, section in config.items():
            section.update(extra_config[key])
        return config
    else:
        logger.error("Config file does not exist. See README.md")
        exit(2)
