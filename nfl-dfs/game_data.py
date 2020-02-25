from datetime import date
import itertools
from bs4 import BeautifulSoup
import requests
import io
import pandas as pd




# Function to get historical NFL daily fantasy results

def get_historical_results(season_start, season_end=None):
    """Scrapes historical data for NFL daily fantasy

    Parameters:
    season_start (int): The season_start argume
    season_end (int): The season_end ar

    Returns:
    int:Returning value

   """

    # If season_end is not entered, return the last full completed season
    season_end_range = season_end

    if not season_end_range:
        season_end_range = int(date.today().year - 1)

    seasons = [s for s in range(season_start, season_end_range + 1)]
    weeks = [w for w in range(1, 2 + 1)]

    # Initialize empty DataFrame to store the results
    all_data = pd.DataFrame()

    # Send the request and store the response
    for s, w in itertools.product(seasons, weeks):
        url = f"http://rotoguru1.com/cgi-bin/fyday.pl?week={w}&year={s}&game=dk&scsv=1"
        r = requests.get(url).text

        # Parse the data and append to all_data
        soup = BeautifulSoup(r, "lxml")
        data_string = io.StringIO(soup.find("pre").text)
        data = pd.read_csv(data_string, sep=';')

        all_data = pd.concat(objs=[all_data, data])

    return(all_data)
           
