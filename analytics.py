# The file contains code to produce visualizations based on readings data

# Imported the necessary modules
from sshPlot import sshPlot
import seaborn as sns
from database import database
import pandas as pd
import pygal
import cairosvg
from matplotlib.lines import Line2D

# Defined analytics class


class analytics:

    # Function to create bar chart
    def create_bar_chart(self):

        # Connected to the database
        db = database()
        conn = db.create_conn()

        # Retrieved min, max temp, humidity and data and stored in data frame
        data = pd.read_sql_query('''SELECT DATE, MIN(TEMP), MAX(TEMP), MIN(HUMIDITY),
        MAX(HUMIDITY) FROM READINGS GROUP BY DATE''', conn)

        # Created bar chart comparing min, max temp, humidity for each day
        s_bar = pygal.StackedBar()
        s_bar.title = 'Min, max temperature and humidity comparison per day'
        s_bar.x_labels = map(str, data['DATE'])
        s_bar.add('Min-Temperature', data['MIN(TEMP)'])
        s_bar.add('Max-Temperature', data['MAX(TEMP)'])
        s_bar.add('Min-Humidity', data['MIN(HUMIDITY)'])
        s_bar.add('Max-Humidity', data['MAX(HUMIDITY)'])
        s_bar.render_to_png('test.png')

# Created object to create visualizations
viz = analytics()
viz.create_bar_chart()
