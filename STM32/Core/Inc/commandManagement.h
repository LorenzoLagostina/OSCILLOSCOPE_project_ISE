#include <stdint.h>
#include "stm32f4xx_hal.h"
#include "commandExecution.h"

#ifndef COMMAND_MANAGEMENT
#define COMMAND_MANAGEMENT
//resetto la stringa di comando
void resetCommand(char* command, uint8_t length);
//analizzo il comando e, se questo risulta valido,
//lancio la funzione associata ad esso
void analyzeCommand(char* command, uint8_t length);

//converto i caratteri da esadecimale a intero
uint8_t hexToInt(char hex);
//ottengo il valore dell'argomento del comando
uint32_t obtainCommandValue(char* command, uint8_t posIn, uint8_t posFin);
#endif
