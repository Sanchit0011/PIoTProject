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
        db = database()
        conn = db.create_conn()

        path1 = os.path.realpath(__file__)
        path2 = os.path.basename(__file__)
        rel_path = path1.replace(path2, "")

        with open(rel_path + 'config.json', 'r') as f:
            config = json.load(f)

        data = pd.read_sql_query('''SELECT DATE, MIN(TEMP), MAX(TEMP), MIN(HUMIDITY),
        MAX(HUMIDITY) FROM READINGS GROUP BY DATE''', conn)
        csv_content = []
        comment = ""

        for i in range(0, len(data)):
            if data["MIN(HUMIDITY)"][i] < config['min-humidity']:
                if data["MIN(TEMP)"][i] < config['min-temperature']:
                    diff1 = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                    diff2 = config['min-temperature'] - data["MIN(TEMP)"][i]
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C below minimum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% below minimum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

                elif data["MAX(TEMP)"][i] > config['max-temperature']:
                    diff1 = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                    diff2 = data["MAX(TEMP)"][i] - config['max-temperature']
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C above maximum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% below minimum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

            elif data["MAX(HUMIDITY)"][i] > config['max-humidity']:
                if data["MIN(TEMP)"][i] < config['min-temperature']:
                    diff1 = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                    diff2 = config['min-temperature'] - data["MIN(TEMP)"][i]
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C below minimum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% above maximum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

                elif data["MAX(TEMP)"][i] > config['max-temperature']:
                    diff1 = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                    diff2 = data["MAX(TEMP)"][i] - config['max-temperature']
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C above maximum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% above maximum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

            elif data["MIN(TEMP)"][i] < config['min-temperature']:
                if data["MIN(HUMIDITY)"][i] < config['min-humidity']:
                    diff1 = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                    diff2 = config['min-temperature'] - data["MIN(TEMP)"][i]
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C below minimum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% below minimum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

                elif data["MAX(HUMIDITY)"][i] > config['max-humidity']:
                    diff1 = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                    diff2 = config['min-temperature'] - data["MIN(TEMP)"][i]
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C below minimum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% above maximum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

            elif data["MAX(TEMP)"][i] > config['max-temperature']:
                if data["MIN(HUMIDITY)"][i] < config['min-humidity']:
                    diff1 = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                    diff2 = data["MAX(TEMP)"][i] - config['max-temperature']
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C above maximum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% below minimum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

                elif data["MAX(TEMP)"][i] > config['max-temperature']:
                    diff1 = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                    diff2 = data["MAX(TEMP)"][i] - config['max-temperature']
                    comment = "BAD: " + str(round(diff2, 2))
                    comment = comment + " *C above maximum temperature; "
                    comment = comment + str(round(diff1, 2))
                    comment = comment + "% above maximum humidity"
                    csv_content.append([data["DATE"][i], comment])
                    df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                    df.to_csv("report.csv", index=False)

            elif data["MAX(HUMIDITY)"][i] > config['max-humidity']:
                diff = data["MAX(HUMIDITY)"][i] - config['max-humidity']
                comment = "BAD: " + str(round(diff, 2))
                comment = comment + "% above maximum humidity"
                csv_content.append([data["DATE"][i], comment])
                df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                df.to_csv("report.csv", index=False)

            elif data["MIN(HUMIDITY)"][i] < config['min-humidity']:
                diff = config['min-humidity'] - data["MIN(HUMIDITY)"][i]
                comment = "BAD: " + str(round(diff, 2))
                comment = comment + "% below minimum humidity"
                csv_content.append([data["DATE"][i], comment])
                df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                df.to_csv("report.csv", index=False)

            elif data["MIN(TEMP)"][i] < config['min-temperature']:
                diff = config['min-temperature'] - data["MIN(TEMP)"][i]
                comment = "BAD: " + str(round(diff, 2))
                comment = comment + " *C below minimum temperature"
                csv_content.append([data["DATE"][i], comment])
                df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                df.to_csv("report.csv", index=False)

            elif data["MAX(TEMP)"][i] > config['max-temperature']:
                diff = data["MAX(TEMP)"][i] - config['max-temperature']
                comment = "BAD: " + str(round(diff, 2))
                comment = comment + " *C above maximum temperature"
                csv_content.append([data["DATE"][i], comment])
                df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                df.to_csv("report.csv", index=False)

            else:
                csv_content.append([data["DATE"][i], "OK"])
                df = pd.DataFrame(csv_content, columns=['DATE', 'STATUS'])
                df.to_csv("report.csv", index=False)

# Created object to call create_csv
cr = createReport()
cr.create_csv()
