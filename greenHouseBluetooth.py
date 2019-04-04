import subprocess as sp
import json
import os
import bluetooth
from pushbullet.pushbullet import PushBullet
import notifyPushbullet


class greenHouseBluetooth:

    # Creating monitor class object and getting current temp, humidity
    npb = notifyPushbullet.notifyPushbullet()
    temp = npb.temperature
    humid = npb.humidity

    def scanDevices(self):
        print("Scanning nearby bluetooth devices...")
        nearbyDevices = bluetooth.discover_devices(lookup_names=True)

        for name in nearbyDevices:
            return(name)

    def sendPushNotification(self):
        apiKey = "o.BpgNSJ77CGxsWEz2CUJWkDI0oI8hYGoq"
        p = PushBullet(apiKey)
        # Getting a list of devices
        devices = p.getDevices()

        # Specifying relative path
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        # Loading config.json file
        with open(rel_path + 'config.json', 'r') as f:
            config_dict = json.load(f)

        i = 1
        while i < 10:
            deviceList = self.scanDevices()
            print(deviceList)
            if devices[0].get("nickname") in deviceList:
                print("Device found. Sending notification...")
                print(self.humid)
                print(self.temp)
                # Check if the readings are out of range
                # Send pushbullet notification based on readings status
                if self.humid < config_dict['min-humidity']:
                    if self.temp < config_dict['min-temperature']:
                        range1 = config_dict['min-humidity'] - self.humid
                        range2 = config_dict['min-temperature'] - self.temp
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees lower than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    elif self.temp > config_dict['max-temperature']:
                        range1 = config_dict['min-humidity'] - self.humid
                        range2 = self.temp - config_dict['max-temperature']
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees higher than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    else:
                        range = config_dict['min-humidity'] - self.humid
                        comment = 'The humidity is ' + str(round(range, 2))
                        comment = comment + '% lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                elif self.humid > config_dict['max-humidity']:
                    if self.temp < config_dict['min-temperature']:
                        range1 = self.humid - config_dict['max-humidity']
                        range2 = config_dict['min-temperature'] - self.temp
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees lower than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    elif self.temp > config_dict['max-temperature']:
                        range1 = self.humid - config_dict['max-humidity']
                        range2 = self.temp - config_dict['max-temperature']
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees higher than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    else:
                        range = self.humid - config_dict['max-humidity']
                        comment = 'The humidity is ' + str(round(range, 2))
                        comment = comment + '% higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                elif self.temp < config_dict['min-temperature']:
                    if self.humid < config_dict['min-humidity']:
                        range1 = config_dict['min-humidity'] - self.humid
                        range2 = config_dict['min-temperature'] - self.temp
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees lower than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    elif self.humid > config_dict['max-humidity']:
                        range1 = self.humid - config_dict['max-humidity']
                        range2 = config_dict['min-temperature'] - self.temp
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees lower than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    else:
                        range = config_dict['min-temperature'] - self.temp
                        comment = 'The temperature is ' + str(round(range, 2))
                        comment = comment + ' degrees lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                elif self.temp > config_dict['max-temperature']:
                    if self.humid < config_dict['min-humidity']:
                        range1 = config_dict['min-humidity'] - self.humid
                        range2 = self.temp - config_dict['max-temperature']
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees higher than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% lower than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    elif self.humid > config_dict['max-humidity']:
                        range1 = self.humid - config_dict['max-humidity']
                        range2 = self.temp - config_dict['max-temperature']
                        comment = 'The temperature is ' + str(round(range2, 2))
                        comment = comment + ' degrees higher than the limit '
                        comment = comment + 'and the humidity is '
                        comment = comment + str(round(range1, 2))
                        comment = comment + '% higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                    else:
                        range = self.temp - config_dict['max-temperature']
                        comment = 'The temperature is ' + str(round(range, 2))
                        comment = comment + ' degrees higher than the limit'
                        p.pushNote(devices[0]["iden"], 'Bluetooth', comment)

                i = 10
            # If the device is not found
            else:
                print("Device not found")
                i = i+1
# Creating the object and calling the function
device = greenHouseBluetooth()
device.sendPushNotification()
