//
// Created by lukas on 15.11.20.
//

#ifndef KVMSWITCH_USBSWITCH_H
#define KVMSWITCH_USBSWITCH_H

#include <Arduino.h>
#include <Pins.h>

extern int activeSource;
extern bool activeUSBSourceChanged;
extern bool activeHDMISourceChanged;
extern bool switchUSB;
extern bool getPinState(int pin);

void usb_switch_setup();
void usb_switch_loop();

void setActiveUSBSource();
void switchUSBSource();

int getActiveUSBSource();

#endif //KVMSWITCH_USBSWITCH_H
