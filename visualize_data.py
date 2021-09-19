# Author: Brandt Davis
# This class is used to perform the various visualizations of covid-related data 
#
# Currently it will handle Alberta's stats, but in the future I plan to expand this to other provinces as well 

# Imports 
import matplotlib.pyplot as plt

class Visualize_data:
    # Attributes

    # Methods
    def __init__(self):
        pass

    #
    def create_bar_graph_of_data(self, data):
        plt.figure(figsize=(12,10))
        data.sort_values().plot.bar()
        plt.savefig("Visuals/chart.png")