from tkinter import *

class AlternateTwoMessages:
    def __init__(self):
        window = Tk()
        window.title("Alternate Two Messages")
        
        self.textvariable = StringVar()
        button = Button(window, textvariable = self.textvariable, command = self.changeText)
        button.grid(row=1, column=1)

        self.textvariable.set("Programming is fun")       
        
        window.mainloop()
        
    def changeText(self):
        if self.textvariable.get() == "Programming is fun":
            self.textvariable.set("It is fun to program")
        else:
            self.textvariable.set("Programming is fun")

AlternateTwoMessages()