import tkinter as tk
from tkinter.constants import COMMAND
import parser as parse
from rumps.rumps import Window

##76a5af
##f6b26b
 
class App(tk.Tk):
    def __init__(self, master=None):
        tk.Tk.__init__(self, master)
        self.clear = ''
        self.title('OSDA')
        self.geometry('400x400')
        self.txt = tk.Label(self,pady=30,text='Say Something:',foreground='#f6b26b',background='#76a5af')
        self.txt.pack()
        self.output = tk.StringVar(self)
        self.output.set('Output will be displayed here')
        self.rootEntry = tk.Entry(self, textvariable=self.txt,background='#f6b26b',highlightbackground='#c90076')
        self.rootEntry.pack()
        self.bind('<Return>', self.send)
        self.s = tk.Label(self,pady=50,textvariable=self.output,foreground='#f6b26b',background='#76a5af')
        self.s.pack()
        
    def send(self,event=None):
        entryString = self.rootEntry.get()
        parse.call_function(entryString)
        f = open('/Users/timyc1/Desktop/houseofrep/Output.txt','r')
        for line in f:
            if line != '':
                self.output.set(line)
            else:
                self.output.set('')
        f = open('/Users/timyc1/Desktop/houseofrep/Output.txt','w')
        f.write(self.clear)

root = App()
root.configure(background="#76a5af")
root.mainloop()
