//
// Created by lukas on 15.11.20.
//

#ifndef KVMSWITCH_HDMISWITCH_H
#define KVMSWITCH_HDMISWITCH_H

#include <Arduino.h>
#include <Pins.h>

extern int activeSource;
extern bool activeHDMISourceChanged;
extern bool switchHDMI;

void hdmi_switch_setup();
void hdmi_switch_loop();

void switchHDMISource();
void setActiveHDMISource();

#endif //KVMSWITCH_HDMISWITCH_H
