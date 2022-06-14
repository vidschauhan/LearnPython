# Created by vidit.singh at 12-06-2022

import pandas as pd

l = [12.32, 34.22, 33.12, 43.44, 78.55]

d = {'JAN': 31,
     'FEB': 28,
     'MAR': 32,
     'APR': 30}

d_res = pd.Series(d, name='dict_series')
l_res = pd.Series(l, name='list_series')
print(d_res)
print(d_res[0])
print(d_res['FEB'])
print(f'pandas list series {l_res[3]}')
