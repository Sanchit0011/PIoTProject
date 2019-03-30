# File to get matplotlib.pyplot module

# Imported the necessary modules
import matplotlib
matplotlib.use('Agg')

# Defined sshPlot class


class sshPlot:

    # Function to get matplotlib.pyplot module
    def getPlot():
        plt = matplotlib.pyplot
        return plt
