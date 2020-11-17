Import("env")

# this is no valid python file as it is interpreted by platformio's SCon configuration system

try:
    import yaml
except ImportError:
    env.Execute("$PYTHONEXE -m pip install -r extra_script/requirements.txt")
    import yaml
from before import before_buildprog, before_upload
from after import after_script

# add after script as PreAction too, because of files that may be lost from broken builds
env.AddPreAction("${BUILD_DIR}/src/main.cpp.o", [after_script, before_buildprog])
env.AddPostAction("${BUILD_DIR}/src/main.cpp.o", after_script)

env.AddPreAction("upload", before_upload)
