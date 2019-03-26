from monitor import monitor
from pushbullet.pushbullet import PushBullet
import database
import json
import os


class notifyPushbullet:

    monitorobj = monitor()
    temperature = monitorobj.calc_acc_temp()
    humidity = monitorobj.getHumidity()

    def notify(self):
        self.notified = 0
        date = self.monitorobj.getDate()
        db = database.database()

        apiKey = "o.yVczv6qpQuZIKF8zaPImpIxIxw0evUIp"
        p = PushBullet(apiKey)

        # Getting a list of devices
        devices = p.getDevices()
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        with open(rel_path + 'config.json', 'r') as f:
            config_dict = json.load(f)

        conn = db.create_conn()

        cur = conn.cursor()
        cur.execute("SELECT * FROM READINGS WHERE NOTIFIED = 1 AND DATE = ? LIMIT 1;", [str(date)])

        rows = cur.fetchall()

        if self.humidity < config_dict['min-humidity'] and self.temperature < config_dict['min-temperature']:
            range1 = config_dict['min-humidity'] - self.humidity
            range2 = config_dict['min-temperature'] - self.temperature
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range2, 2)) + ' degrees lower than the limit and the humidity is ' + str(round(range1, 2)) + '% lower than the limit')
            self.notified = 1

        elif self.humidity < config_dict['min-humidity'] and self.temperature > config_dict['max-temperature']:
            range1 = config_dict['min-humidity'] - self.humidity
            range2 = self.temperature - config_dict['max-temperature']
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range2, 2)) + ' degrees higher than the limit and the humidity is ' + str(round(range1, 2)) + '% lower than the limit')
            self.notified = 1

        elif self.humidity > config_dict['max-humidity'] and self.temperature < config_dict['min-temperature']:
            range1 = self.humidity - config_dict['max-humidity']
            range2 = config_dict['min-temperature'] - self.temperature
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range2, 2)) + ' degrees lower than the limit and the humidity is ' + str(round(range1, 2)) + '% higher than the limit')
            self.notified = 1

        elif self.humidity > config_dict['max-humidity'] and self.temperature > config_dict['max-temperature']:
            range1 = self.humidity - config_dict['max-humidity']
            range2 = self.temperature - config_dict['max-temperature']
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range2, 2)) + ' degrees higher than the limit and the humidity is ' + str(round(range1, 2)) + '% higher than the limit')
            self.notified = 1

        elif self.temperature > config_dict['max-temperature']:
            range = self.temperature - config_dict['max-temperature']
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range, 2)) + ' degrees higher than the limit')
            self.notified = 1

        elif self.temperature < config_dict['min-temperature']:
            range = config_dict['min-temperature'] - self.temperature
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The temperature is ' + str(round(range, 2)) + ' degrees lower than the limit')
            self.notified = 1

        elif self.humidity > config_dict['max-humidity']:
            range = self.humidity - config_dict['max-humidity']
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The humidity is ' + str(round(range, 2)) + '% higher than the limit')
            self.notified = 1

        elif self.humidity < config_dict['min-humidity']:
            range = config_dict['min-humidity'] - self.humidity
            if(len(rows) == 0):
                p.pushNote(devices[0]["iden"], '', 'The humidity is ' + str(round(range, 2)) + '% lower than the limit')
            self.notified = 1

        return self.notified
