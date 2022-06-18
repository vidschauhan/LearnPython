# Created by vidit.singh at 16-06-2022

import pandas as pd
import src.utils.datasets as ds

base_dir = ds.base_dir()

customer_df = pd.read_json(base_dir + '\\customers.json', lines=True)
course_df = pd.read_json(base_dir + '\\courses.json', lines=True)
print("***************************************************************")
print(customer_df)
print("***************************************************************")


# writing file into json buffers orient= split -> it splits Index, columns and data to [list of data]
split_json_data = customer_df.to_json(orient='split')
print(split_json_data)
print("***************************************************************")


# reading data from json buffers. from orient=split format
#print(pd.read_json(orient='split'))
print("***************************************************************")

print(course_df.to_json(orient='records'))  # array of json documents
print("***************************************************************")
print(customer_df.to_json(orient='records', lines=True))  # Multiple jsons with one json per line
print("***************************************************************")
