# Calculate energy

m = float( input ("Enter the amount of water in kilograms: "))

initial_temperature = float ( input ("Enter the initial temperature: "))

final_temperature = float ( input ("Enter the final temperature: "))

q = m * (final_temperature - initial_temperature) *4184

print ("The energy needed is " + str(q))
                            
