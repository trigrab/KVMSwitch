//
// Created by lukas on 15.11.20.
//

#include <hdmiSwitch.h>

void switchHDMISource() {
    if (switchHDMI) {
        digitalWrite(SOURCE_HDMI_SWITCH_PIN, LOW);     // press button
        delay(200);                                    // wait for 0.2 seconds
        digitalWrite(SOURCE_HDMI_SWITCH_PIN, HIGH);    // release button
        delay(200);
    }
}

void hdmi_switch_setup() {
    pinMode(SOURCE_HDMI_SWITCH_PIN, OUTPUT);
    digitalWrite(SOURCE_HDMI_SWITCH_PIN, HIGH);
    pinMode(SOURCE_HDMI_LED_PIN_0, INPUT);
    pinMode(SOURCE_HDMI_LED_PIN_1, INPUT);
    pinMode(SOURCE_HDMI_LED_PIN_2, INPUT);
}

void hdmi_switch_loop() {
    setActiveHDMISource();
}

void setActiveHDMISource() {
    if (!activeHDMISourceChanged) {
        int led_pin = 0;
        switch (activeSource) {
            case 0:
                led_pin = SOURCE_HDMI_LED_PIN_0;
                break;
            case 1:
                led_pin = SOURCE_HDMI_LED_PIN_1;
                break;
            case 2:
                led_pin = SOURCE_HDMI_LED_PIN_2;
                break;
            case 3:
                return;
                break;
            default:
                break;
        }
        if (!getPinState(led_pin)) {
            switchHDMISource();
        } else {
            activeHDMISourceChanged = true;
        }
    }
}