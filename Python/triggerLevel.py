from tkinter import *
from tkinter import ttk
from EntryObject import EntryObject


class TriggerLevel(EntryObject):
    def __init__(self, frame, nomeLabel, valMin, valMax):
        #inizializzo oggetto con valore massimo e minimo scelti
        super().__init__(frame, nomeLabel)
        self.valMin = valMin
        self.valMax = valMax
        #aggiungo una label in cui vi sara' scritto LSB
        self.unitMeasurements = ttk.Label(frame, text = "LSB")
        
        
       
        
        
    def Grid(self, row_start, column_start):
        #posiziono oggetto
        super().Grid(row_start, column_start)
        self.unitMeasurements.grid(row = row_start, column = column_start + 2, sticky = (W))
        
        
    def checkValue(self):
        try:
            #controllo che il valore sia valido
            self.value = int(self.StringVal.get())
            #controllo che il valore sia nel range
            if self.valMin <= self.value <= self.valMax:
                self.errorString.set("")
                return True
            else:
                #se non e' nel range do' segnalazione di errore
                self.errorString.set("Errore: Valore fuori range")
                return False

        
        except Exception as e:
            #qualora non sia stato inserito nulla, il valore di default sara' 0
            if self.StringVal.get() == "":
                self.value = 0
                return True
            else:
                #do' segnalazione di errore qualora il valore inserito non sia valido
                self.errorString.set("Errore: Valore non valido")
            
                return False
    
            
            
            
        
        
