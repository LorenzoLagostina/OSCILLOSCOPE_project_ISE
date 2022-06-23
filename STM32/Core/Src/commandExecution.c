#include "commandExecution.h"

void triggerType(uint8_t type){

	//interrompo l'esecuzione
	stopSampling();


	//salvo il tipo di trigger in quanto e' necessario
	//per la gestione del buffer
	triggerMode = type;


	//se devo eseguire la modalita' auto, normal o single
	//avvio il campionamento
	if (type == 0 || type == 1 || type == 2 ){


		if (type == 0){

			//nel caso della modalita' auto devo essere in grado
			//di riconoscere l'assenza di trigger nella prima parte
			sampleIndex = 0;

		} else {

			//in modalita' normal e single
			sampleIndex = 256;

		}

		startSampling();

	}
}

void triggerLevel(uint8_t level){

	//interrompo l'esecuzione
	stopSampling();

	triggerLevelValue = level;

	//cambio il livello di trigger
	changeTrigger(level);

	//ricomincio l'esecuzione
		if (triggerMode != 3){

			if (triggerMode == 0){

						//nel caso della modalita' auto devo essere in grado
						//di riconoscere l'assenza di trigger nella prima parte
						sampleIndex = 0;

					} else {

						//in modalita' normal e single
						sampleIndex = 256;

					}
			startSampling();
		}
}

void samplingPeriod(uint32_t period){

	//interrompo l'esecuzione
	stopSampling();

	//cambio il periodo di campionamento
	changeSamplingPeriod(period);

	//ricomincio l'esecuzione
	if (triggerMode != 3){

		if (triggerMode == 0){

					//nel caso della modalita' auto devo essere in grado
					//di riconoscere l'assenza di trigger nella prima parte
					sampleIndex = 0;

				} else {

					//in modalita' normal e single
					sampleIndex = 256;

				}
		startSampling();
	}
}
