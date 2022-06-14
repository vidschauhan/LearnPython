# Created by vidit.singh at 13-06-2022
import pandas as pd
import src.utils.datasets as ds

order_items_df = ds.get_dataframe('order_items', pd)
orders_df = ds.get_dataframe('orders', pd)
print(order_items_df.columns)

print('***************************************************')
# print('Sub_totals :: ', order_items_df[order_items_df.order_item_order_id == 2].order_item_subtotal)
# print('Sum of sub_totals :: ', order_items_df[order_items_df.order_item_order_id == 2]['order_item_subtotal'].sum())
print('*************** Group Aggregations ****************')
print(list(orders_df.groupby(orders_df['order_date'])['order_id'])[:2])
print('***************************************************')
print(orders_df.groupby(orders_df['order_date'])['order_id'].count())
print('***************************************************')
print('Aggregate subtotal by order_id :: ', order_items_df
      .groupby('order_item_order_id')['order_item_subtotal'].sum())
print('***************************************************')
print('Aggregate by order_id :: ',
      order_items_df
      .groupby('order_item_order_id')['order_item_subtotal']
      .agg(['min', 'max', 'count', 'sum']))
print('***************************************************')
print('Aggregate by order_id :: ',
      order_items_df
      .groupby('order_item_order_id')['order_item_subtotal']
      .agg(['min', 'max', 'count', 'sum'])
      .rename(columns={'count': 'item_count', 'sum': 'revenue'}))
print('***************************************************')
print(order_items_df.rename(columns={'order_item_order_id': 'order_id'}))
print('***************************************************')
print(order_items_df
      .groupby('order_item_order_id')['order_item_subtotal']
      .agg(['sum', 'count'])
      .rename(columns={'count': 'item_count', 'sum': 'revenue'})
      .reset_index())  # reset index position of the columns.

print('***************************************************')
# slicing order_date from orders, to introduce new column as order_months. use sort_index() or sort_value()
orders_df['order_months'] = orders_df.order_date.str.slice(0, 7)
order_grp = orders_df.query('order_status == "CLOSED"').groupby('order_months')['order_id'].count().sort_index()
print(order_grp)
print('***************************************************')
