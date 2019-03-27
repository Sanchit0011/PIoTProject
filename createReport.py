# File which creates csv file containing reading status for each day

# Imported the necessary modules
import pandas as pd
import json
import sqlite3
import os
from database import database
from monitor import monitor

# Defined createReport class


class createReport:

    # Function to create csv file containing reading status for each day
    def create_csv(self):

        # Created database object and connected to database
        db = database()
        conn = db.create_conn()

        # Defined relative path
        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        # Loaded config.json file
        with open(rel_path + 'config.json', 'r') as f:
            config = json.load(f)

        # Got min, max temp, humidity from database and stored in dataframe
        data = pd.read_sql_query('''SELECT DATE, MIN(TEMP), MAX(TEMP), MIN(HUMIDITY),
        MAX(HUMIDITY) FROM READINGS GROUP BY DATE''', conn)

        csv_content = []

        # Looped through dataframe and checked if readings are out of range
        # Created csv file based on readings status
        for i in range(0, len(data)):
            comment = "OK"
            if data["MIN(TEMP)"][i] < config['min-temperature']:
                diff = config['min-temperature'] - data["MIN(TEMP)"][i]
                if len(comment) == 0:
                    comment = str(round(diff, 2))
                    comment = comment + " *C below minimum temperature"
                else:
                    comment = comment + "; " + str(round(diff, 2))
                    comment = comment + " *C below minimum temperature"

            if data["MAX(TEMP)"][i] > config['max-temperature']:
                diff = data["MAX(TEMP)"][i] - config['max-temperature']
                if len(comment) == 0:
                    comment = str(round(diff, 2))
                    comment = comment + " *C above maximum temperature"
                else:
                    comment = comment + "; " + str(round(diff, 2))
                    comment = comment + " *C above maximum temperature"

            if data["MIN(HUMIDITY)"][i] < config['min-humidity']:
                diff = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                if len(comment) == 0:
                    comment = str(round(diff, 2))
                    comment = comment + "% below minimum humidity"
                else:
                    comment = comment + "; " + str(round(diff, 2))
                    comment = comment + "% below minimum humidity"

            if data["MAX(HUMIDITY)"][i] > config['max-humidity']:
                diff = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                if len(comment) == 0:
                    comment = str(round(diff, 2))
                    comment = comment + "% above maximum humidity"

                else:
                    comment = comment + "; " + str(round(diff, 2))
                    comment = comment + "% above maximum humidity"

            csv_content.append([data["DATE"][i], comment])
            df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
            df.to_csv("report.csv", index=False)

# Created object to call create_csv
cr = createReport()
cr.create_csv()
