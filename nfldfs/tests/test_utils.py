#!/usr/bin/env python3

import pytest
import nfldfs.utils as utils


# These are valid parameters and should return no errors
def test_game_parameters_validator_pass():
    assert utils.game_parameters_validator('dk', 2019) == None
    assert utils.game_parameters_validator('fd', 2014) == None
    assert utils.game_parameters_validator('yh', 2016) == None

# Raise an error for invalid dfs site
def test_game_parameters_validator_raise_error_site():

    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dd', '2019')

    assert "Invalid dfs site" in str(info.value)


# Raise an error for invalid year
def test_game_parameters_validator_raise_error_year():

    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', '2021')

    assert "Invalid year" in str(info.value)
