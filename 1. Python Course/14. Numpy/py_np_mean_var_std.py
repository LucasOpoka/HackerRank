#https://www.hackerrank.com/challenges/np-mean-var-and-std

import numpy as np
lst = [('mean','1'),('var','0'),('std','None')]
arr = np.array([input().split() for _ in range(int(input().split()[0]))], int)
for i in lst: exec(f'print(np.{i[0]}(arr, axis={i[1]}))')