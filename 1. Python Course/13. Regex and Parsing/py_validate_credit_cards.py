#https://www.hackerrank.com/challenges/validating-credit-card-number

from re import fullmatch as fm
for _ in range(int(input())):
    c = fm(r'(?=[456])(?!.*(\d)(-?\1){3,})(\d{4}-?){4}', s:=input())
    print('Valid') if c is not None else print('Invalid')