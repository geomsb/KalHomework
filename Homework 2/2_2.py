#Prompt the user for the radius and the lenght of a cilinder

radius, lenght = input("Enter the radius and lenght here separated by a comma: ").split(",")
radius_numb = float(radius)
lenght_numb = float (lenght)

PI = 3.1416

# Calculate area
area = radius_numb * radius_numb * PI
print ("area is", area)

# Calculate volume
volume = area*lenght_numb
print ("volume is", volume)
