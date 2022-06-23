from tkinter import Canvas
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np

class Graph():
    def __init__(self, frame, coordx, coordy):
        # add figure canvas
        fig = Figure();
        #Set line CH1
        self.CH_ax = fig.add_subplot(111)
        #setto il titolo e il nome degli assi
        self.CH_ax.set_title('Oscilloscope');
        self.CH_ax.set_xlabel('Samples')
        self.CH_ax.set_ylabel('Value Channel [V]')
        #setto i limiti degli assi
        self.CH_ax.set_xlim(0,256)
        self.CH_ax.set_ylim(0, 3.3)
        
        self.CH0_line = self.CH_ax.plot([], [])[0]
        self.CH1_line = self.CH_ax.plot([], [])[0]
        
        #imposto la figura del grafico
        self.canvas = FigureCanvasTkAgg(fig, master=frame)
        #imposto la grandezza del grafico
        self.canvas.get_tk_widget().place(width = 256,height = 256)
        #imposto le coordinate del frame
        self.canvas.get_tk_widget().grid(row = coordx, column = coordy)
        self.canvas.draw()
        
    def setValues(self, line1, line2,trigPos):
        #setto i valori dei 2 canali
        self.CH0_line.set_ydata(np.append([], line1[128+trigPos:384+trigPos]) / 256 * 3.3)
        self.CH0_line.set_xdata(np.arange(0, 256))
        self.CH1_line.set_ydata(np.append([], line2[128+trigPos:384+trigPos]) / 256 * 3.3)
        self.CH1_line.set_xdata(np.arange(0, 256))
        
        #disegno le linee
        self.canvas.draw()
        
    
        