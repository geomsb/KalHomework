# Calculate tips

subtotal, gratuity_rate = input("Enter the subtotal and gratuity here separated by a comma: ").split(",")
                            
subtotal_number = float(subtotal)
gratuity_rate_number = float (gratuity_rate)/100

tip = round (subtotal_number * gratuity_rate_number, 2)

total = round (subtotal_number + tip, 2)

print ("The gratuity is " + str(tip) + " and the total is " + str(total))


            
