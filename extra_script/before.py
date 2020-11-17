import os

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
    if config["OTA"]["setup"]:
        upload_flags = "--auth=" + config["OTA"]["password"]
        env.Append(UPLOAD_FLAGS=[upload_flags])


def before_buildprog(source, target, env):
    config = get_config()
    if config["wifi"]["setup"]:
        wifi_ssid = config["wifi"]["ssid"]
        wifi_pass = config["wifi"]["passphrase"]
        new_line = config["wifi"]["line_f_string"].format(wifi_ssid=wifi_ssid, wifi_pass=wifi_pass)
        change_line_in_file(config["wifi"]["file_path"], config["wifi"]["line_handle"], new_line)
    if config["OTA"]["setup"]:
        ota_password = config["OTA"]["password"]
        new_line = config["OTA"]["line_f_string"].format(ota_password=ota_password)
        change_line_in_file(config["OTA"]["file_path"], config["wifi"]["line_handle"], new_line)


def change_line_in_file(filename, line_handle, new_line):
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
        for i, line in enumerate(lines):
            if line_handle in line:
                lines[i] = new_line
        if not os.path.exists(filename + tmp_suffix):
            os.rename(filename, filename + tmp_suffix)
        else:
            logger.error(f"[ERROR] {filename + tmp_suffix} file exists, was the last build interrupted?")
            exit(2)
        with open(filename, "w") as output_file:
            if len(lines) > 0:
                output_file.writelines(lines)
