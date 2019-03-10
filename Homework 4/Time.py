import datetime
import time

class Time:
    def __init__(self):
        now = datetime.datetime.now()
        self.__hour = now.hour
        self.__minute = now.minute 
        self.__second = now.second
        self.__currentElapsedTime = time.time()

#Accesor Methods
    def getHour(self):
            return self.__hour

    def getMinute(self):
            return self.__minute

    def getSecond(self):
            return self.__second

    def setTime(self, elapsedTime):
        newTimeSeconds = elapsedTime + self.__currentElapsedTime
        self.__hour = newTimeSeconds // 3600 % 24
        self.__minute = (newTimeSeconds % 3600) // 60
        self.__second = round((newTimeSeconds % 3600) % 60,0)

    def printNewTime(self):
        print("The hour:minute:second for the elapsed time is " + str(self.__hour) + ":" + str(self.__minute) + ":" + str(self.__second))
