# Created by vidit.singh at 12-06-2022

import src.utils.datasets as ds
import pandas as pd

list1=[[1,2],[3,4],[5,6]]
df=pd.DataFrame(list1)
print(df)

file_path = ds.get_file_path('orders')

order_schema = ['order_id', 'order_date', 'customer_id', 'order_status']
orders_df = pd.read_csv(file_path,
                        header=None,
                        names=order_schema)
print(orders_df.head(10)) # Prints 10 rows from dataframes.
print('****************************************************************')
print(orders_df.order_date[4])

sales_ld = [(1, None, 2800), (2, 'Vidit', 50000), (2, 'Vanshu', 46000)]
sales_schema = ['id', 'name', 'sales']
sales_df = pd.DataFrame(sales_ld, columns=sales_schema)
print(sales_df)

print(sales_df.name)
# or
print(sales_df['name'])

print(sales_df[['name', 'sales']])

# dataframe from dicts
print('**************************************')
d_sales = [{'id': 123, 'name': 'Vidit'},
           {'id': 345, 'name': 'Singh', 'age': 21},
           {'id': 456, 'name': 'Vanshu'},
           {'id': 456}]

df_d_sales = pd.DataFrame(d_sales)
print(df_d_sales)
print(df_d_sales.shape)
print('**************************************')

print(df_d_sales.count())
print(df_d_sales.count()[1])
print(df_d_sales.dtypes)

# print(df_d_sales.fillna(0)) # replaces nan with
print(df_d_sales.fillna({'name': 'NAN',
                         'age': 0}))
# replaces nan with 0 and name with NAN. This will not make nay changes in
# original dataframe instead crate a new one.

print('**************************************')

# Dropping Dataframes.
# Dropping columns. to drop columns specify axis = 1, by default axis = 0 which is for rows.
print(df_d_sales.drop(['name', 'age'], axis=1))
print(df_d_sales.drop(columns='name'))
print(df_d_sales.drop(columns=['name', 'age']))

# deleting rows
print(df_d_sales.drop([0, 1]))  # rows 0,1 deleted.

print('**************************************')
# renaming columns.
print(df_d_sales.columns)
df_d_sales.columns = ['e_id', 'e_name', 'e_age']
print(df_d_sales)

print('**************************************')
print(df_d_sales.sort_index(ascending=False))
print(df_d_sales.sort_values(by='e_name', ascending=False))
print(df_d_sales.sort_values(by=['e_name', 'e_id'], ascending=[False, True]))
