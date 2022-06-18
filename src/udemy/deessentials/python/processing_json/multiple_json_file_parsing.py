# Created by vidit.singh at 16-06-2022

import json
import src.utils.datasets as ds

json_string = ds.open_file(ds.base_dir() + '\\customers.json', 'r')

json_list_dicts = list(map(json.loads, json_string))
emails = list(map(lambda j: j['email'], json_list_dicts))
print(emails)
