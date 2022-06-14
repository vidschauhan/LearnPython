# Created by vidit.singh at 14-06-2022
import pandas as pd
import src.utils.datasets as ds

order_items_df = ds.get_dataframe('order_items', pd)
orders_df = ds.get_dataframe('orders', pd)

# resetting index for both data frame so that join happens on same attribute
filtered_data = orders_df.query('order_status in ["COMPLETE","CLOSED"]')
filtered_data.set_index('order_id')
order_items_df.set_index('order_item_order_id')

joined_data = filtered_data.join(order_items_df, how='inner')
# print(joined_data)

# compute daily_revenue using order.date and order_item_order_subtotal considering only COMPLETE and CLOSED orders

print(joined_data
      .groupby('order_date')['order_item_subtotal']
      .agg(['sum'])
      .rename(columns={'sum': 'total_revenue'})
      )

print("*****************************************************************")
# get all orders which are no corresponding orders.

left_joined_data = orders_df.set_index('order_id') \
    .join(order_items_df.set_index('order_item_order_id'), how='left') \
    .query('order_item_id.isna()')
print(left_joined_data)

print("*****************************************************************")
#
print(joined_data
      .groupby(['order_date', 'order_item_product_id'])['order_item_subtotal']
      .agg(['sum'])
      .rename(columns={'sum': 'total_revenue'})
      )
