import itertools
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

pd.set_option('display.width', 2000)

def games_to_search(season_from, week_from, season_to=None, week_to=None):
    
    season_to_range = season_to
    week_to_range = week_to

    if not season_to_range:
            season_to_range = season_from

    if not week_to_range:
        week_to_range = week_from

    seasons = [s for s in range(season_from, season_to_range + 1)]
    weeks = [w for w in range(week_from, week_to_range + 1)]

    base_url = "http://rotoguru1.com/cgi-bin/fyday.pl?week={}&year={}&game=dk&scsv=1"
    game_urls = [base_url.format(s, w) for s, w in itertools.product(weeks, seasons)]

    return game_urls


# Function to take game_urls and return data
def get_game_data(game_urls=[]):
    
    # Initialize empty DataFrame to store the results
    all_data = pd.DataFrame()
    
    for g in game_urls:
        response = requests.get(g).text
        soup = BeautifulSoup(response, "lxml")
        data_string = StringIO(soup.find("pre").text)
        data = pd.read_csv(data_string, 
                           sep=';',
                           index_col=2,
                           header=None,
                           skiprows=1,
                           names=['week',
                                  'year',
                                  'gid',
                                  'player_name',
                                  'position',
                                  'team_name',
                                  'home_or_away',
                                  'opponent_name',
                                  'points',
                                  'salary']
                           )        
        all_data = pd.concat(objs=[all_data, data])
        
    return(all_data)