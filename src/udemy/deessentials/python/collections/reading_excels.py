# Created by vidit.singh at 04-06-2022

file_path = 'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\retail_db\\orders' \
            '\\part-00000 '
# orders_file = open(file_path, 'r')
# print(orders_file.read())

# This is better approach as this will not load whole file in memory. WIth huge files it becomes memory problems.
with open(file_path, 'r') as fileobject:
    orders = fileobject.read().splitlines()
    orders_tuples = [(*order.split(','),) for order in orders]
    print(orders_tuples[:2])
    dates = [date[1] for date in orders_tuples]
    print(dates[:10])
    print('**************************************************************************')

#################################################
# To sort the dict convert dict to list of tuples, then use sort()
famous_players = {'Sachin Tendulker': 'Cricketer', 'Brian Lara': 'Cricketer',
                  'Harman': 'Badminton', 'Nadal': 'Tennis'}

sort_data_as_list = sorted(famous_players)  # this will sort data by keys and convert it into list.
print(sort_data_as_list)

# to convert dict to list of sorted tuples by keys
sports_items = sorted(famous_players.items())
print(sports_items)

# to sort by values use
sorted_values = sorted(famous_players.items(), key=lambda player: player[1])
print(sorted_values)  # Now the values are sorted by value section.
