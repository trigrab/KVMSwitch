//
// Created by lukas on 15.11.20.
//

#ifndef KVMSWITCH_DASHBOARD_H
#define KVMSWITCH_DASHBOARD_H

#include <Arduino.h>

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

extern int activeSource;
extern bool activeUSBSourceChanged;
extern bool activeHDMISourceChanged;
extern bool switchUSB;
extern bool switchHDMI;

extern int getUSBLEDStates();
extern int getHDMILEDStates();

void dashboard_setup();
void dashboard_loop();

void setDefaults();
void setButtonStates();
void attachCallbacks();

void buttonCallback(int button);
void updateButtons(int activeButton);
void setButtonCard(int number, bool value);

#endif //KVMSWITCH_DASHBOARD_H
