import itertools

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
