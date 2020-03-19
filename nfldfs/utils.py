#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:28:43 2020

@author: bdoucet
"""


def game_parameters_validator(dfs_site, season_number):

    config = {'dk': [2014, 2015, 2016, 2017, 2018, 2019],
              'fd': [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'yh': [2016, 2017, 2018, 2019]}

    season_numbers = config.get(dfs_site)
    if not season_numbers:
        print('Enter a valid dfs site')
        print('{} are valid dfs sites'.format(config.keys()))

    for season in season_numbers:
        if season_number == season:
            return True

    print('{} is out of range'.format(season_number))
    print('{} are valid years'.format(season_numbers))

    return False
