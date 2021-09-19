# Author: Brandt Davis
# This will become a class that handles all the relevant data transformations for Alberta covid stats


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

covid_data = pd.read_csv("covid-19-alberta-statistics-data.csv")

status_died = covid_data[covid_data['Case status'] == "Died"]

#status_died.to_csv("deaths.csv", ",")

x = status_died.groupby(['Age group']).size()
y = status_died['Case status'].shape



print(status_died.head())
#print(status_died.shape)
print(type(x))
print(len(x))


plt.figure(figsize=(12,10))
x.sort_values().plot.bar()

#print()

#fig, ax = plt.subplots(figsize=(10, 8))
#ax.bar(x, y)

#plt.bar(x, y)
plt.savefig("chart.png")



