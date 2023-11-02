import tkinter as tk

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('650x650')

        self.operation = ""
        self.output = tk.Label(self.root,text="Output")
        self.buttons = {
            'one' : tk.Button(self.root,text="1",command=lambda: self.add('1')),
            'two': tk.Button(self.root, text="2", command=lambda: self.add('2')),
            'three': tk.Button(self.root, text="3", command=lambda: self.add('3')),
            'four': tk.Button(self.root, text="4", command=lambda: self.add('4')),
            'five': tk.Button(self.root, text="5", command=lambda: self.add('5')),
            'six': tk.Button(self.root, text="6", command=lambda: self.add('6')),
            'seven': tk.Button(self.root, text="7", command=lambda: self.add('7')),
            'eight': tk.Button(self.root, text="8", command=lambda: self.add('8')),
            'nine': tk.Button(self.root, text="9", command=lambda: self.add('9')),
            'zero': tk.Button(self.root, text="0", command=lambda: self.add('0')),
            'times': tk.Button(self.root, text="x", command=lambda: self.add('*')),
            'divide': tk.Button(self.root, text="/", command=lambda: self.add('/')),
            'add': tk.Button(self.root, text="+", command=lambda: self.add('+')),
            'subtract': tk.Button(self.root, text="-",command=lambda: self.add("-")),
            'equals': tk.Button(self.root, text="=", command=lambda: self.result()),
            'AC': tk.Button(self.root, text="AC",command=lambda: self.restart())
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
    def result(self):
        print(eval(self.operation))
        self.output.config(text=str(eval(self.operation)))
    def add(self,c):
        self.operation += c
        self.output.config(text=self.operation)
    def restart(self):
        self.operation = ""
        print(f'Restart - {self.operation}')
        self.output.config(text=self.operation)
W = Window()
tk.mainloop()
