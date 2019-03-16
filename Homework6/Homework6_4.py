from tkinter import *

fileName = input("Enter a file name: ")

# Create the canvas
window = Tk()
myCanvas = Canvas(window, width=400, height =400, background = "white")
myCanvas.grid(row=0, column=0)

# Create the lists
openFile = open(fileName, 'r')
dictionary = {}
for line in openFile:
    numbersInLineStr = line.split()
    numbersInLineInt = list(map(int,numbersInLineStr))
    verticeNumber = numbersInLineInt[0]
    if len(numbersInLineInt) > 1:
        dictionary[verticeNumber] = (numbersInLineInt[1],numbersInLineInt[2])
    print(dictionary)
    for number in numbersInLineInt[3:]:
        if number in dictionary:
            myCanvas.create_line(dictionary[verticeNumber], dictionary[number], fill = "black")

window.mainloop()