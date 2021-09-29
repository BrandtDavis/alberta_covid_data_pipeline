# Author: Brandt Davis
# This file controls the program flow and functionality

import extract_data 
import transform_data
import load_data 
import visualize_data


# Initialize objects
extract = extract_data.Extract_data()
transform = transform_data.Transform_data()
load = load_data.Load_data()
visualize = visualize_data.Visualize_data()

# Pipeline operations 
extract.retrieve_ab_csv_files()
ab_covid_data = extract.get_alberta_covid_stats_dataframe()
ab_covid_deaths = transform.get_deaths_by_age(ab_covid_data)
visualize.create_bar_graph_of_data(ab_covid_deaths)

