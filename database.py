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
