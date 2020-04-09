#!/usr/bin/env python3


def validate_season(season_from, season_to, valid_seasons):

    if season_from > season_to:
        raise Exception('Season From must be less than or equal to Season To')

    if season_from not in valid_seasons:
        raise Exception('Season From {} is out of scope of the valid seasons for this site: {}'.format(season_from, valid_seasons))

    if season_to not in valid_seasons:
        raise Exception('Season To {} is out of scope of the valid seasons for this site: {}'.format(season_to, valid_seasons))


def validate_week(week_from, week_to):

    if week_from > week_to:
        raise Exception('Week From must be less than or equal to Week To')

    if not 1 <= week_from <= 17:
        raise Exception('Week From must be between 1 & 17 (inclusive)')

    if not 1 <= week_to <= 17:
        raise Exception('Week To must be between 1 & 17 (inclusive)')


def game_parameters_validator(dfs_site, season_from, season_to, week_from, week_to):

    config = {'dk': [2014, 2015, 2016, 2017, 2018, 2019],
              'fd': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'yh': [2016, 2017, 2018, 2019]}

    valid_season_numbers = config.get(dfs_site)

    if not valid_season_numbers: # unable to find the key
        raise Exception('Invalid dfs site')

    validate_season(season_from=season_from, season_to=season_to, valid_seasons=valid_season_numbers)

    validate_week(week_from=week_from, week_to=week_to)

