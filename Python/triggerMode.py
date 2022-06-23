from tkinter import *
from tkinter import ttk

#lista in cui sono contenute le varie modalita'
mode = ["AUTO", "NORMAL", "SINGLE RUN", "STOP"]
class TriggerMode():
    def __init__(self, frame):
        #inizializzo l'oggetto comprensivo di menu a tendina e label
        self.combo = ttk.Combobox(frame, values = mode, state="readonly")
        self.label = ttk.Label(frame, text="Trigger Mode")
        
    def Grid(self, row_start, column_start):
        #posiziono oggetto secondo i dati passati dalla funzione
        self.combo.grid(row = row_start, column = column_start + 1, sticky = (W))
        self.label.grid(row = row_start, column = column_start, sticky =(E))
    
    
    def Disable(self):
        #in questo modo l'entry sara' disabilitata
        self.combo["state"] = "disabled"
    
    def Enable(self):
        #l'entry in questo modo viene abilitata
        self.combo["state"] = "readonly"
        
    def GetValue(self):
        #se viene selezionato un'opzione 
        #il valore sara' corrispondente all'opzione scelta
        if self.combo.current() >= 0:
            return self.combo.current()
        else:
            #la modalita' di default sara' lo stop
            return 3
