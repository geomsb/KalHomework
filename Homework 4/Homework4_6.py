from Fan import Fan
fan1 = Fan(Fan.fast, 5, "blue", True)
print (fan1.getSpeed())
print(fan1.getRadius())
print(fan1.getColor())
print(fan1.isTurnedOn())

fan2 = Fan(Fan.medium, 5, "blue", False)
print(fan2.getSpeed())
print(fan2.getRadius())
print(fan2.getColor())
print(fan2.isTurnedOn())

fan2.turnOn()
print(fan2.isTurnedOn())