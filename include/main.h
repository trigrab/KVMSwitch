#ifndef KVMSWITCH_MAIN_H
#define KVMSWITCH_MAIN_H

#include <Arduino.h>

#include "Pins.h"
#include "wifi.h"
#include "ota.h"
#include "dashboard.h"
#include "hdmiSwitch.h"
#include "usbSwitch.h"

#if defined(ESP8266)
/* ESP8266 Dependencies */
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#elif defined(ESP32)
/* ESP32 Dependencies */
  #include <WiFi.h>
  #include <AsyncTCP.h>
  #include <ESPAsyncWebServer.h>
#endif
#include <ESPDash.h>

int activeSource = 0;
bool activeUSBSourceChanged = false;
bool activeHDMISourceChanged = false;

bool switchUSB = true;
bool switchHDMI = true;

void setup();
void loop();

void processSerialInput();

#endif //KVMSWITCH_MAIN_H
