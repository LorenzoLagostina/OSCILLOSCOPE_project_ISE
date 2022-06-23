#include "utilities.h"

void bufferReset(){

	//resetto tutto il buffer
	for(int i = 0; i < 511; i ++){

			buffer[i][0] = 0;
			buffer[i][1] = 0;
		}
}

void bufferShift(){

	//eseguo lo shift a sinistra dei primi 256 campioni nel buffer
	//di fatto la prima meta' del buffer viene usata come fifo
	for(int i = 0; i < 255; i++){

		buffer[i][0] = buffer[i+1][0];
		buffer[i][1] = buffer[i+1][1];
	}
}

void startSampling(){

	//avvio il timer che scandisce l'acquisizione dei campioni
	HAL_TIM_OC_Start_IT(&htim2, TIM_CHANNEL_1);
	//HAL_TIM_OC_Start(&htim2, TIM_CHANNEL_1);
	//abilito il dma per l'adc
	changeTrigger(triggerLevelValue);
	HAL_ADC_Start_DMA(&hadc1, samples, 2);
	//avvio l'adc
	HAL_ADC_Start(&hadc1);
	HAL_ADC_Start_IT(&hadc1);
	//resetto il flag del trigger
	triggerFound = 0;
	bufferReset();

	if (triggerMode == 0){

			sampleIndex = 0;
		} else {

			sampleIndex = 256;
		}

}

void stopSampling(){

	//fermo il timer
	HAL_TIM_OC_Stop_IT(&htim2, TIM_CHANNEL_1);
	//disabilito il dma per l'adc
	HAL_ADC_Stop_DMA(&hadc1);


}

void changeTrigger(uint8_t level){

	  ADC_AnalogWDGConfTypeDef AnalogWDGConfig = {0};
	  AnalogWDGConfig.WatchdogMode = ADC_ANALOGWATCHDOG_SINGLE_REG;
	  AnalogWDGConfig.HighThreshold = level;
	  AnalogWDGConfig.LowThreshold = 0;
	  AnalogWDGConfig.Channel = ADC_CHANNEL_0;
	  AnalogWDGConfig.ITMode = ENABLE;
	  if (HAL_ADC_AnalogWDGConfig(&hadc1, &AnalogWDGConfig) != HAL_OK)
	  {
	    Error_Handler();
	  }
}

void changeSamplingPeriod(uint32_t period){

	uint32_t steps;
	steps = ((period * 2) / 25 )-1;

	__HAL_TIM_SET_AUTORELOAD(&htim2,steps);
}

void samplesTransmission(){

	char begin = '*', end = '#';
	char s1[3],s2[3];

	//fermo il campionamento
	stopSampling();

	HAL_UART_Transmit(&huart2,(uint8_t*)&begin,1,1000);

	for(int i = 0; i < 512; i++){


		sprintf(s1,"%02x",buffer[i][0]);
		sprintf(s2,"%02x",buffer[i][1]);

		HAL_UART_Transmit(&huart2,(uint8_t*)s1,2,1000);
		HAL_UART_Transmit(&huart2,(uint8_t*)s2,2,1000);
	}

	HAL_UART_Transmit(&huart2,(uint8_t*)&end,1,1000);

	if (triggerMode == 0 || triggerMode == 1){

		startSampling();
	} else {

		triggerMode = 3;
	}



}
