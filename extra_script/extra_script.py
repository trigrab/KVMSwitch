Import("env")

# this is no valid python file as it is interpreted by platformio's SCon configuration system

import os
try:
    import yaml
except ImportError:
    env.Execute("$PYTHONEXE -m pip install -r extra_script/requirements.txt")
    import yaml
from before import before_buildprog, before_upload
from after import after_buildprog

# fix espota
from config import get_config
_config = get_config()
if not _config["OTA"]["use"]:
    env.Replace(UPLOAD_PROTOCOL="esptool")

for item in os.listdir(env.get("PROJECTSRC_DIR")):
    full_path = os.path.join("${BUILD_DIR}", "src", item) + ".o"
    env.AddPreAction(full_path, [after_buildprog, before_buildprog])
    env.AddPostAction(full_path, after_buildprog)

# add after script as PreAction too, because of files that may be lost from broken builds
AlwaysBuild("${BUILD_DIR}/${PROGNAME}.elf")

env.AddPreAction("upload", before_upload)
