#https://www.hackerrank.com/challenges/np-arrays

import numpy

def arrays(arr):
    return numpy.fromiter(arr[::-1], dtype=float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)