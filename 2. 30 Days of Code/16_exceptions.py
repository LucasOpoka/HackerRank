#https://www.hackerrank.com/challenges/30-exceptions-string-to-integer

try:
    print(int(input()))
except ValueError:
    print('Bad String')