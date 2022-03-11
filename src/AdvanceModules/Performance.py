# Created by vidit.singh at 10-03-2022

def get_range1(num):
    return [str(num1) for num1 in range(num)]


def get_range2(num):
    return list(map(str, range(num)))


stmt = ''' get_range1(1000) '''
setup = ''' def get_range2(num):return list(map(str, range(num)))'''

import timeit

t1 = timeit.timeit(stmt, setup, number=1000)
