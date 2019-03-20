import os
from sense_hat import SenseHat


class monitor:
    def getHumidity(self):
        sense = SenseHat()
        humidity = sense.get_humidity()
        return(humidity)
       
    def getTime(self):
        date = datetime.datetime.now()
        return(date)

    def get_cpu_temp(self):
        res = os.popen("vcgencmd measure_temp").readline()
        temp = float(res.replace("temp=", "").replace("'C\n", ""))
        return(temp)

    def calc_acc_temp(self):
        sense = SenseHat()
        temp = sense.get_temperature_from_pressure()
        temp_cpu = self.get_cpu_temp()
        temp_acc = temp - ((temp_cpu-temp)/1.5)
        return(temp_acc)
