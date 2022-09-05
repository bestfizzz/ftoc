from functools import partial
import tkinter as tk
window=tk.Tk()
window.title('tempature converter')
def calFTC():
    pass
def cToF():
    def calCTF():
        celsius=int(temp.get())
        Fahrenheit = (celsius * 1.8) + 32  
        lb2["text"]= f'{Fahrenheit}°F'
        celsius=(Fahrenheit-32)/1.8
    lb=tk.Label(text='°C',anchor=tk.E)
    lb2=tk.Label(text='°F',width=15,anchor=tk.E)
    btn=tk.Button(text='=>',command=calCTF)
    temp=tk.Entry()
    swapp=tk.Button(text='swap',command=fToC)
    temp.grid(row=0,column=0)
    lb.grid(row=0,column=1)
    btn.grid(row=0,column=2)
    lb2.grid(row=0,column=3,sticky='E')
    swapp.grid(row=0,column=4)
def fToC():
    def calFTC():
        Fahrenheit=int(temp.get())
        celsius=(Fahrenheit-32)/1.8
        lb2["text"]= f'{celsius}°C'
    lb=tk.Label(text='°F',anchor=tk.E)
    lb2=tk.Label(text='°C',width=15,anchor=tk.E)
    btn=tk.Button(text='=>',command=calFTC)
    temp=tk.Entry()
    swapp=tk.Button(text='swap',command=cToF)
    temp.grid(row=0,column=0)
    lb.grid(row=0,column=1)
    btn.grid(row=0,column=2)
    lb2.grid(row=0,column=3,sticky='E')
    swapp.grid(row=0,column=4)
cToF()
window.mainloop()