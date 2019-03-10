from QuadraticEcuation import QuadraticEcuation

listOfStrings = input ("Enter a,b,c here separated by a coma: ").split(',')

a,b,c = [int(string) for string in listOfStrings]

QuadraticEcuation1 = QuadraticEcuation(a,b,c)
QuadraticEcuation1.display()


