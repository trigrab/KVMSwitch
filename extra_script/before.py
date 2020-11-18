import os
from shutil import copyfile

from config import get_config, tmp_suffix, logger


def before_upload(source, target, env):
    """
    add auth flag to upload_flags
    :param source:
    :param target:
    :param env: Scons Construction Environment
    :return: None
    """
    config = get_config()
    env.Replace(UPLOAD_PROTOCOL="esptool")
    if config["OTA"]["use"]:
        env.Replace(UPLOAD_PROTOCOL="espota")
        upload_port = config["OTA"]["ip_address"]
        env.Replace(UPLOAD_PORT=upload_port)
        upload_flag = "--port=" + str(config["OTA"]["port"])
        env.Append(UPLOAD_FLAGS=upload_flag)
        upload_flag = "--auth=" + config["OTA"]["password"]
        env.Append(UPLOAD_FLAGS=upload_flag)
    elif "serial" in config:
        if "port" in config["serial"]:
            env.Replace(UPLOAD_PORT=config["serial"]["port"])

    print(env.Dump())


def before_buildprog(source, target, env):
    config = get_config()
    for section_name, section in config.items():
        for key, item in section.items():
            if key == "replacements":
                filename = item[0]["file_path"]
                if is_file_in_source(filename, source) and not are_there_leftovers(filename):
                    process_replacements(section, item)


def process_replacements(section, item):
    for replacement in item:
        process_single_replacement(section, replacement)


def process_single_replacement(section, replacement):
    format_vars = {}
    for variable in replacement["variables"]:
        if variable not in section:
            return
        format_vars[variable] = section[variable]
    new_line = replacement["line_f_string"].format(**format_vars)
    change_line_in_file(replacement["file_path"],
                        replacement["line_handle"],
                        new_line)

def is_file_in_source(filename, source):
    return filename in [x.rstr() for x in source]


def are_there_leftovers(filename):
    if not os.path.exists(filename + tmp_suffix):
        copyfile(filename, filename + tmp_suffix)
    else:
        logger.error(f"[ERROR] {filename + tmp_suffix} file exists, was the last build interrupted?")
        exit(2)


def change_line_in_file(filename, line_handle, new_line):
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            if line_handle in line:
                lines[i] = new_line
        with open(filename, "w") as output_file:
            if len(lines) > 0:
                output_file.writelines(lines)