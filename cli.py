#!/usr/bin/env python3
import click

from nfldfs import games as games


# Welcome message
print('Welcome to nfldfs!\n')

# Options for command line interface
@click.command()
<<<<<<< HEAD
@click.argument('dfs_site', nargs=-1)
#@click.option('--dfs_site', required=True, prompt='Which dfs site(s)?', help='Name of the DFS site')
@click.option('--season_from', required=True, type=int, prompt='Season beginning', help='The season number in the beginning search range')
=======
@click.option('--dfs_site', type=str, prompt='Which dfs site(s)?', help='Name of the DFS site')
@click.option('--season_from',type=int, prompt='Season beginning', help='The season numnber in the beginning search range')
@click.option('--week_from', type=int, prompt='Week beginning')
>>>>>>> ec28fdd02b8895a8eba032a0236e028098979543
@click.option('--season_to', type=int, prompt='Season ending')
@click.option('--week_to', type=int, prompt='Week ending')
@click.option('--filename', type=str, prompt='Output Filename')
def get_dfs_data(dfs_site, season_from, season_to, week_from, week_to, filename):
    """
    Simple program to scrape NFL daily fantasy stats.
    """
<<<<<<< HEAD
    print(list(dfs_site))
    dfs_site = (dfs_site)
=======
    dfs_site = [dfs_site]

    print(dfs_site, season_from, season_to, week_from, week_to, filename)
>>>>>>> ec28fdd02b8895a8eba032a0236e028098979543
    g = games.find_games(dfs_site=dfs_site,
                         season_from=season_from,
                         week_from=week_from,
                         season_to=season_to,
                         week_to=week_to)

    data = games.get_game_data(game_urls=g)

    return data.to_csv(f'data/{filename}.csv')

if __name__ == "__main__":
    get_dfs_data()
