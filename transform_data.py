# Author: Brandt Davis
# This class handles all the relevant data transformations for Alberta covid stats
#


# Imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Transform_data:
    # Attributes

    # Methods
    def __init__(self):
        pass

    # Takes a dataframe object containg general covid stats
    def get_deaths_by_age(self, covid_data):
        covid_deaths = covid_data[covid_data['Case status'] == "Died"]
        return covid_deaths.groupby(['Age group']).size()









