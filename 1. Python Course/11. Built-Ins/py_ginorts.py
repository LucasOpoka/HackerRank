#https://www.hackerrank.com/challenges/ginorts

s = list(input())
s.sort(key = lambda x:(x in '02468', x.isdigit(), x.isupper(), x.islower(), x))
print(*s, sep='')