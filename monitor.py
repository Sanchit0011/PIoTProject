import os
import time
from sense_hat import SenseHat


class monitor:
    def getHumidity(self):
        sense = SenseHat()
        humidity = sense.get_humidity()
        return(humidity)
    
    def getTime(self):
        date = datetime.datetime.now()
        return(date)


reading = monitor()
reading.getHumidity()
reading.getTime()