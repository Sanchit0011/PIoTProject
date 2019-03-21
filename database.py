import sqlite3
from monitor import monitor


class database:

    def create_conn(self):
        conn = sqlite3.connect('PIoT_db.db')
        return(conn)

    def create_table(self):
        conn = self.create_conn()
        conn.execute('''CREATE TABLE READINGS
        ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
          TEMP REAL NOT NULL,
          HUMIDITY REAL NOT NULL,
          DATE DATETIME NOT NULL,
          TIME DATETIME NOT NULL
        );''')

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
