# The file contains code to call insert_table function

# Imported the necessary module
from database import database

# Defined monitorAndNotify class


class monitorAndNotify:

    # Function to call insert_table in database class
    def init_insert(self):
        db = database()
        # db.create_table()
        db.insert_table()

# Created object to call init_insert
mon = monitorAndNotify()
mon.init_insert()
