#include "main.h"

// the setup function runs once when you press reset or power the board
void setup() {

    Serial.begin(115200);
    Serial.println();

    wifi_setup();

    ota_setup();

    Serial.print("Connected, IP address: ");
    Serial.println(WiFi.localIP());

    dashboard_setup();
    usb_switch_setup();
    hdmi_switch_setup();
}

// the loop function runs over and over again forever
void loop() {
    ota_loop();
    dashboard_loop();
    usb_switch_loop();
    hdmi_switch_loop();
    processSerialInput();
}

void processSerialInput() {
    if (Serial.available() > 0) {
        String input = Serial.readStringUntil('\n');
        if (input.startsWith("source")) {
            Serial.print("active source: ");
            Serial.println(activeSource);
            Serial.print("active source changed: ");
            Serial.println(activeUSBSourceChanged);
        } else if (input.startsWith("switch usb")) {
            switchUSBSource();
            delay(200);                      // wait for a milisecond
            Serial.println("Switched");
            Serial.print("States: ");
            Serial.println(getLEDStates());
        } else if (input.startsWith("switch hdmi")) {
            switchHDMISource();
            Serial.println("Switched");
        } else if (input.startsWith("states")) {
            Serial.print("States: ");
            Serial.println(getLEDStates());
        } else if (input.startsWith("pin on ")) {
            int pin = input.substring(7).toInt();
            Serial.print("set pin ");
            Serial.print(pin);
            Serial.println(" on");
            digitalWrite(pin, HIGH);
        } else if (input.startsWith("pin off ")) {
            int pin = input.substring(7).toInt();
            Serial.print("set pin ");
            Serial.print(pin);
            Serial.println(" off");
            digitalWrite(pin, LOW);
        } else {
            Serial.println("help: switch_pin, source");
        }
    }
}


