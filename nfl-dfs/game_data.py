from datetime import date
import itertools
from bs4 import BeautifulSoup
import requests
import io
import pandas as pd

def seasons_to_search(season_from, week_from, season_to=None, week_to=None):
    # If season_to not entered, only search for one season
    season_to_range = season_to
    week_to_range = week_to

    if not season_to_range:
            season_to_range = season_from

    if not week_to_range:
        week_to_range = week_from

    seasons = [s for s in range(season_from, season_to_range + 1)]
    weeks = [w for w in range(week_from, week_to_range + 1)]

    base_url = "http://rotoguru1.com/cgi-bin/fyday.pl?week={}&year={}&game=dk&scsv=1"
    game_urls = [base_url.format(s, w) for s, w in itertools.product(seasons, weeks)]

    return game_urls
