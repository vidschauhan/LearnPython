# Created by vidit.singh at 18-06-2022
import os
import pandas as pd
import src.utils.datasets as ds

orders_json = open(ds.get_json_path('orders'))  # Reading files dynamically see implementation in utils
orders_df = pd.read_json(orders_json, lines=True, chunksize=5000)  # this returns json reader object.
print(type(orders_df))

for orders in orders_df:
    print(orders.head(10))
