# The file contains code to insert the values read into the database

# Imported the necessary modules
import os
import sqlite3
from monitor import monitor
import notifyPushbullet

# Defined database class


class database:

    # Function to create connection to database
    def create_conn(self):
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        conn = sqlite3.connect(rel_path + 'PIoT_db.db')
        return(conn)

    # Function to create readings table if it does not exist
    def create_table(self):
        conn = self.create_conn()
        conn.execute('''CREATE TABLE IF NOT EXISTS READINGS
        ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
          TEMP REAL NOT NULL,
          HUMIDITY REAL NOT NULL,
          DATE DATETIME NOT NULL,
          TIME DATETIME NOT NULL,
          NOTIFIED INT NOT NULL
          );''')

    # Function to insert data reading data into table
    def insert_table(self):
        conn = self.create_conn()
        mon = monitor()
        npb = notifyPushbullet.notifyPushbullet()
        notified = npb.notify()
        temp = round(npb.temperature, 2)
        humid = round(npb.humidity, 2)
        date = mon.getDate()
        time = mon.getTime()

        conn.execute("INSERT INTO READINGS(TEMP, HUMIDITY, DATE, TIME, NOTIFIED) \
        VALUES(?, ?, ?, ?, ?);", (temp, humid, date, time, notified))

        if((temp > 0 and temp < 100) and (humid > 0 and humid < 100)):
            conn.commit()

        conn.close()
