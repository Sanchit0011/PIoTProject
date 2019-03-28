import subprocess as sp
import os
import bluetooth

class greenHouseBluetooth:
    
    def scanDevices(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print("found %d devices" % len(nearby_devices))
        
        for addr, name in nearby_devices:
            print("  %s - %s" % (addr, name))
            
    
    def listPairedDevices(self):
        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines()
        print(data)
        
    # def sendPushNotification:
        
    
    
device = greenHouseBluetooth()
device.scanDevices()
device.listPairedDevices()