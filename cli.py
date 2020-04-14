#!/usr/bin/env python3
import click
from datetime import date

from nfldfs import games as games


# Options for command line interface
@click.command()
@click.argument('dfs_site',
                required=True)
@click.option('--season_from',
              type=int,
              prompt='Season beginning',
              help='The season number in the beginning search range')
@click.option('--season_to',
              type=int,
              prompt='Season ending',
              help='The season number at the end of the search range (inclusive)')
@click.option('--week_from',
              type=int,
              prompt='Week beginning',
              help='The week number in the beginning search range')
@click.option('--week_to',
              type=int,
              prompt='Week ending',
              help='The week number at the end of the search range (inclusive)')
def get_dfs_data(dfs_site, season_from, season_to, week_from, week_to):
    """
    Simple program to scrape NFL daily fantasy points and salary information.
    Designed to be used as a bulk download tool. Results are returned in comma
    delimited format (csv) to the /data directory. Refer there to look at the
    'draftkings_sample_output.csv'.

    DFS_SITE The name of the dfs site to return data for. Refer to the package
    docs for more usage examples.

    """
    g = games.find_games(dfs_site=dfs_site,
                            season_from=season_from,
                            week_from=week_from,
                            season_to=season_to,
                            week_to=week_to)

    data = games.get_game_data(game_urls=g)
    run_date = date.today().strftime('%Y%m%d')

    return data.to_csv(f'data/{dfs_site}_{run_date}.csv')


if __name__ == "__main__":
    print('Welcome to NFL DFS!\n')
    get_dfs_data()
