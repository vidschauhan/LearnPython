# Created by vidit.singh at 06-06-2022

# orders_file = open(file_path, 'r')
# print(orders_file.read())

# This is better approach as this will not load whole file in memory. WIth huge files it becomes memory problems.
import os


def get(filename):
    file = get_file_path(filename)
    with open(file, 'r') as fileobject:
        return fileobject.read().splitlines()


def open_file(filename, modes):
    with open(filename, modes) as fileobject:
        return fileobject.read().splitlines()


def get_file_path(filename):
    return f'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\retail_db\\{filename}\\part-00000 '


def output_dir():
    return 'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\outputs'


def base_dir():
    return 'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\'


def get_json_path(dir_name):
    base_dirs = 'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\retail_db_json\\'
    json_file = os.listdir(f'{base_dirs}{dir_name}')[0]  # assuming there is only 1 file in directory
    return f'{base_dirs}{dir_name}\\{json_file}'


def get_dataframe(filename, pd):
    order_schema = ['order_id', 'order_date', 'customer_id', 'order_status']
    order_items_schema = ['order_item_id', 'order_item_order_id', 'order_item_product_id', 'order_item_quantity',
                          'order_item_subtotal', 'order_item_product_price']
    return pd.read_csv(get_file_path(filename), header=None,
                       names=order_schema if filename == 'orders' else order_items_schema)
