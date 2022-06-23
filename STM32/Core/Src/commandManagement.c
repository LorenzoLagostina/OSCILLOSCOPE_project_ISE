#include "commandManagement.h"

void resetCommand(char* command, uint8_t length){

	for(int i = 0; i <= length; i++){

		command[i] = '\0';
	}


}


void analyzeCommand(char* command, uint8_t length){

	if (length == 6) {

		if (command[1] == 'T') {

			if (command[2] == 'T') {

						//eseguo comando Trigger Type
						triggerType(obtainCommandValue(command, 3, 4));
					}

			if (command[2] == 'L') {

						//eseguo comando Trigger Level
						triggerLevel(obtainCommandValue(command, 3, 4));
					}
		}
	} else if (length == 12) {

		if (command[1] == 'S' && command[2] == 'P') {

			//eseguo comando Sampling Period
			samplingPeriod(obtainCommandValue(command, 3, 10));
		}
	}
}

uint32_t obtainCommandValue(char* command, uint8_t posIn, uint8_t posFin){

	uint32_t result = 0;

	for(int i = posIn; i <= posFin; i++){

		result <<= 4;
		result += hexToInt(command[i]);
	}
	return result;
}

uint8_t hexToInt(char hex)
{
    if (hex >= '0' && hex <= '9')
        return hex - 48;
    if (hex >= 'A' && hex <= 'F')
        return hex - 'A' + 10;
    if (hex >= 'a' && hex <= 'f')
        return hex - 'a' + 10;
    return 0;
}
