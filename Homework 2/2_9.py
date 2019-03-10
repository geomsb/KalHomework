# Calculate wind-chill temperature

ta = float (input ("Enter the temperaure in Fahrenheit between -58 and 41: "))

v = float (input ("Enter the wind speed in miles per hour: "))

twc = 35.74 + .6215*(ta) - 35*(v**.16) + .4275*(ta)*(v**.16)

if v >= 2:  
    print ("The wind chill index is: " + str(twc))
    
else:
    print ("The formula only works if the wind speed is greater than or equal to 2")
     
