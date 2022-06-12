# Created by vidit.singh at 10-06-2022

import itertools as iter

qop = list(iter.accumulate([1, 2, 3, 4, 5]))  # add accumulative to previous element
print(qop)

import operator as op

sale_data = [
    (2020, 123),
    (2021, 132),
    (2022, 753),
    (2023, 864),
    (2024, 124),
    (2025, 846)
]
sale_month = map(lambda sm: sm[0], sale_data)
sale_revenue = map(lambda sr: sr[1], sale_data)

accumulated_sales = list(iter.accumulate(sale_revenue))
data = list(zip(sale_month, accumulated_sales))
print(data)

var1 = [1, 2, 3]
var2 = (4, 5, 6)
var3 = list(iter.chain(var1, var2))
print(var3)

date_strings = ['2021-11-22', '2021-11-23', '2021-11-24', '2021-11-25', ' 2021-11-26', '2021-11-27', '2021-11-28']
n = iter.dropwhile(lambda n: n < '2021-11-27', date_strings)
print(list(n))
