# Created by vidit.singh at 14-06-2022

import pandas as pd
import src.utils.datasets as ds

order_items_df = ds.get_dataframe('order_items', pd)
orders_df = ds.get_dataframe('orders', pd)

# writing aggregated data into csv.
order_items_df.groupby('order_item_order_id')['order_item_subtotal']\
    .agg(['min', 'max', 'sum', 'count'])\
    .rename(columns={'sum': 'revenue', 'count': 'order_count'})\
    .to_csv(ds.output_dir() + '\\revenue.csv')
