#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter

import string as s
l,n,a = s.ascii_letters, s.digits, '_-'
lna, ln = l+n+a, l+n

def fun(s):
    x = s.partition('@')
    y = x[2].partition('.')
    cnd1 = all(i in lna for i in x[0]) and (x[1] == '@')
    cnd2 = all(i in ln for i in y[0]) and y[1] == '.'
    cnd3 = all(i in l for i in y[2]) and len(y[2]) <= 3
    cnd4 = len(x[0]) > 0 and len(y[0]) > 0
    
    return all([cnd1,cnd2,cnd3,cnd4])

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)