#https://www.hackerrank.com/challenges/reduce-function

from fractions import Fraction
from functools import reduce

def product(fracs):
    func = lambda x,y : Fraction(x.numerator*y.numerator, x.denominator*y.denominator)
    t = reduce(func, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)