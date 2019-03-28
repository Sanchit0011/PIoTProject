# File which sends pushbullet notification based on readings status

# Imported necessary modules
from monitor import monitor
from pushbullet.pushbullet import PushBullet
import database
import json
import os

# Defined notifyPushbullet class


class notifyPushbullet:

    # Created monitor class object and got current temp, humidity
    monitorobj = monitor()
    temperature = monitorobj.calc_acc_temp()
    humidity = monitorobj.getHumidity()

    # Function to send pushbullet notification based on readings status
    def notify(self):
        self.notified = 0
        comment = ""

        # Got current date and created database object
        date = self.monitorobj.getDate()
        db = database.database()

        # Specified device api key and created PushBullet object
        apiKey = "o.yVczv6qpQuZIKF8zaPImpIxIxw0evUIp"
        p = PushBullet(apiKey)

        # Get list of devices
        devices = p.getDevices()

        # Specified relative path
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        # Loaded config.json file
        with open(rel_path + 'config.json', 'r') as f:
            config_dict = json.load(f)

        # Created connection to db
        # Retrieved data to check if notification is sent
        conn = db.create_conn()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM READINGS WHERE NOTIFIED = 1 AND DATE = ?
        LIMIT 1;''', [str(date)])
        rows = cur.fetchall()

        # Checked if readings are out of range
        # Sent pushbullet notification based on readings status
        if self.humidity < config_dict['min-humidity']:
            if self.temperature < config_dict['min-temperature']:
                range1 = config_dict['min-humidity'] - self.humidity
                range2 = config_dict['min-temperature'] - self.temperature
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees lower than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            elif self.temperature > config_dict['max-temperature']:
                range1 = config_dict['min-humidity'] - self.humidity
                range2 = self.temperature - config_dict['max-temperature']
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees higher than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            else:
                range = config_dict['min-humidity'] - self.humidity
                comment = 'The humidity is ' + str(round(range, 2))
                comment = comment + '% lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

        elif self.humidity > config_dict['max-humidity']:
            if self.temperature < config_dict['min-temperature']:
                range1 = self.humidity - config_dict['max-humidity']
                range2 = config_dict['min-temperature'] - self.temperature
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees lower than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            elif self.temperature > config_dict['max-temperature']:
                range1 = self.humidity - config_dict['max-humidity']
                range2 = self.temperature - config_dict['max-temperature']
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees higher than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            else:
                range = self.humidity - config_dict['max-humidity']
                comment = 'The humidity is ' + str(round(range, 2))
                comment = comment + '% higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

        elif self.temperature < config_dict['min-temperature']:
            if self.humidity < config_dict['min-humidity']:
                range1 = config_dict['min-humidity'] - self.humidity
                range2 = config_dict['min-temperature'] - self.temperature
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees lower than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            elif self.humidity > config_dict['max-humidity']:
                range1 = self.humidity - config_dict['max-humidity']
                range2 = config_dict['min-temperature'] - self.temperature
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees lower than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            else:
                range = config_dict['min-temperature'] - self.temperature
                comment = 'The temperature is ' + str(round(range, 2))
                comment = comment + ' degrees lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

        elif self.temperature > config_dict['max-temperature']:
            if self.humidity < config_dict['min-humidity']:
                range1 = config_dict['min-humidity'] - self.humidity
                range2 = self.temperature - config_dict['max-temperature']
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees higher than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% lower than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            elif self.humidity > config_dict['max-humidity']:
                range1 = self.humidity - config_dict['max-humidity']
                range2 = self.temperature - config_dict['max-temperature']
                comment = 'The temperature is ' + str(round(range2, 2))
                comment = comment + ' degrees higher than the limit '
                comment = comment + 'and the humidity is '
                comment = comment + str(round(range1, 2))
                comment = comment + '% higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

            else:
                range = self.temperature - config_dict['max-temperature']
                comment = 'The temperature is ' + str(round(range, 2))
                comment = comment + ' degrees higher than the limit'
                if(len(rows) == 0):
                    p.pushNote(devices[0]["iden"], '', comment)
                self.notified = 1

        return self.notified
