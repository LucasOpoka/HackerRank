#https://www.hackerrank.com/challenges/floor-ceil-and-rint

import numpy as np
np.set_printoptions(legacy='1.13')
arr, lst = np.array(input().split(), float), ['floor','ceil','rint']
for i in lst: exec(f'print(np.{i}(arr))')