# File which contains the main method

# Imported the necessary module
from database import database

# Defined monitorAndNotify class


class monitorAndNotify:

    # Function to call insert_table in database file
    def init_insert(self):
        db = database()

        # Only if table does not exist
        db.create_table()

        db.insert_table()

# Created object to call init_insert
mon = monitorAndNotify()
mon.init_insert()
