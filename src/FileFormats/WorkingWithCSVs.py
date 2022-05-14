# Created by vidit.singh at 19-04-2022
import csv


def get_aum_data():
    file = open("C:\\Users\\vidit.singh\\Downloads\\ELSS_MF_2_12_2022.csv", 'r', encoding='utf-8')
    data = csv.reader(file)
    op = iter(data)

    for lines in op:
        if lines[0] != "Name":
            yield lines[0], float(lines[3])


max_aum = 0.0

for name, data in get_aum_data():
    max_aum = max(max_aum, data)

for name,max_ in get_aum_data():
    if max_aum == max_:
        print(name + " ----> " + str(max_))
