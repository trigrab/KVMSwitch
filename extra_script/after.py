import os
from config import get_config, tmp_suffix


def after_script(source, target, env):
    config: dict = get_config()
    for key, section in config.items():
        if "line_handle" in section:
            if section["setup"]:
                if os.path.exists(section["file_path"] + tmp_suffix):
                    os.rename(section["file_path"] + tmp_suffix, section["file_path"])
