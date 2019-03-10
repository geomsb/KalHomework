#Credit card number validation

number = int(input("Enter a credit card number here: "))

# Return this number if it is a single digit, otherwise, return # the sum of the two digist


def getDigit (number):
    modulo = number % 10
    div = number // 10
    number = div
    final = modulo*2
    modulo_doub = final % 10
    div_doub = final // 10      
    if final > 9:
        final = modulo_doub + div_doub
    else:
        final = modulo*2
    return (final)

def getDigitOdd (number):
    modulo = number % 10
    div = number // 10
    number = div
    final = modulo

    return (final)
    
# Get the result from Step 2

def sumOfDoubleEvenPlace (number):
    sum_dig = 0
    counter = 0
    while (number)>0:
        counter = counter + 1
        if counter % 2 == 0:
            sum_dig += getDigit (number)
        div = number // 10
        number = div        
            
    return (sum_dig)

# Get the result from Step 3 Return sum of odd place digits in number

def sumOfOddPlace (number):
    sum_dig = 0
    counter = 0
    while (number)>0:
        counter = counter + 1
        if counter % 2 > 0:
            sum_dig += getDigitOdd (number)
            sum_dig_odd = (sum_dig)
        div = number // 10
        number = div
   
    return (sum_dig_odd)

#Return true if the card number is valid

def isValid(number):
    validation = sumOfDoubleEvenPlace (number) + sumOfOddPlace (number)
    if (validation % 10) == 0:
        print("The number of the credit card is valid")
    else:
        print("The number of the credit card is invalid")
        
isValid (number)
