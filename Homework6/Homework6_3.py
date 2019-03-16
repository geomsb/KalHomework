import random
from pathlib import Path

fileName = input ("Enter a file name: ")
listOfNumbers = []
for i in range(100):
    listOfNumbers.append(random.randint(1,101))

totalOfNumbers = ''
for number in listOfNumbers:
    totalOfNumbers += str(number) + " "

config = Path(fileName)
if config.is_file():    
    print("The file already exists")
    
else:
    outFile = open(fileName,"x")
    outFile.write(totalOfNumbers)
    outFile.close()

    openFile = open(fileName, "r")
    numbersInFileStr = []
    for line in openFile:
        numbersInLine = line.split()
        numbersInFileStr += numbersInLine

numbersInFileInt = list(map(int,numbersInFileStr))
sortedNumbers = sorted(numbersInFileInt)
print(sortedNumbers)
