# Find the number of years and days

minutes = int(input ("Enter the number of minutes here: "))

hours = minutes // 60

total_days = hours // 24

years = total_days // 365

days = total_days % 365

if days == 0:

    print ( str(minutes) + " minutes is approximately " + str(years))

else:

    print ( str(minutes) + " minutes is approximately " + str(years) + " years and " + str(days) + " days")

