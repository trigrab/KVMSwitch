//
// Created by lukas on 17.11.20.
//

#ifndef KVMSWITCH_WIFI_H
#define KVMSWITCH_WIFI_H

#include <Arduino.h>

#if defined(ESP8266)
/* ESP8266 Dependencies */
#include <ESP8266WiFi.h>
#endif

void wifi_setup();

#endif //KVMSWITCH_WIFI_H
