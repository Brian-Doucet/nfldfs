#!/usr/bin/env python3
import click

from nfldfs import games as games


# Options for command line interface
@click.command()
@click.argument('dfs_site',
                required=True,
                nargs=-1)
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
@click.option('--filename',
              type=str,
              prompt='Enter a filename',
              help='Filename for your results. Omit the .csv file extension')
def get_dfs_data(dfs_site, season_from, season_to, week_from, week_to, filename):
    """
    Simple program to scrape NFL daily fantasy points and salary information.
    Designed to be used as a bulk download tool. Results are returned in comma
    delimited format (csv) to the /data directory. Check there to look at the
    'draftkings_sample_output.csv'.

    DFS_SITE The name of the dfs site(s) to return data for. Multiple sites should
    be separated by a space. Refer to the package docs for more usage examples.

    """
    dfs_site = list(dfs_site)
    g = games.find_games(dfs_site=dfs_site,
                         season_from=season_from,
                         week_from=week_from,
                         season_to=season_to,
                         week_to=week_to)

    data = games.get_game_data(game_urls=g)

    return data.to_csv(f'data/{filename}.csv')


if __name__ == "__main__":
    get_dfs_data()
