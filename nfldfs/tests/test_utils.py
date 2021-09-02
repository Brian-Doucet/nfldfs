#!/usr/bin/env python3

import pytest
import nfldfs.utils as utils


# These are valid parameters and should raise no errors
def test_game_parameters_validator_pass():
    assert utils.game_parameters_validator('dk', 2019, 2019, 1, 14) is None
    assert utils.game_parameters_validator('fd', 2014, 2016, 2, 6) is None
    assert utils.game_parameters_validator('yh', 2016, 2017, 1, 1) is None


# Raise an error for invalid dfs site
def test_game_parameters_validator_raise_error_site():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dd', 2019, 2019, 1, 1)

    assert "Invalid dfs site" in str(info.value)


# Raise an error for invalid year
def test_game_parameters_validator_raise_error_year():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', '2012', '2019', 1, 1)


    assert "Season From 2012 is out of scope of the valid seasons for this site: [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]" in str(
        info.value)


def test_game_parameters_validator_raise_error_season_to():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('yh', 2016, 2022, 1, 15)

    assert ("Season To 2022 is out of scope of the valid seasons for this site: [2016, 2017, 2018, 2019, 2020, 2021]") in str(
        info.value)

# Set of tests to validate that errors are raised for invalid week numbers


def test_game_parameters_validator_week_from_raise_error():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', 2018, 2019, 7, 1)

    assert "Week From must be less than or equal to Week To" in str(info.value)


def test_game_parameters_validator_week_from_not_in_range_raise_error():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', 2019, 2019, 0, 17)

    assert "Week From must be between 1 & 17 (inclusive)" in str(info.value)


def test_game_parameters_validator_week_to_not_in_range_raise_error():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', 2019, 2019, 1, 18)

    assert "Week To must be between 1 & 17 (inclusive)" in str(info.value)

# Set of tests to validate that errors are raised for invalid season numbers


def test_game_parameters_validator_raise_error_season_from():
    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', 2020, 2019, 1, 2)

    assert "Season From must be less than or equal to Season To" in str(
        info.value)
