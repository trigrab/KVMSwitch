import os
import yaml
import logging

logger = logging.getLogger("")

config_file = "config.yml"

extra_config = {
    "wifi": {
        "replacements": [
            {
                "file_path": os.path.join("src", "wifi.cpp"),
                "line_handle": "WiFi.begin",
                "variables": ["ssid", "passphrase"],
                "line_f_string": "    WiFi.begin(\"{ssid}\", \"{passphrase}\");\n",
            },
        ]
    },
    "OTA": {
        "replacements": [
            {
                "file_path": os.path.join("src", "ota.cpp"),
                "line_handle": "ArduinoOTA.setPort",
                "variables": ["port"],
                "line_f_string": "    ArduinoOTA.setPort({port});\n",
            },
            {
                "file_path": os.path.join("src", "ota.cpp"),
                "line_handle": "ArduinoOTA.setHostname",
                "variables": ["hostname"],
                "line_f_string": "    ArduinoOTA.setHostname(\"{hostname}\");\n",
            },
            {
                "file_path": os.path.join("src", "ota.cpp"),
                "line_handle": "ArduinoOTA.setPassword",
                "variables": ["password"],
                "line_f_string": "    ArduinoOTA.setPassword(\"{password}\");\n",
             },
            {
                "file_path": os.path.join("src", "ota.cpp"),
                "line_handle": "ArduinoOTA.handle",
                "variables": [],
                "line_f_string": "    ArduinoOTA.handle();\n",
             },
        ]
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
            if key in extra_config:
                section.update(extra_config[key])
        return config
    else:
        logger.error("Config file does not exist. See README.md")
        exit(2)
