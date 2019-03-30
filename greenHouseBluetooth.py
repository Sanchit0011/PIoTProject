import subprocess as sp
import os
import bluetooth
from pushbullet.pushbullet import PushBullet

class greenHouseBluetooth:
    
    def scanDevices(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        #print(nearby_devices)
        
        #print("found %d devices" % len(nearby_devices))
        
        #for addr, name in nearby_devices:
           # print("  %s - %s" % (addr, name))
            
        
    #def sendPushNotification(self):
        apiKey = "o.yVczv6qpQuZIKF8zaPImpIxIxw0evUIp"
        p = PushBullet(apiKey)
        
        # Getting a list of devices
        pushbulletDevices = p.getDevices()
        print(nearby_devices)
            if pushbulletDevices[0].get("nickname") in nearby_devices:
                print("Found device with names: ", nearby_devices)
                p.pushNote(devices[0]["iden"], 'Raspberry-Pi-Notification','')

device = greenHouseBluetooth()
device.scanDevices()