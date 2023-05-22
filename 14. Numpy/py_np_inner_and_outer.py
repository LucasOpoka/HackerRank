#https://www.hackerrank.com/challenges/np-inner-and-outer

import numpy as np
lst = [np.array(input().split(), int) for _ in range(2)]
print(np.inner(*lst), np.outer(*lst), sep='\n')