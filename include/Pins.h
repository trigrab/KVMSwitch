//
// Created by lukas on 15.11.20.
//

#ifndef KVMSWITCH_PINS_H
#define KVMSWITCH_PINS_H

#include <Arduino.h>

#define SOURCE_USB_LED_PIN_0 16
#define SOURCE_USB_LED_PIN_1 14
#define SOURCE_USB_LED_PIN_2 12
#define SOURCE_USB_LED_PIN_3 13

#define SOURCE_USB_SWITCH_PIN 0

#define SOURCE_HDMI_SWITCH_PIN 15

#define SOURCE_HDMI_LED_PIN_0 5
#define SOURCE_HDMI_LED_PIN_1 4
#define SOURCE_HDMI_LED_PIN_2 2

String getLEDStates();
int getHDMILEDStates();
int getUSBLEDStates();
bool getPinState(int pin);



#endif //KVMSWITCH_PINS_H
