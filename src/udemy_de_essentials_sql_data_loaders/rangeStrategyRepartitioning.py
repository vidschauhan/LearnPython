# Created by vidit.singh at 24-05-2022
import pandas as pd
from pandas.tseries.offsets import MonthBegin, MonthEnd

from src.utils.posgress import Posgress

connection = Posgress.connect('localhost', 5432, 'itversity_retail_db', 'itversity_retail_user', 'password')
print(connection)

months = pd.date_range(start='1/1/2017', end='12/31/2018', freq='1M')

cursor = connection.cursor()
table_name = 'users_range_part'
query = '''
CREATE TABLE {table_name}_{yyyymm}
PARTITION OF {table_name}
FOR VALUES FROM ('{begin_date}') TO ('{end_date}')
'''
for month in months:
    begin_date = month - MonthBegin(1)
    end_date = month + MonthEnd(0)
    print(f'Adding partition for {begin_date} and {end_date}')
    cursor.execute(
        query.format(
            table_name=table_name,
            yyyymm=str(month)[:7].replace('-', ''),
            begin_date=str(begin_date).split(' ')[0],
            end_date=str(end_date).split(' ')[0]
        ), ()
    )
connection.commit()
cursor.close()
connection.close()
