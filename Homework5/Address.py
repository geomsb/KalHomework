class Address:
    def __init__ (self, name, street, city, state, zipCode):
        self.__name = name
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode

    def getName(self):
        return self.__name
    def getStreet(self):
        return self.__street
    def getCity(self):
        return self.__city
    def getState(self):
        return self.__state    
    def getZipCode (self):
        return self.__zipCode
