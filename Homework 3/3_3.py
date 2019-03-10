# Approximate the square root

def sqrt (n):

    initialGuess = 1
    lastGuess = initialGuess
    while (n) >= 1:
        nextGuess = (lastGuess + ((n)/lastGuess))/ 2
        if abs (nextGuess - lastGuess) <= .0001:
            return (nextGuess)
        lastGuess = nextGuess

print (sqrt (16))






