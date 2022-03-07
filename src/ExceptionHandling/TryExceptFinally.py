# Created by vidit.singh at 07-03-2022

try:
    result = '10' + 20
except:
    print('String Expected but int provided')
else:
    print('Else will be executed if there is no exception!')
finally:
    print('Always run')

try:
    f = open('Vidit.txt', 'r')
    f.write("this is a line")
except (OSError, FileNotFoundError) as ex:
    print(f"File not exist ::::  {ex}")
except:
    print(" All other exceptions!")
