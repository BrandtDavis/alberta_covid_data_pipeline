# Author: Brandt Davis
# This class handles all the relevant data extractions for Alberta covid stats
#
# Currently it uses a locally stored csv file, however, in the future I plan to implement
# a web-scraping solution to automate the collection of up-to-date data

# Imports 
import pandas as pd
from datetime import datetime
from datetime import date
import requests
from bs4 import BeautifulSoup as soup

class Extract_data:
    # Attributes
    #
    # Constants
    # 
    # Web address constants
    AB_STATS_URL =  "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export"
    AB_VACC_URL = "https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#vaccine-outcomes"

    # File path constants are relative to the AB government website url
    STATS_FILE_PATH = "/data/stats/covid-19-alberta-statistics-data.csv"
    SUMMARY_FILE_PATH = "/data/stats/covid-19-alberta-statistics-summary-data.csv"
    MAP_FILE_PATH = "/data/stats/covid-19-alberta-statistics-map-data.csv"
    COVERAGE_FILE_PATH = "/data/stats/lga-coverage.csv"

    # HTML classes of various tables
    AB_VACC_TABLES = "goa-table-wrapper"

    # Methods
    def __init__(self):
        pass

    # ---------------- In Progress -----------------------
    def is_outdated(self):
        ''' Will check if the current local data is outdated '''

        current_time = datetime.date.today()
        last_extraction = self.get_last_extraction()

        if current_time - last_extraction > self.ONE_DAY:
             return True
            
        return False

    # Create/overwrite files in the Data folder, which correspond to the downloaded .csv files
    def save_file(self, filepath, file_mode, file_content):
        open(filepath, file_mode).write(file_content)

    # Iterate over all the 'Download' buttons on AB COVID-19 stats page
    def retrieve_ab_csv_files(self):
        page = self.get_page_from_internet(self.AB_STATS_URL)
        files = page.findAll('a', class_='goa-cta')

        for f in files:
            data_url = requests.compat.urljoin(self.AB_STATS_URL, f['href'])
            data_content = requests.get(data_url)
            filepath = "./Data/csv_files/" + f['href'].split("/data/stats/")[1]
            self.save_file(filepath, 'wb', data_content.content)
        
        return files 
    
    # In Progress: This method currently finds a single table from html copied from the AB govt's webpage.
    def scrape_ab_tables(self):
        # KEEP
        # This code need not be run every time, only when the data changes, this will become automated
        #page = soup(requests.get(self.AB_VACC_URL).content, 'html.parser')
        #body = page.find_all('div', {"id" : "vaccine-outcomes"})[0]
        #self.save_file('./Data/html/tables.html', str(body.prettify()))

        p4 = ""
        body = self.get_page_from_local_storage('./Data/html/tables.html').find_all('div', {"id" : "vaccine-outcomes"})[0]
        body.find('ul').decompose()

        table_titles = body.find_all('p')

        for t in table_titles:
            if 'Table 4' in t.text:
                p4 = t

        table_4 = p4.findNext('table')
        self.save_file('./Data/html/table_4.html', 'w', str(table_4))
        #df = pd.read_html(str(table_4))
        #df[0].info()
        # print(str(df[0]))


    # GET METHODS
    def get_page_from_internet(self, url):
        ''' Return the contents of a particular web page '''
        return soup(requests.get(url).content, 'html.parser')

    def get_page_from_local_storage(self, filepath):
        ''' Return the contents of a web page stored at "./Data/html/" '''
        return soup(open(filepath).read(), 'html.parser')

    def get_alberta_covid_stats_dataframe(self):
        return pd.read_csv("Data/covid-19-alberta-statistics-data.csv")





# --------------------
#---------------------

def get_alberta_vacc_stats_dataframe(self):
    return pd.read_csv("Data/Vaccine/covid-19-alberta-vaccine-data.csv")
e = Extract_data()

e.scrape_ab_tables()