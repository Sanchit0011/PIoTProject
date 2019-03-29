import os
from sense_hat import SenseHat
from datetime import datetime

# Defined monitor class


class monitor:

    # Function to get current humidity
    def getHumidity(self):
        sense = SenseHat()
        humidity = sense.get_humidity()
        return(humidity)

    # Function to get current date
    def getDate(self):
        sense = SenseHat()
        dateobj = datetime.now()
        year = dateobj.year
        month = dateobj.month
        day = dateobj.day
        date = str(year) + "-" + str(month) + "-" + str(day)
        return(date)

    # Function to get current time
    def getTime(self):
        sense = SenseHat()
        dateobj = datetime.now()
        time = str(dateobj.hour) + ":" + str(dateobj.minute)
        return(time)

    # Function to get current cpu temperature
    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        temp = float(res.replace("temp=", "").replace("'C\n", ""))
        return(temp)

    # Function to calculate accurate temperature
    def calc_acc_temp(self):
        sense = SenseHat()
        temp = sense.get_temperature_from_pressure()
        temp_cpu = self.get_cpu_temp()
        temp_acc = temp - ((temp_cpu-temp)/1.5)
        return(temp_acc)

m = monitor()
m.getTime()
