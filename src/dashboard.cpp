//
// Created by lukas on 15.11.20.
//

#include "dashboard.h"

AsyncWebServer server(80);
ESPDash dashboard(&server);

Card button0Card(&dashboard, BUTTON_CARD, "(1) Computer");
Card button1Card(&dashboard, BUTTON_CARD, "(2) Laptop");
Card button2Card(&dashboard, BUTTON_CARD, "(3) Laptop 2");
Card button3Card(&dashboard, BUTTON_CARD, "(4) Unknown");

Card usbToggleCard(&dashboard, BUTTON_CARD, "USB toggle");
Card hdmiToggleCard(&dashboard, BUTTON_CARD, "HDMI toggle");

Card usbStatusCard(&dashboard, STATUS_CARD, "USB Source");
Card hdmiStatusCard(&dashboard, STATUS_CARD, "HDMI Source");

unsigned int updateInterval = 1000;  // update only once a second
long lastUpdate = 0;

void dashboard_setup() {
    /* Start AsyncWebServer */
    server.begin();

    setDefaults();
    attachCallbacks();
}

void setDefaults() {
    setButtonStates();
    dashboard.sendUpdates();
}

void setButtonStates() {
    const char* usbStatus = activeUSBSourceChanged ?  "success" : "idle";
    const char* hdmiStatus = activeHDMISourceChanged ?  "success" : "idle";
    usbStatusCard.update(getUSBLEDStates(), usbStatus);
    hdmiStatusCard.update(getHDMILEDStates(), hdmiStatus);
    updateButtons(activeSource);
    usbToggleCard.update(switchUSB);
    hdmiToggleCard.update(switchHDMI);
}

void attachCallbacks() {
    usbToggleCard.attachCallback([&](bool value) {
        switchUSB = value;
        usbToggleCard.update(value);
        dashboard.sendUpdates();
    });
    hdmiToggleCard.attachCallback([&](bool value) {
        switchHDMI = value;
        hdmiToggleCard.update(value);
        dashboard.sendUpdates();
    });
    button0Card.attachCallback([&](bool value) {
        Serial.println("send Callback");
        buttonCallback(0);
    });
    button1Card.attachCallback([&](bool value) {
        Serial.println("send Callback");
        buttonCallback(1);
    });
    button2Card.attachCallback([&](bool value) {
        Serial.println("send Callback");
        buttonCallback(2);
    });
    button3Card.attachCallback([&](bool value) {
        Serial.println("send Callback");
        buttonCallback(3);
    });
}

void dashboard_loop() {
    if((unsigned long)(millis() - lastUpdate) > updateInterval) {
        lastUpdate = millis();
        setButtonStates();
        dashboard.sendUpdates();
    }
}

void buttonCallback(int button) {
    Serial.print("Button clicked: ");
    Serial.println(button);
    updateButtons(button);
    activeSource = button;
    activeUSBSourceChanged = false;
    activeHDMISourceChanged = false;
    dashboard.sendUpdates();
}

void updateButtons(int activeButton) {
    for (int i = 0; i < 4; i++) {
        if (i == activeButton) {
            setButtonCard(i, true);
        } else {
            setButtonCard(i, false);
        }
    }
}

void setButtonCard(int number, bool value) {
    switch (number) {
        case 0:
            button0Card.update(value);
            break;
        case 1:
            button1Card.update(value);
            break;
        case 2:
            button2Card.update(value);
            break;
        case 3:
            button3Card.update(value);
            break;
        default:
            break;
    }
}