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

    # Function to create scatter plot
    def create_scatter_plot(self):

        # Getting the matlibplot.pyplot module
        plt = sshPlot.getPlot()

        # Connected to the database
        db = database()
        conn = db.create_conn()

        # Retrieved reading data and stored in data frame
        data = pd.read_sql_query('''SELECT * FROM READINGS''', conn)

        # Created four new data frames based on time range
        time = data['TIME']
        range1 = (time >= "10") & (time < "12")
        df1 = data[range1]
        df1 = df1.assign(time_range="10-12")
        range2 = (time >= "12") & (time < "14")
        df2 = data[range2]
        df2 = df2.assign(time_range="12-14")
        range3 = (time >= "14") & (time < "16")
        df3 = data[range3]
        df3 = df3.assign(time_range="14-16")
        range4 = (time >= "16") & (time < "18")
        df4 = data[range4]
        df4 = df4.assign(time_range="16-18")

        # Concatenated all four data frames
        df = pd.concat([df1, df2, df3, df4], ignore_index=True)

        temp = df["TEMP"]
        humidity = df["HUMIDITY"]
        time_range = df["time_range"]

        # Created scatterplot depicting relationship between temp and humidity
        # in a given time range
        sns.scatterplot(x=temp, y=humidity, data=df, hue=time_range)
        plt.title('''Temperature humidity relationship for given time range''')
        custom = [Line2D([], [], marker='.', color='blue', linestyle='None'),
                  Line2D([], [], marker='.', color='orange', linestyle='None'),
                  Line2D([], [], marker='.', color='green', linestyle='None'),
                  Line2D([], [], marker='.', color='red', linestyle='None')]
        plt.legend(custom, ['10-12', '12-14', '14-16', '16-18'], loc='best')

        # Save plot as png file
        plt.savefig('temphumidscatter.png')

# Created object to create visualizations
viz = analytics()
viz.create_scatter_plot()
viz.create_bar_chart()
