#https://www.hackerrank.com/challenges/grading

#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            pass
        elif (rnd:=((grades[i] // 5 + 1) * 5)) - grades[i] < 3:
            grades[i] = rnd
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()