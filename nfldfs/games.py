#!/usr/bin/env python

import itertools
from io import StringIO
from urllib.parse import urlparse
import time

from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

from nfldfs import utils as utils


# Function to create game search parameters
def find_games(dfs_site, season_from, week_from, season_to=None, week_to=None):
    """
    Returns a list of URLs.

    Use this function to generate a list of URLs that can be used to fetch
    NFL daily fantasy results for DraftKings, FanDuel, and Yahoo! Fantasy.

    Parameters
    ----------
    dfs_site : list of str
        Abbreviation for each daily fantasy site to find data for.
        Acceptable values: 'dk': DraftKings, 'fd': FanDuel, 'yh': Yahoo!
    season_from: int
        The season number to begin search range.
    week_from: int
        The week of the season to begin search range
    season_to : int, default None
        The season number to search for data up to, inclusive.
    week_to : int, default None
        The week number to search for data up to, inclusive.

    Returns
    -------
    A list of formatted URL strings

    Example
    -------
    URLs for week 1 of the 2014 season for DraftKings and FanDuel.
    >>> find_games(dfs_site=['dk', 'fd'], season_from=2014, week_from=1)
    ['http://rotoguru1.com/cgi-bin/fyday.pl?week=1&year=2014&game=dk&scsv=1',
    'http://rotoguru1.com/cgi-bin/fyday.pl?week=1&year=2014&game=fd&scsv=1']
    """

    season_to_range = season_to or season_from

    week_to_range = week_to or week_from

    utils.game_parameters_validator(dfs_site, season_from, season_to=season_to_range, week_from=week_from,
                                    week_to=week_to_range)

    seasons = [*range(season_from, season_to_range + 1)]
    weeks = [*range(week_from, week_to_range + 1)]


    base_url = "http://rotoguru1.com/cgi-bin/fyday.pl?week={}&year={}&game=" + f"{dfs_site}&scsv=1"
    game_urls = [base_url.format(w, s) for w, s in itertools.product(
        weeks, seasons)]

    # Only unique URls
    game_urls = set(game_urls)

    return game_urls


# Function to take game_urls and return data
def get_game_data(game_urls=[]):
    """
    Returns a pandas DataFrame

    Use this function to scrape NFL daily fantasy results data from
    www.rotoguru1.com by passing a list of URLs.

    Parameters
    ----------
    game_urls : list of strings
        List of URL strings with each element being a specific URL

    Returns
    -------
    pd.DataFrame
        Data values include:
        =============   =======================================================
        gid             Unique id for each player (as `int`)
        week            The week number (as `int`)
        year            The season number (as `int`)
        player_name     Full player name, [Last Name, First Name] (as `str`)
        position        Player position, e.g. QB, TE, and Def (as `str`)
        team_name       Team the player is member of, abbreviation (as `str`)
        home_or_away    Identifies if a player was home or away (as `str`)
        opponent_name   Opponent name, abbreviation (as `str`)
        points          Total daily fantasy points scored (as `float`)
        salary          Daily fantasy salary, site specific (as `float`)
        dfs_site        Value indicating which dfs site the data relates to
        ==============  =======================================================
    """
    all_data = pd.DataFrame()

    for g in game_urls:
        # Parse the game from the query string to use as column value
        # game = urlparse(g).query[22:24]
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
        data['dfs_site'] = g
        all_data = pd.concat(objs=[all_data, data])

        time.sleep(0.25)

    return all_data
