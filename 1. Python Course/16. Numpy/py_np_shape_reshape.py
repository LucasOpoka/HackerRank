#https://www.hackerrank.com/challenges/np-shape-reshape

import numpy as np
print(np.reshape(list(map(int, input().split())), (3,3)))