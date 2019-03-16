fileName = input("Enter a file name: ")

OpenFile = open(fileName, "r")

counter = 0
wordsInFile = []
for line in OpenFile:
    wordsInLine = line.split()
    wordsInFile += wordsInLine
    counter +=1

totalLines = counter
totalWords = len(wordsInFile)

listOfWords = [word for word in wordsInFile]

characters = ''
for word in listOfWords:
    characters += word
totalCharacters = len(characters)

print ("Characters: " + str(totalCharacters))
print("Words: " + str(totalWords))
print("Lines: " + str(totalLines))
