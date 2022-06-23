#include <stdint.h>
#include "main.h"
#include <stdio.h>
#include <string.h>
#ifndef UTILITIES
#define UTILITIES

//dichiaro gli handler delle periferiche
ADC_HandleTypeDef hadc1;
DMA_HandleTypeDef hdma_adc1;

TIM_HandleTypeDef htim2;

UART_HandleTypeDef huart2;

//dichiaro la variabile in cui salvare i campioni dal dma
extern uint32_t samples[2];

//dichiaro il buffer per i campioni
uint8_t buffer[513][2];
//dichiaro l'indice relativo al campione da salvare
volatile uint16_t sampleIndex;
//dichiaro la variabile necessaria a salvare l'arrivo del trigger
volatile uint8_t triggerFound;
//dichiaro la variabile necessaria a salvare il livello del trigger
volatile uint8_t triggerLevelValue;
//dichiaro la modalita' del trigger
uint8_t triggerMode;
//dichiaro le funzioni per fermare e far partire il timer
void startSampling();
void stopSampling();

//dichiaro le funzioni per cambiare il livello di trigger ed il periodo di campionamento
void changeTrigger(uint8_t level);
void changeSamplingPeriod(uint32_t period);

//dichiaro la funzione per il reset del buffer
void bufferReset();
//dichiaro la funzione per shiftare i primi 255 valori del buffer
//in questo modo potro' avere i valori precedenti al trigger sul grafico
void bufferShift();

//dichiaro la funzione relativa all'invio dei campioni
void samplesTransmission();

#endif
