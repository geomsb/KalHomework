import time
class StopWatch:
    def __init__(self):
        self.__startTime = time.clock()
        self.__endTime = 0 

#Accesor Methods
    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

#Methods

    def start(self):
        self.__startTime = time.clock()

    def stop(self):
        self.__endTime = time.clock()

    def getElapsedTime (self):
            elapsedTime = self.__endTime - self.__startTime
            return elapsedTime