//
// Created by lukas on 15.11.20.
//

#include "Pins.h"

String getLEDStates() {
    String states = "";
    states = states + "USB :" + String(getUSBLEDStates()) + "\n";
    states = states + "HDMI :" + String(getHDMILEDStates()) + "\n";
    return states;
}

int getHDMILEDStates() {
    int states = 0;
    states += getPinState(SOURCE_HDMI_LED_PIN_0) ? 1 : 0;
    states += getPinState(SOURCE_HDMI_LED_PIN_1) ? 2 : 0;
    states += getPinState(SOURCE_HDMI_LED_PIN_2) ? 3 : 0;
    return states;
}

int getUSBLEDStates() {
    int states = 0;
    states += getPinState(SOURCE_USB_LED_PIN_0) ? 1 : 0;
    states += getPinState(SOURCE_USB_LED_PIN_1) ? 2 : 0;
    states += getPinState(SOURCE_USB_LED_PIN_2) ? 3 : 0;
    states += getPinState(SOURCE_USB_LED_PIN_3) ? 4 : 0;
    return states;
}

bool getPinState(int pin) {
    return digitalRead(pin) == HIGH ? true : false;
}