# Created by vidit.singh at 15-06-2022

import json
import src.utils.datasets as ds

base_dir = ds.base_dir()
file = open(base_dir+'\\single_document.json')
single_doc_dict = json.load(file)  # json.load() takes file object as parameter
print(single_doc_dict['first_name'])

youtube_json_file = open(base_dir + 'youtube_playlist_items.json')

id_list = [item['id'] for item in json.load(youtube_json_file)['items']]
print(id_list)


