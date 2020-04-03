#!/usr/bin/env python3
import click
import pandas as pd
from nfldfs import games as games


# Options for command line interface
@click.command()
@click.option('--dfs_site', prompt='Which dfs site(s)?')
@click.option('--season_from', type=int, prompt='For which season?')
@click.option('--week_from', type=int, prompt='Week to begin search')
@click.option('--nrows', type=int, prompt='Enter number of rows to return')

def get_dfs_data(dfs_site, season_from, week_from, nrows):
    dfs_site = [dfs_site]
    g = games.find_games(dfs_site, season_from, week_from)
    data = games.get_game_data(g)

    print("Success!")
    print(f"Succesfully scraped {data.shape[0]} rows")

if __name__ == "__main__":
    get_dfs_data()
