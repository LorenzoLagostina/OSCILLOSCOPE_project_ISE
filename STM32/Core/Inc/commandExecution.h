#include <stdint.h>
#include "utilities.h"

#ifndef COMMAND_EXECUTION
#define COMMAND_EXECUTION


//dichiaro le funzioni relative ai diversi comandi
void triggerType(uint8_t type);
void triggerLevel(uint8_t level);
void samplingPeriod (uint32_t period);
#endif
