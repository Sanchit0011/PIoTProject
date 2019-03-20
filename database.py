# The file contains code to insert the values read to the database

# Imported the necessary files
import sqlite3
from monitor import monitor

# Defined database class


class database:

    # Function to insert reading data into table
    def insert_table(self):
        conn = self.create_conn()
        mon = monitor()
        temp = round(mon.calc_acc_temp(), 2)
        humid = round(mon.getHumidity(), 2)
        date = mon.getDate()
        time = mon.getTime()
        conn.execute("INSERT INTO READINGS(TEMP, HUMIDITY, DATE, TIME) \
        VALUES(?, ?, ?, ?);", (temp, humid, date, time))

        if((temp > 0 and temp < 100) and (humid > 0 and humid < 100)):
            conn.commit()
            print("Records created successfully")

        conn.close()
