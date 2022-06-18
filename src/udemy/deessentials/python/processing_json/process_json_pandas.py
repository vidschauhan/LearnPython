# Created by vidit.singh at 16-06-2022


import json
import pandas as pd

import src.utils.datasets as ds

base_dir = ds.base_dir()
# reading json using pandas
json_df = pd.read_json(base_dir + '\\customers.json', lines=True)
# print(json_df)

# reading complex json files
youtube_json_file = open(base_dir + 'youtube_playlist_items.json')
yt_items = json.load(youtube_json_file)['items']
yt_items_df = pd.DataFrame(yt_items)
print(yt_items_df)

# flattening the complex json to dataframes . using pandas json_normalize
print(pd.json_normalize(yt_items))
