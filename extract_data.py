# Author: Brandt Davis
# This class handles all the relevant data extractions for Alberta covid stats
#
# Currently it uses a locally stored csv file, however, in the future I plan to implement
# a web-scraping solution to automate the collection of up-to-date data

# Imports 
import pandas as pd
import requests
import mechanize
from bs4 import BeautifulSoup as soup

class Extract_data:
    # Attributes

    # Methods
    def __init__(self):
        pass

    def get_alberta_covid_stats_dataframe(self):
        #page = requests.get("https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export")
        #return page
        return pd.read_csv("Data/covid-19-alberta-statistics-data.csv")

'''
e = Extract_data()
page = e.get_alberta_covid_stats_dataframe()

page = soup(page.content, 'html.parser')
file = page.find('a', class_='goa-cta')


print()

link ="https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export" 
page = requests.get(link+file['href']) 

print(page.content)
'''