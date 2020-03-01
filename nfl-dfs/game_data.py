import itertools
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from urllib.parse import urlparse

# Function to create game search parameters
def games_to_search(dfs_site, season_from, week_from, season_to=None, week_to=None):

    season_to_range = season_to
    week_to_range = week_to

    if not season_to_range:
            season_to_range = season_from

    if not week_to_range:
        week_to_range = week_from

    games = dfs_site
    seasons = [*range(season_from, season_to_range + 1)]
    weeks = [*range(week_from, week_to_range + 1)]

    base_url = "http://rotoguru1.com/cgi-bin/fyday.pl?week={}&year={}&game={}&scsv=1"
    game_urls = [base_url.format(w, s, g) for w, s, g in itertools.product(weeks, seasons, games)]

    return game_urls


# Function to take game_urls and return data
def get_game_data(game_urls=[]):

    # Initialize empty DataFrame to store the results
    all_data = pd.DataFrame()

    for g in game_urls:
        # Parse the game from the query string to use as column value
        game = urlparse(g).query[22:24] 
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
        data['dfs_site'] = game
        all_data = pd.concat(objs=[all_data, data])

    return(all_data)
