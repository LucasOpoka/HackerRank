#https://www.hackerrank.com/challenges/validating-named-email-addresses

from re import fullmatch as fm
for _ in range(int(input())):
    if not fm(r'[^\W\d_]+ <[^\W\d_][\w._-]*@[^\W\d_]+\.[^\W\d_]{1,3}>', s:=input()) is None:
        print(s)