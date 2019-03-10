# Pentagonal numbers

def getPentagonalNumber (n):
    return int((n*(3*n-1)/2)) 

for number in range (100):
    if number % 10 == 0:
        print()
    print ((getPentagonalNumber (number+1)), end=" ")

