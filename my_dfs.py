#!/usr/bin/env python3

from nfldfs import games as games
import click

@click.command()
@click.option('--dfs_site', prompt='Enter list of dfs site(s)')
@click.option('--season_from', prompt='Season to begin search')
@click.option('--week_from', prompt='Week to begin search')
@click.option('--nrows', prompt='Enter number of rows to return')

def get_dfs_data(dfs_site, season_from, week_from, nrows):
    """
    """
    dfs_site = [dfs_site]
    season_from, week_from = int(season_from), int(week_from)
    nrows = int(nrows)
    g = games.find_games(dfs_site, season_from, week_from)
    data = games.get_game_data(g)

    print(data.head(nrows))

if __name__ == '__main__':
    get_dfs_data()
