# Created by vidit.singh at 15-06-2022
from src.utils.posgress import Posgress
import pandas as pd
import src.utils.datasets as ds

connection = Posgress.connect('localhost', 5432, 'itversity_retail_db_batch_processing', 'itversity_retail_user_batch',
                              'password')
order_items_df = ds.get_dataframe('order_items', pd)
orders_df = ds.get_dataframe('orders', pd)

print(connection)
cursor = connection.cursor()

insert_query = ("""
        INSERT INTO orders 
            (order_id, order_date, order_customer_id, order_status)
        VALUES 
            (%s, %s, %s, %s)
    """)


def truncate_table(cur):
    return cur.execute('TRUNCATE TABLE orders')


def load_order_in_sequence(conn, cur, query, order_data):
    for order in order_data:  # Inserting row and committing in each iteration. ( This is bad practice and less
        # efficient)
        cur.execute(query, order)
        conn.commit()


# Data frames are directly not inserted into database. we need to convert them either list of tuples or list of


def load_order_in_single_commit(conn, cur, query, order_data):
    # Inserting row at a time but committing at the end. this is faster than previous approach. But may have
    # performance overhead when python engine and database engine are not located at the same geographical area.
    for order in order_data:
        cur.execute(query, order)

    conn.commit()


# Using execute many approach.
def load_bulk_data_at_once(conn, cur, query, order_data):
    cur.executemany(query, order_data)
    conn.commit()


# Best practice inserting data, as it creates check points on each batch insert, that are recoverable if any batch
# fails.
def load_orders_in_batches(conn, cur, query, order_data, batch_size=10000):
    for i in range(0, len(order_data), batch_size):
        cur.executemany(query, order_data[i: i + batch_size])
        conn.commit()


if __name__ == '__main__':
    # lists. where each row represent as a list or tuples. ---> orders_df.values.tolist()
    # load_order_in_sequence(connection, cursor, insert_query, orders_df.values.tolist()[:10000])
    # load_order_in_single_commit(connection, cursor, insert_query, orders_df.values.tolist()[:10000])
    # load_bulk_data_at_once(connection, cursor, insert_query, orders_df.values.tolist())
    truncate_table(cursor)
    load_orders_in_batches(connection, cursor, insert_query, orders_df.values.tolist())
