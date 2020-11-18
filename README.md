# KVMSwitch 

This is a project using an ESP8266 to programmatically switch a 4 port usb
hub and a 3 port hdmi switch.

## requirements

* platformio cli
* cmake
* pyyaml - should be installed automatically by platformio

## config

This project can be configured using a `config.yml` file. You can setup these
settings there. 
If you do not want to configure anything, just copy `config.yml.dist` to 
`config.yml`. 

* wifi - configure an access point you want to connect to
    * you can leave this unchanged to use last known wifi config of the esp
* OTA - configure a password for ArduinoOTA (Over the Air update)

## client

The project runs a web server on the esp which can be uses with any browser.
If you want to have some more advanced setup, see /pyclient for a python
client using websockets.

Install it using pip:
```bash
pip install git+https://github.com/trigrab/KVMSwitch@master#egg=espclient&subdirectory=pyclient
```
