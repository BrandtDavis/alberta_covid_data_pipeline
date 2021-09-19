# Author: Brandt Davis
# This class handles all the relevant data extractions for Alberta covid stats
#
# Currently it uses a locally stored csv file, however, in the future I plan to implement
# a web-scraping solution to automate the collection of up-to-date data

# Imports 
import pandas as pd

class Extract_data:
    # Attributes

    # Methods
    def __init__(self):
        pass

    def get_alberta_covid_stats_dataframe(self):
        return pd.read_csv("Data/covid-19-alberta-statistics-data.csv")
