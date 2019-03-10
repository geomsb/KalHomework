class Fan:
    slow = 1
    medium = 2
    fast = 3
    def __init__ (self, speed = slow, radius = 5, color = "blue", isTurnedOn = False):
        self.__speed = speed 
        self.__radius = radius
        self.__color= color
        self.__isTurnedOn = isTurnedOn

#Mutator methods
    def setSpeed(self, speed):
        self.__speed = speed 

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color 

    def turnOn(self):
        self.__isTurnedOn = True
    
    def turnOff(self):
        self.__isTurnedOn = False
    
#Accesor methods
    def getSpeed(self):
        return self.__speed

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def isTurnedOn(self):
        return self.__isTurnedOn