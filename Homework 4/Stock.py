class Stock:
    def __init__(self, symbol, name, stockPreviousPrice, stockCurrentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__stockPreviousPrice = stockPreviousPrice
        self.__stockCurrentPrice = stockCurrentPrice

#Accesor Methods
    def getStockName(self):
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

#Stock's previous price
    def setStockPreviousPrice(self, stockPreviousPrice):
        self.__stockPreviousPrice = stockPreviousPrice

    def getStockPreviousPrice(self):
        return self.__stockPreviousPrice

#Stock's current price
    def setStockCurrentPrice(self, stockCurrentPrice):
        self.__stockCurrentPrice = stockCurrentPrice

    def getStockCurrentPrice(self):
        return self.__stockCurrentPrice

#Change Percent
    def getChangePercent(self):
        percent = ((self.__stockPreviousPrice / self.__stockCurrentPrice)*100)-100
        return percent
