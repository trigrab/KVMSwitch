//
// Created by lukas on 17.11.20.
//

#include "wifi.h"

void wifi_setup() {
    // This line is automatically replaced on build time. Do not change! See README.md and config.yml
    // WiFi.begin(YOUR_WIFI_SSID, YOUR_WIFI_PASSPHRASE);
    Serial.print("Connecting");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println();
}
