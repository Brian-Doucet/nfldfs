# nfldfs

[![codecov](https://codecov.io/gh/BrianDoucet01/daily-fantasy-sports/branch/master/graph/badge.svg)](https://codecov.io/gh/BrianDoucet01/daily-fantasy-sports)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![HitCount](http://hits.dwyl.com/BrianDoucet01/daily-fantasy-sports.svg)](http://hits.dwyl.com/BrianDoucet01/daily-fantasy-sports)

`nfldfs` is a Python package for NFL daily fantasy sports analysis. It provides an easy interface to scrape data for DraftKings, FanDuel, and Yahoo! from [rotoguru1](http://rotoguru.net) so that you don't have to.

* [Features](https://github.com/BrianDoucet01/daily-fantasy-sports#features)
* [Installation](https://github.com/BrianDoucet01/daily-fantasy-sports#installation)
* [Usage](https://github.com/BrianDoucet01/daily-fantasy-sports#usage)
  * [IPython or Jupyter](https://github.com/BrianDoucet01/daily-fantasy-sports#ipython-or-jupyter-notebook)
  * [Use the CLI tool](https://github.com/BrianDoucet01/daily-fantasy-sports#using-the-cli)
* [Future Work](https://github.com/BrianDoucet01/daily-fantasy-sports#future-work)


## Features

+ Search for data using combinations of season and week
+ Return data only for the daily fantasy sites you care about
+ Work with results as a pandas DataFrame or use the CLI to output results directly to a `.csv`


## Installation
`nfldfs` is supported for Python 3 can be installed from the repo. You'll need [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) installed.

*These are the steps for getting your dev environment up and running on a Mac*

```bash
# Clone the repo
git clone https://github.com/BrianDoucet01/daily-fantasy-sports.git
cd daily-fantasy-sports
tree

# If cloned successfully your directory structure should look like this
# working in ~/daily-fantasy-sports
├── LICENSE
├── README.md
├── nfldfs
│   ├── __init__.py
│   ├── games.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_games.py
│   │   └── test_utils.py
│   └── utils.py
└── requirements.txt

# Create a virtual environment for nfldfs and then activate it
virtualenv ~/virtualenvs/nfldfs -p python3 --no-site-packages
. ~/virtualenvs/nfl/bin/activate

# Install the project requirements
pip install -r requirements.txt
```


## Usage
Here are some quick and dirty examples that review how to import the package, search for dfs stats and scrape data. For more robust examples and a data dictionary, refer to the [docs](https://github.com/BrianDoucet01/daily-fantasy-sports/tree/master/docs) folder.

### IPython or Jupyter Notebook

**Get DraftKings salary and points data for the entire 2019 season.**

```Python
from nfldfs import games as games

# Scrape DraftKings salary and points data for the entire 2019 season
g = games.find_games(['dk'], 2019, 1, 2019, 17)
stats = games.get_game_data(g)

type(stats)
pandas.core.frame.DataFrame

# Confirm there's data for weeks 1-17
stats.week.unique()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17])

# Inspect a random sample of 10 rows
stats.sample(10)

       week year      player_name       position team_name home_or_away  \
gid                                                                    
5588    16  2019      Penny, Elijhaa       RB       nyg            a   
5765    11  2019    Spencer, Diontae       WR       den            a   
5556     3  2019      Samuel, Curtis       WR       car            a   
5790    17  2019    Blake, Christian       WR       atl            a   
5649    16  2019      Foster, Robert       WR       buf            a   
7031    12  2019          Washington      Def       was            h   
4675    14  2019       Henry, Hunter       TE       lac            a   
1403     3  2019        Dalton, Andy       QB       cin            a   
5386     3  2019      Lockett, Tyler       WR       sea            h   
1519     7  2019  Trubisky, Mitchell       QB       chi            h  

      opponent_name  points  salary dfs_site  
gid                                          
5588           was    0.00  3000.0       dk  
5765           min    0.00  3000.0       dk  
5556           ari   16.30  4800.0       dk  
5790           tam    0.00  3000.0       dk  
5649           nwe    0.00  3000.0       dk  
7031           det   21.00  3000.0       dk  
4675           jac   11.90  5100.0       dk  
1403           buf   18.06  5300.0       dk  
5386           nor   35.40  6200.0       dk  
1519           nor   20.04  5100.0       dk  
```


**Get data for DraftKings, FanDuel, and Yahoo! for week 2 of the 2018 season.**

```python
# Get data for DraftKings, FanDuel, and Yahoo! for week 2 of the 2018 season
all_sites = games.find_games(['dk', 'fd', 'yh'], 2018, 2)
week_2_stats = games.get_game_data(all_sites)

# Sample of 1 row for each dfs site
week_2_stats.groupby('dfs_site').apply(lambda x: x.sample(1))

                week year    player_name   position   team_name   home_or_away  \
dfs_site gid                                                                
dk       7018     2  2018     New England      Def       nwe            a   
fd       3670     2  2018   Ginn Jr., Ted       WR       nor            h   
yh       5631     2  2018  Ridley, Calvin       WR       atl            h   

                opponent_name  points salary   dfs_site  
dfs_site gid                                          
dk       7018           jac     3.0  3000.0       dk  
fd       3670           cle     5.5  6800.0       fd  
yh       5631           car    14.7    10.0       yh  


```

### Using the CLI

<img src="cli.gif" alt="Using the nfldfs CLI" style="width: 500px;"/>


## Future Work
* Adding additional functionality to the CLI
    * Options to preview data before output
    * Functions for analysis
* Incorporating more data:
    * Weather
    * Game schedules and slates (Main, Sunday Night etc...)
* Scraping  points and salary data for the current season
* Downloading projections that are available from various sites
