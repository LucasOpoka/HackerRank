#https://www.hackerrank.com/challenges/validating-uid

from re import fullmatch as fm
for _ in range(int(input())):
    c = fm(r'(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[^\W_]{10}', s:=input())
    r = fm(r'(?:([^\W_])(?!.*\1))*', s)
    print('Valid') if None not in (c, r) else print('Invalid')