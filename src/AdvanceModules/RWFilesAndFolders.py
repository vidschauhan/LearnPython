# Created by vidit.singh at 10-03-2022

# Read write file and folders

import os

print(os.getcwd())
print(os.listdir('D:\Data Engineering\Python Scripts'))

for folder, sub_folder, file in os.walk("D:\Data Engineering"):
    print(f'Currently looking at {folder}')
    print('\n')
    print('The sub folders are :::')
    for sub in sub_folder:
        print(f'\t Sub folder : {sub}')

    print('\n')
    print('The files are :::')
    for f in file:
        print(f'\t Files : {file}')
    print('\n')
