from QuadraticEquation import QuadraticEquation

listOfStrings = input ("Enter a,b,c here separated by a coma: ").split(',')

a,b,c = [int(string) for string in listOfStrings]

QuadraticEquation1 = QuadraticEquation(a,b,c)
QuadraticEquation1.display()


