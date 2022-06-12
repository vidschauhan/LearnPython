import csv

# Created by vidit.singh at 11-06-2022
path = 'D:\\Data Engineering\\Projects\\Internal\\bootcamp\\data-engineering-spark\\data\\retail_db\\orders\\'
file = path + 'part-00000'

with open(file, 'r') as fileobject:
    file_data = fileobject.read().splitlines()
    csv_data = csv.reader(file_data)
    order_transform = list(
        tuple(map(lambda item: tuple(map(lambda order: int(order) if str(order).isdigit() else order, csv_data)),
                  csv_data)))
    print(order_transform)

li = ('1,name,age', '2,ggg,eww')
print(list(csv.reader(li)))

li1 = ('1\tname\tage', '2\tggg\teww')
print(list(csv.reader(li1, delimiter='\t')))


def write_lines():
    with open(path + 'new_file', mode='x') as f:
        l_op = list(csv.reader(li1, delimiter='\t'))
        scv_writer = csv.writer(f, delimiter='|')
        scv_writer.writerows(l_op)

def write_headers_and_data():
    file_name = path + 'new_file1'
    li = [{'id' : 1,'name' : 'Vidit','age' : 3},
          {'id' : 2,'name' : 'Singh','age' : 13}]
    with open(file_name, mode='w') as f:
        l_op = csv.reader(li1, delimiter='\t')
        scv_writer = csv.DictWriter(f,
                                    fieldnames=['id', 'name', 'age'],
                                    delimiter=';')
        scv_writer.writerows(li)


write_headers_and_data()
