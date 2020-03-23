import pytest
import nfldfs.utils as utils
#print(utils.game_parameters_validator('dk', 2019))

# Assert this returns the no errors
def test_game_parameters_validator_pass():
    assert utils.game_parameters_validator('dk', 2019) == None

# Assert that this raises an error for invalid dfs site
def test_game_parameters_validator_raise_error_site():

    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dd', '2019')


    assert "Invalid dfs site" in str(info.value)


# Assert this raises an error for invalid year
def test_game_parameters_validator_raise_error_year():

    with pytest.raises(Exception) as info:
        utils.game_parameters_validator('dk', '2021')

    assert "Invalid year" in str(info.value)
