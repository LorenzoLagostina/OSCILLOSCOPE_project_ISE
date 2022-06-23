from tkinter import ttk
from tkinter import *
from EntryObject import EntryObject
#definisco la lista contenente le unita' di misura 
unitMeasure = ["ms", "us", "ns"]
#definisco il dizionario avente come chiave le unita' di misura e come valore il rapporto
#con il nanosecondo
unitMeasurementsVal = {"ms" : 10 ** (6), "us" : 10 ** (3), "ns" : 10 ** (0)}
#definisco i valori massimi e minimi accettabili
minVal = 10000
maxVal = 100000000

class SamplingPeriod(EntryObject):
    def __init__(self, frame):
        #inizializzo l'oggetto e il menu a tendiana
        super().__init__(frame, "Sampling Period")
        self.unitMeasureCombo = ttk.Combobox(frame, values = unitMeasure, state="readonly" )
        
    def Grid(self, row_start, column_start):
        super().Grid(row_start, column_start)
        #colloco spazialmente il menu a tendina per la scelta delle unita' di misura
        self.unitMeasureCombo.grid(row = row_start, column = column_start + 2, 
                                   sticky = (W, E))
        
    def getValue(self):
        
        if (self.checkValue()):
            #ritorno valore approssimato in nano secondi
            return round(self.value * unitMeasurementsVal[self.unit])
        else:
            return minVal
    
    
    def checkValue(self):
        try:
            #controllo che il valore sia un float
            self.value = float(self.StringVal.get())
            #setto unita' di misura
            self.unit = unitMeasure[self.unitMeasureCombo.current()]
            self.errorString.set("")
            #controllo che il valore sia valido
            if minVal <= self.value * unitMeasurementsVal[self.unit] <= maxVal:
                return True
            else:
                #avviso che il valore e' fuori range
                self.errorString.set("Errore: Valore fuori range")
                return False
        except Exception as e:
            #avviso che il valore inserito non e' valido
            self.errorString.set("Errore: Valore non valido")
            return False
        
    
        
    def DisableEntry(self):
        #in questo modo l'entry sara' disabilitata
        super().DisableEntry()
        self.unitMeasureCombo["state"] = "disabled"
        
    
    def EnableEntry(self):
        #l'entry in questo modo viene abilitata
        super().EnableEntry()
        self.unitMeasureCombo["state"] = "readonly"
        