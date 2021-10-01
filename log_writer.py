# Author: Brandt Davis
# This class will serve to write logs in order to better trace program 
# execution, as well as the activities performed, potentially even a 
# saved state functionality

from datetime import datetime

class Log_writer():
    # ATTRIBUTES
    # ==========

    # Constants
    GENERAL_LOG_PATH = "./log/log.txt"
    CONTROL_LOG_PATH = "./log/control_log"
    CURRENT_DATE_AND_TIME = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self):
        pass

    # Takes a list of files as parameter
    def record_files_downloaded(self, files):
        header = "======== FILES DOWNLOADED =======\n======== " + self.CURRENT_DATE_AND_TIME + " ======\n"
        
        with open(self.GENERAL_LOG_PATH, "a") as log:
            log.write(header)

            for f in files:
                log.write("\t" + f['href'] + "\n")
    
            log.close()

    def update_control_log(self):
        with open(self.CONTROL_LOG_PATH, "a") as ctl_log:
            ctl_log.write("Data extraction: " + self.CURRENT_DATE_AND_TIME)
        
        ctl_log.close()

    def log_data_extraction(self, files):
        self.record_files_downloaded(files)
        self.update_control_log();
    
    def record_website_scraped(self):
        pass