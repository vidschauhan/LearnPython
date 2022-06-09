# Created by vidit.singh at 06-06-2022

# orders_file = open(file_path, 'r')
# print(orders_file.read())

# This is better approach as this will not load whole file in memory. WIth huge files it becomes memory problems.
def get(filename):
    file = f'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\retail_db\\{filename}\\part-00000 '
    with open(file, 'r') as fileobject:
        return fileobject.read().splitlines()
