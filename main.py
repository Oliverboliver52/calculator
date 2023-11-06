import tkinter as tk
from tkinter import ttk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('650x650')

        self.operation = ""
        self.output = tk.Label(self.root,text="Output")
        self.prevAns = 0
        self.buttons = {
            'one' : ttk.Button(self.root,text="1",command=lambda: self.add('1')),
            'two': ttk.Button(self.root, text="2", command=lambda: self.add('2')),
            'three': ttk.Button(self.root, text="3", command=lambda: self.add('3')),
            'four': ttk.Button(self.root, text="4", command=lambda: self.add('4')),
            'five': ttk.Button(self.root, text="5", command=lambda: self.add('5')),
            'six': ttk.Button(self.root, text="6", command=lambda: self.add('6')),
            'seven': ttk.Button(self.root, text="7", command=lambda: self.add('7')),
            'eight': ttk.Button(self.root, text="8", command=lambda: self.add('8')),
            'nine': ttk.Button(self.root, text="9", command=lambda: self.add('9')),
            'zero': ttk.Button(self.root, text="0", command=lambda: self.add('0')),
            'times': ttk.Button(self.root, text="x", command=lambda: self.add('*')),
            'divide': ttk.Button(self.root, text="/", command=lambda: self.add('/')),
            'add': ttk.Button(self.root, text="+", command=lambda: self.add('+')),
            'subtract': ttk.Button(self.root, text="-",command=lambda: self.add("-")),
            'equals': ttk.Button(self.root, text="=", command=lambda: self.result()),
            'AC': ttk.Button(self.root, text="AC",command=lambda: self.restart()),
            'dot': ttk.Button(self.root,text=".",command=lambda: self.add('.')),
            'brackets1': ttk.Button(self.root,text="(",command=lambda: self.add('(')),
            'brackets2': ttk.Button(self.root, text=")",command=lambda: self.add(')')),
            'ANS': ttk.Button(self.root,text="Ans",command=lambda: self.add(f'{str(self.prevAns)}'))
        }
        x = 0
        y = 1
        self.output.grid(row=0,column=0)
        for i in self.buttons:
            if i == 'times':
                break
            self.buttons[i].grid(row=y,column=x)
            x += 1
            if x % 3 == 0:
                x = 0
                y += 1
        self.buttons['divide'].grid(row=1,column=3)
        self.buttons['times'].grid(row=2,column=3)
        self.buttons['add'].grid(row=3,column=3)
        self.buttons['subtract'].grid(row=4,column=3)
        self.buttons['equals'].grid(row=4,column=2)
        self.buttons['AC'].grid(row=0,column=3)
        self.buttons['dot'].grid(row=4,column=1)
        self.buttons['brackets1'].grid(row=1,column=4)
        self.buttons['brackets2'].grid(row=1,column=5)
        self.buttons['ANS'].grid(row=2,column=4)
    def result(self):
        self.prevAns = eval(self.operation)
        self.output.config(text=str(self.prevAns))
    def add(self,c):
        self.operation += c
        self.output.config(text=self.operation)
    def restart(self):
        self.operation = ""
        print(f'Restart - {self.operation}')
        self.output.config(text=self.operation)
W = Window()
tk.mainloop()
