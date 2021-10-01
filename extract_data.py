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
    #
    # Constants
    # 
    # Web address constants
    AB_STATS_URL =  "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"

    # File path constants are relative to the AB government website url
    STATS_FILE_PATH = "/data/stats/covid-19-alberta-statistics-data.csv"
    SUMMARY_FILE_PATH = "/data/stats/covid-19-alberta-statistics-summary-data.csv"
    MAP_FILE_PATH = "/data/stats/covid-19-alberta-statistics-map-data.csv"
    COVERAGE_FILE_PATH = "/data/stats/lga-coverage.csv"

    # Methods
    def __init__(self):
        pass

    # Parse the control_log file to see if enough time has passed to re-retrieve the files
    def is_outdated(self):
        pass

    def get_filename(self):
        pass

    # Create/overwrite files in the Data folder, which correspond to the downloaded .csv files
    def save_file(self, file, data_content):
        filename = "./Data/" + file['href'].split("/data/stats/")[1] 
        open(filename, 'wb').write(data_content.content)
               
    # Iterate over all the 'Download' buttons on AB COVID-19 stats page
    def retrieve_ab_csv_files(self):

        #if is_outdated():

        
        page = requests.get(self.AB_STATS_URL)
        page = soup(page.content, 'html.parser')
        files = page.findAll('a', class_='goa-cta')

        for f in files:
            data_url = requests.compat.urljoin(self.AB_STATS_URL, f['href'])
            data_content = requests.get(data_url)
            self.save_file(f, data_content)
        
        return files 
           
    def get_alberta_covid_stats_dataframe(self):
        return pd.read_csv("Data/covid-19-alberta-statistics-data.csv")
