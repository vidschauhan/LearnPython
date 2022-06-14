# Created by vidit.singh at 13-06-2022
import pandas as pd
import src.utils.datasets as ds

order_schema = ['order_id', 'order_date', 'customer_id', 'order_status']
orders_df = pd.read_csv(ds.get_file_path('orders'), header=None, names=order_schema)

print(orders_df.columns)  # print columns name
print(orders_df.head(10))
print('**********************************************************')
print(orders_df[orders_df.customer_id == 11599])  # filtering data
print('**********************************************************')
print(orders_df[orders_df['customer_id'] == 11599])  # filtering data
print('**********************************************************')
print(orders_df.query('customer_id == 8827'))  # filtering data using query method

print('**********************************************************')

print(orders_df[(orders_df.customer_id == 5657) & (orders_df.order_status == 'PENDING')])
print('**********************************************************')
print(orders_df.query('customer_id == 5657 and order_status == "PENDING"'))
print('**********************************************************')
print(orders_df.query('order_date.str.startswith("2013-07") and order_status == "PENDING"', engine='python'))
print('**********************************************************')
print(orders_df[(orders_df.order_date.str.startswith("2013-07")) & (orders_df.order_status == "PENDING")])
print('**********************************************************')
print(orders_df[(orders_df.order_date.str.startswith("2013-08")) &
                (orders_df.customer_id == 5602) &
                (orders_df.order_status.isin(["COMPLETE", "PENDING"]))])
print('**********************************************************')
print(orders_df.query('order_status in ["COMPLETE","CLOSED"]'))
