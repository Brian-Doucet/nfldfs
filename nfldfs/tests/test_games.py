#!/usr/bin/env python3

import pandas as pd
import pytest
import nfldfs.games as games

# Should return 1 URL string
def test_find_games_pass():
    assert len(games.find_games(['dk'], 2018, 1)) ==1
    assert len(games.find_games(['dk', 'fd'], 2018, 1)) ==2

# Return errors for invalid years and dfs site name
def test_find_games_error():
    with pytest.raises(Exception) as info:
        games.find_games(['dk'], 2013, 1)

    assert "Invalid year" in str(info.value)

def test_find_games_error():
    with pytest.raises(Exception) as info:
        games.find_games(['DK'], 2016, 1)

    assert "Invalid dfs site" in str(info.value)

# Confirm that a dataframe object is returned
def test_get_game_data_is_dataframe():
    g = games.find_games(['dk'], 2018, 5)
    df = games.get_game_data(g)

    assert type(df) == pd.DataFrame
    assert len(list(df.columns)) == 10
