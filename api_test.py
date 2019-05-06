# this is a simple api test, working on shaping the data how I want

import requests

# set name to lookup stats
player_name = 'arch linux'

# get data from api listed
api = ('https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=%s' % player_name)
get_data = requests.get(api)

data_list = get_data.text.splitlines()

print(data_list)