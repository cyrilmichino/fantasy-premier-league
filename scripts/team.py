import json
import requests
import pandas as pd

base_url = 'https://fantasy.premierleague.com/api/'
team_id = 1079394
response = requests.get(base_url + 'fixtures/')
response = requests.get(base_url + 'entry/{team_id}/')
print(response.status_code)
print(response.content)