import serial
from serial.tools import list_ports
from tkinter import *
from tkinter import ttk
from graph import Graph
from triggerLevel import TriggerLevel
from samplingPeriod import SamplingPeriod
from triggerMode import TriggerMode
from SerialChoosePort import *
import time

#variabili globali per quanto riguarda la modalita' di lavoro dell'interfaccia
runMode = False
sendCommStatus = False



def ReadElement():
    try:
        global runMode
    
        ser.reset_input_buffer()
        #leggo 1 byte
        byteToRead = ser.read(1)
        #print(byteToRead)
        CH0 = []
        CH1 = []
        #se il byte letto coincide con il carattere *
        # e mi trovo in run mode continuo a leggere
    
        if str(byteToRead, 'utf-8') == "*" and runMode:
            #leggo 1 byte
            byteToRead = ser.read(1)
            valFound = ""
            firstDigit = False
            Channel0 = True
            #leggo e faccio elaborazione fin quando il byte letto e' diverso da # 
            while str(byteToRead, 'utf-8') != "#":
                #se il primo digit lo salvo in una stringa
                if not firstDigit:
                    firstDigit = True
                    valFound = str(byteToRead, 'utf-8')
                else:
                    #altrimenti aggiungo in append valore a stringa
                    firstDigit = False
                    valFound += str(byteToRead, 'utf-8')
                    #trasformo valore in intero e lo salvo sulla lista corrispondende
                    #al canale a cui appartiene il numero
                    if Channel0:
                        CH0.append(int(valFound, 16))
                        Channel0 = False
                    else:
                        CH1.append(int(valFound, 16))
                        Channel0 = True
                    valFound = ""
                #leggo prossimo byte
                byteToRead = ser.read(1)
            #mando i valori trovati al grafico al fine da poterli graficare
            graph.setValues(CH0, CH1, TriggerPositionObj.getValue())
    except Exception as e:
        pass
        print(e)
    
            


#funzione che permette di inviare i dati di impostazioni al micro
def WriteElement(valueTriggerLevel, valuePeriodSample, valueTriggerMode):
    #invio dei comandi secondo le specifiche
    ser.write(bytes("*TL" + format(valueTriggerLevel, "02x") + "#", "utf-8" ))
    ser.write(bytes("*SP" + format(valuePeriodSample, "08x") + "#", "utf-8" ))
    ser.write(bytes("*TT" + format(valueTriggerMode, "02x") + "#" , "utf-8"))

#funzione che gestisce i casi il comportamento della seriale
def behSerial():
    global sendCommStatus
    global runMode
    #se devo inviare dei comandi
    if sendCommStatus:
        #funzione che invia i vari comandi
        WriteElement(TriggerLevelObj.getValue(), PeriodObj.getValue(), ModeObj.GetValue())
        #cambio gli stati alle 2 variabili globali
        sendCommStatus = False
        runMode = True
    elif runMode:
        #Se sono in run mode mi occupo di leggere
        ReadElement() 

    #dopo 1 millisecondo richiamo questa funzione al fine da controllare
    #in polling cosa fare
    root.after(1, behSerial)
           

def sendCommands(*args):
    try:
        global runMode
        global sendCommStatus
        #controllo se sono in run mode
        if not(runMode):
            
            #controllo che i valori inseriti siano corretti
            if TriggerLevelObj.checkValue() and PeriodObj.checkValue() and TriggerPositionObj.checkValue():
                #nel caso cambio la variabile globale sendCommStatus                
                sendCommStatus = True
                
                
                #Disabilito i permessi di modifica ai vari oggetti presenti all'interfaccia
                TriggerLevelObj.DisableEntry()
                PeriodObj.DisableEntry()
                ModeObj.Disable()
                TriggerPositionObj.DisableEntry()
                
                #Change text button
                runStop_Button["text"] = "STOP"
                
                              
                
                
                
        else:
            #invio uno stop
            ser.write(bytes("*TT03#" , "utf-8"))
            
            #cambio lo stato alla variabile run mode
            runMode = False
            
            #abilito i permessi di modifica delle entry 
            #e delle combobox presenti all'interfaccia
            
            ModeObj.Enable()
            TriggerLevelObj.EnableEntry()
            TriggerPositionObj.EnableEntry()
            PeriodObj.EnableEntry()


            #cambio il nome al bottone
            runStop_Button["text"] = "RUN"
            
    except Exception as e:
        print(e)
        pass

#finche' dato seriale non aperta aspetto
global valid
while not valid:
    time.sleep(1)



#dichiarazione root
root = Tk()
root.title("Oscilloscope")
#dichiarazione main frame e configurazione
mainframe = ttk.Frame(root, padding = "6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#uso la seriale aperta precedentemente
global ser
try:
    
    #posiziono grafico
    graph = Graph(mainframe, 5, 4)
    
    #gestisco l'oggetto per quanto concerne la scelta del livello
    # di trigger
    TriggerLevelObj = TriggerLevel(mainframe, "Trigger Level", 0, 255)
    TriggerLevelObj.Grid(0, 0)
    
    #gestisco l'oggetto per la selezione del periodo di sample
    PeriodObj = SamplingPeriod(mainframe)
    PeriodObj.Grid(0, 5)
    
    #gestione oggetto trigger position
    TriggerPositionObj = TriggerLevel(mainframe, "Trigger Position", -128, 128)
    TriggerPositionObj.Grid(2, 5)
    
    #definisco l'oggetto comprensivo di combobox e label
    #per quanto concerne la selezione del tipo di trigger
    ModeObj = TriggerMode(mainframe)
    ModeObj.Grid(2, 0)
    
    #definisco il bottone per l'esecuzione dell'oscilloscopio
    runStop_Button = ttk.Button(mainframe, text="RUN",command=sendCommands)
    runStop_Button.grid(row=6, column=0, sticky=(W,E))
    
    root.update()
    #ogni millisecondo viene chiamata la funzione che gestisce
    # il comportamento della seriale
    root.after(1, behSerial)
    
    
    #configurazione finestra
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
    root.bind("<Return>", sendCommands)
    root.update()
    root.mainloop()
    #chiusura seriale
    ser.close()

except Exception as e:
    #stampo eventuale errore
    print(e)    
    
    
