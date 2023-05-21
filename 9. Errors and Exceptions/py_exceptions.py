#https://www.hackerrank.com/challenges/exceptions

n = int(input())

for _ in range(n):
    a, b = input().split()
    try:
        print(int(int(a) / int(b)))
    except ZeroDivisionError as z:
        print('Error Code: integer division or modulo by zero')
    except ValueError as v:
        print(f'Error Code: {v}')