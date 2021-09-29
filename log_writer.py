# Author: Brandt Davis
# This class will serve to write logs in order to better trace program 
# execution, as well as the activities performed, potentially even a 
# saved state functionality

from datetime import datetime

class Log_writer():
    
    def __init__(self):
        pass

    # Takes a list of files as parameter
    def record_files_downloaded(self, files):
        current_date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        header = "======== FILES DOWNLOADED =======\n======= " + current_date_and_time + " =======\n"
        
        with open("./log/logfile.txt", "a") as logfile:
            logfile.write(header)

            for f in files:
                logfile.write("\t" + f['href'] + "\n")
            
            logfile.close()
                
    
    def record_website_scraped(self):
        pass