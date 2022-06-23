from tkinter import *
from tkinter import ttk
from serial.tools import list_ports
import serial

def runSerial(*args):
    try:
        global ser
        global valid
        #Tolgo segnalazione di eventuale errore
        ErrorStringSerial.set("")
        #apro seriale selezionata
        valSerial = serialCombo.current()
        ser = serial.Serial((str(portSerial[valSerial]).split(" "))[0], 115200, timeout = 0.2)
        #cambio status a variabile valid
        #do in questo modo indicazione che seriale selezionata corretta
        valid = True
        #distruggo finestra in quanto non necessaria
        window.destroy()
    except Exception:
        ErrorStringSerial.set("Porta seriale non valida")
    
window = Tk()
#setto il frame della finestra
mainframeSerial = ttk.Frame(window, padding = "6 6 12 12")
mainframeSerial.grid(column=0, row=0, sticky=(N,W,E,S))
mainframeSerial.columnconfigure(0, weight=1)
mainframeSerial.rowconfigure(0, weight=1)

valid = False

portSerial = list_ports.comports()
#fornisco tutte le possibili uscite seriale a disposizione
serialCombo = ttk.Combobox(mainframeSerial, values = portSerial, state = "readonly")
serialCombo.grid(row = 0, column = 0)
#Bottone per dare indicazione di conferma scelta
ButtonStart = ttk.Button(mainframeSerial, text="RUN",command=runSerial)
ButtonStart.grid(row = 0, column = 1)
#Entry utile per dare indicazione di errore nella seriale scelta
ErrorStringSerial = StringVar()
ErrorEntry = ttk.Entry(mainframeSerial, state="readonly", textvariable=ErrorStringSerial)
ErrorEntry.grid(row = 1, column = 0)
for child in mainframeSerial.winfo_children():
        child.grid_configure(padx=5, pady=5)
window.bind("<Return>", runSerial)
window.mainloop()
    
    