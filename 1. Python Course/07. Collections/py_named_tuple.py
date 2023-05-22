#https://www.hackerrank.com/challenges/py-collections-namedtuple

from collections import namedtuple
N = int(input())
stdnt = namedtuple('stdnt',input().split())
sum_grades = 0

for i in range(N):
    student_x = stdnt(*input().split())
    sum_grades += int(student_x.MARKS)
    
print(sum_grades / N)