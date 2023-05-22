from math import gcd
from functools import reduce

x = [[1,2],[3,4],[10,6]]

def product(fracs):
    func = lambda x, y : [x[0]*y[0], x[1]*y[1]]
    frc = reduce(func, fracs)
    frc_gcd = gcd(*frc)
    rslt = [int(i/frc_gcd) for i in frc]
    print(*rslt)
    
product(x)