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

    def file_is_outdated(self):
        pass

    # - Iterate over all the 'Download' buttons on AB COVID-19 stats page
    # - Create/overwrite files in the Data folder, which correspond to the 
    #   downloaded .csv files
    #
    def retrieve_ab_csv_files(self):
        url = "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"

        page = requests.get(url)
        page = soup(page.content, 'html.parser')
        files = page.findAll('a', class_='goa-cta')

        for f in files:
            data_url = requests.compat.urljoin(url, f['href'])
            newpage = requests.get(data_url)

            if f['href'] == "/data/stats/covid-19-alberta-statistics-data.csv" :
                open('./Data/covid-19-alberta-statistics-data.csv', 'wb').write(newpage.content)
                continue

            elif f['href'] == "/data/stats/covid-19-alberta-statistics-summary-data.csv" :
                open('./Data/covid-19-alberta-statistics-summary-data.csv', 'wb').write(newpage.content)
                continue
            
            elif f['href'] == "/data/stats/covid-19-alberta-statistics-map-data.csv" :
                open('./Data/covid-19-alberta-statistics-map-data.csv', 'wb').write(newpage.content)
                continue
            
            elif f['href'] == "/data/stats/lga-coverage.csv" :
                open('./Data/lga_coverage.csv', 'wb').write(newpage.content)
                continue
       
    def get_alberta_covid_stats_dataframe(self):
        return pd.read_csv("Data/covid-19-alberta-statistics-data.csv")
