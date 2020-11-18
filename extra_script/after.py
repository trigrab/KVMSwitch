import os
from config import get_config, tmp_suffix


def after_buildprog(source, target, env):
    config: dict = get_config()
    fix_espota(env, config)
    for section_name, section in config.items():
        for key, item in section.items():
            if key == "replacements":
                for replacement in item:
                    if os.path.exists(replacement["file_path"] + tmp_suffix):
                        os.rename(replacement["file_path"] + tmp_suffix, replacement["file_path"])
