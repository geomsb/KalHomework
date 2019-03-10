# Return the reversal of an integer

def reverse (number):
    rev = 0
    while number > 0:
        modulo = number % 10 
        div = number // 10
        number = div
        rev = (modulo + rev)*10
        
    final = rev // 10
    
    return (final)
    

# Return true if number is a palindrome

def isPalindrome(number):
    if reverse (number) == number:
        return True
    else:
        return False

number = int(input("Enter a number here: "))

if isPalindrome(number) == True:
    print("The integer is a palindrome")

else:
    print("The integer is not a palindrome")
    



