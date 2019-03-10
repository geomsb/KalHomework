# Sum the digits in an integrer

digits = int(input("Enter a number between 0 and 1000: "))

modulo1 = digits % 10

division_floor1 = digits // 10

if digits == 1000:

    division_floor2 = division_floor1 // 100

else:
    division_floor2 = division_floor1 // 10
   

modulo2 = division_floor1 % 10

result = modulo1 + division_floor2 + modulo2

print("The sum of the digits is " + str(result))
    

