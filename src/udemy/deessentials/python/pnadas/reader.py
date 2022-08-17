# Created by vidit.singh at 19-06-2022
import pandas as pd
import src.utils.datasets as ds


def get_json_reader(table, chunk=1000):
    orders_json = open(ds.get_json_path(table))  # Reading files dynamically see implementation in utils
    print(f'Reading data from {table} json file in batch size {chunk}')
    return pd.read_json(orders_json, lines=True, chunksize=chunk)  # this returns json reader object.
