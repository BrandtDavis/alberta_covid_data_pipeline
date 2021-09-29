# Author: Brandt Davis
# This file controls the program flow and functionality

from log_writer import Log_writer
import extract_data 
import transform_data
import load_data 
import log_writer
import visualize_data


# Initialize objects
extract = extract_data.Extract_data()
transform = transform_data.Transform_data()
load = load_data.Load_data()

logger = log_writer.Log_writer()
visualize = visualize_data.Visualize_data()

# Pipeline operations 
file_list = extract.retrieve_ab_csv_files()
logger.record_files_downloaded(file_list)

ab_covid_data = extract.get_alberta_covid_stats_dataframe()
ab_covid_deaths = transform.get_deaths_by_age(ab_covid_data)
visualize.create_bar_graph_of_data(ab_covid_deaths)

