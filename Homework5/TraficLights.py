from tkinter import *


class TrafficLights:
    def __init__(self):

        window = Tk()
        window.title("Traffic Light")

        frame = Frame(window)
        frame.grid(row=2)

        self.var = IntVar()
        redRadio = Radiobutton(frame, text="Red", variable=self.var, value=1, command = self.RadioChange)
        redRadio.grid(row=1, column=1)

        yellowRadio = Radiobutton(frame, text="Yellow", variable=self.var, value=2, command = self.RadioChange)
        yellowRadio.grid(row=1, column=2)
        
        greenRadio = Radiobutton(frame, text="Green", variable=self.var, value=3, command = self.RadioChange)
        greenRadio.grid(row=1, column=3)

        self.canvas = Canvas(window, width=200, height=340, bg="white" )
        self.canvas.grid(row=1)

        self.oval_red = self.canvas.create_oval(50, 10, 160, 110, fill="white")
        self.oval_yellow = self.canvas.create_oval(50, 120, 160, 220, fill="white")
        self.oval_green = self.canvas.create_oval(50, 230, 160, 330, fill="white")

        window.mainloop()

    def RadioChange(self):
        if self.var.get () == 1:
            self.canvas.itemconfig(self.oval_red, fill="red")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="white")

        if self.var.get () == 2:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            self.canvas.itemconfig(self.oval_green, fill="white")

        if self.var.get () == 3:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")

TrafficLights()