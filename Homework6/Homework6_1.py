fileName = input("Enter a file name: ")
stringToBeRemoved = input("Enter a string to be removed: ")

OpenFile = open(fileName, "r")
wordsInFile = []
for line in OpenFile:
    wordsInLine = line.split()
    wordsInFile += wordsInLine
print(wordsInFile)

counter = 0
index = []
numberOfWords = len(wordsInFile)
print(numberOfWords)
for word in wordsInFile:
    if word == stringToBeRemoved:
        index.append(counter)
    counter += 1
print(index)

newList = [word for word in wordsInFile if word != stringToBeRemoved]
print(newList)

newText = ""
for element in newList:
    if element.endswith("."):
        newText += element + "\n"
    else:
        newText += element + " "

print(newText)

outFile = open(fileName,"w")
outFile.write(newText)
outFile.close()





    
