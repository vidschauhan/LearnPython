# Created by vidit.singh at 18-06-2022

import requests
import pandas as pd

url = "https://api.github.com/users/dgadiraju/repos"

data = requests.get(url).json()
# print(data)

payload = requests.get('https://api.github.com/repositories', params={'since': 200}).json()

# print(payload)
git_data = list(
    map(lambda git_payload: {'id': git_payload['id'], 'name': git_payload['name'], 'url': git_payload['url'],
                             'type': git_payload['owner']['type']}, payload))

# list all users group by Organisation

git_data_df = pd.DataFrame(git_data)
# print(git_data_df.head(3))

grouped_data = git_data_df.groupby('type')['name']
grouped_data_count = git_data_df.groupby('type')['name'].count()
print(list(grouped_data))
print("************************************************************")
print(grouped_data_count)

print("************************************************************")
print(git_data_df.sort_values(by=['type', 'name']).head(2))

import sys
import os
print("Python Current Version:-", sys.version)

print(os.environ.items())
print('getting os environment variables : ',os.environ.get('COMPUTERNAME'))