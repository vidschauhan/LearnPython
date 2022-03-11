# Created by vidit.singh at 11-03-2022

'''
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-####
Use the Python os module and regular expressions to iterate through each file, open it, and search for a telephone number.
Good luck!
'''

import os

dir_location = "D:\\Data Engineering\\Udemy - 2021 Complete Python Bootcamp From Zero to Hero in Python\\Udemy - 2021 " \
               "Complete Python Bootcamp From Zero to Hero in Python\\14. Advanced Python Modules\\zips\\"


def unzip(zip_path, zip_file):
    import zipfile
    with zipfile.ZipFile(zip_path + zip_file, 'r') as zip_ref:
        zip_ref.extractall(zip_path)


def traverse_dir(dir_loc, dirs, pattern1):
    d_path = dir_loc + dirs
    for folder, sub_folder, files in os.walk(d_path):
        if os.path.exists(folder):
            for s_fol in sub_folder:
                sub_folder_path = os.path.join(d_path, s_fol)
                if os.path.exists(sub_folder_path):
                    for filename in os.listdir(sub_folder_path):
                        if os.path.isfile(filename) or filename.endswith('.txt'):
                            data = open_file(os.path.join(sub_folder_path, filename))
                            match_content(data, pattern1)


def open_file(path):
    try:
        with open(path, mode='r+') as file:
            return file.read()

    except FileNotFoundError as ex:
        print(f"File not located at the location ::: {path}")
    finally:
        file.close()


def match_content(data, pat):
    import re
    data1 = re.findall(pat, data)
    if data1 is not None:
        for k in data1:
            print(f'Data found :: {k}')


if __name__ == "__main__":
    print('Exracting zip...')
    unzip(dir_location, 'unzip_me_for_instructions.zip')
    print('Exracting zip completed!')
    print(" Traversing directory for file...")
    traverse_dir(dir_location, "extracted_content", r'\d{3}-\d{3}-\d{4}')
