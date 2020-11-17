//
// Created by lukas on 15.11.20.
//

#include "usbSwitch.h"

void usb_switch_setup() {
    pinMode(SOURCE_USB_SWITCH_PIN, OUTPUT);
    pinMode(SOURCE_USB_LED_PIN_0, INPUT);
    pinMode(SOURCE_USB_LED_PIN_1, INPUT);
    pinMode(SOURCE_USB_LED_PIN_2, INPUT);
    pinMode(SOURCE_USB_LED_PIN_3, INPUT);
}

void usb_switch_loop() {
    setActiveUSBSource();
    if (activeUSBSourceChanged && activeHDMISourceChanged) {
        activeSource = getActiveUSBSource();
    }
}

void switchUSBSource() {
    if (switchUSB) {
        digitalWrite(SOURCE_USB_SWITCH_PIN, HIGH);     // press button
        delay(200);                                    // wait for 0.2 seconds
        digitalWrite(SOURCE_USB_SWITCH_PIN, LOW);    // release button
        delay(200);
    }
}

void setActiveUSBSource() {
    if (!activeUSBSourceChanged) {
        int led_pin = 0;
        switch (activeSource) {
            case 0:
                led_pin = SOURCE_USB_LED_PIN_0;
                break;
            case 1:
                led_pin = SOURCE_USB_LED_PIN_1;
                break;
            case 2:
                led_pin = SOURCE_USB_LED_PIN_2;
                break;
            case 3:
                led_pin = SOURCE_USB_LED_PIN_3;
                break;
            default:
                break;
        }
        if (!getPinState(led_pin)) {
            switchUSBSource();
        } else {
            activeUSBSourceChanged = true;
        }
    }
}

int getActiveUSBSource() {
    int newactiveSource = activeSource;
    newactiveSource = getPinState(SOURCE_USB_LED_PIN_0) ? 0 : newactiveSource;
    newactiveSource = getPinState(SOURCE_USB_LED_PIN_1) ? 1 : newactiveSource;
    newactiveSource = getPinState(SOURCE_USB_LED_PIN_2) ? 2 : newactiveSource;
    newactiveSource = getPinState(SOURCE_USB_LED_PIN_3) ? 3 : newactiveSource;
    return newactiveSource;
}