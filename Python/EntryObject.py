from tkinter import *
from tkinter import ttk

class EntryObject():
    def __init__(self, frame, nameObject):
        #definisco un oggetto Entry Object
        #questo è costituito da una entry in cui inserire il valore
        self.StringVal = StringVar()
        self.entry = ttk.Entry(frame, textvariable = self.StringVal)
        #una entry in cui inserire l'eventuale messaggio di errore
        self.errorString = StringVar()
        self.error = ttk.Entry(frame, textvariable = self.errorString)
        #faccio in modo che il messaggio di errore sia read only
        self.error["state"] = "readonly"
        
        #una label per far capire il parametro richiesto
        self.label = ttk.Label(frame, text = nameObject)
        
        #il valore del parametro
        self.value = 0
        
        
        
    def DisableEntry(self):
        #in questo modo l'entry sara' disabilitata
        self.entry["state"] = "disabled"
    
    def EnableEntry(self):
        #l'entry in questo modo viene abilitata
        self.entry["state"] = "normal"
        
    def Grid(self, row_start, column_start):
        #vengono posizionati i vari elementi secondo quanto deciso
        self.entry.grid(row = row_start, column = column_start + 1, sticky = (W))
        self.label.grid(row = row_start, column = column_start, sticky =(E))
        self.error.grid(row = row_start + 1, column = column_start + 1, sticky = (W,E))
        
    def getValue(self):
        #ritornerà il valore dell'entry
        return self.value
        
    