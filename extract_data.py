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
    def save_file(self, file, data_content):
        filename = "./Data/" + file['href'].split("/data/stats/")[1] 
        open(filename, 'wb').write(data_content.content)

    # Create/overwrite files in the Data folder, which correspond to the scraped html
    # Refactor: merge with 'save_file(...)'
    def save_html_file(self, filename, html_content):
        open(filename, 'w').write(html_content)

    # Iterate over all the 'Download' buttons on AB COVID-19 stats page
    def retrieve_ab_csv_files(self):
        page = self.get_page_from_internet(self.AB_STATS_URL)
        files = page.findAll('a', class_='goa-cta')

        for f in files:
            data_url = requests.compat.urljoin(self.AB_STATS_URL, f['href'])
            data_content = requests.get(data_url)
            self.save_file(f, data_content)
        
        return files 
    
    # In Progress: This method currently finds a single table from html copied from the AB govt's webpage.
    def scrape_ab_tables(self):
        # KEEP
        # This code need not be run every time, only when the data changes, this will become automated
        #page = soup(requests.get(self.AB_VACC_URL).content, 'html.parser')
        #body = page.find_all('div', {"id" : "vaccine-outcomes"})[0]
        #self.save_html_file('./Data/html/tables.html', str(body.prettify()))

        p4 = ""
        body = self.get_page_from_local_storage('./Data/html/tables.html').find_all('div', {"id" : "vaccine-outcomes"})[0]
        body.find('ul').decompose()

        table_titles = body.find_all('p')

        for t in table_titles:
            if 'Table 4' in t.text:
                p4 = t

        table_4 = p4.findNext('table')
        #df = pd.read_html(str(table_4.parent))
        #df.head()


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