#https://www.hackerrank.com/challenges/most-commons

from collections import Counter
[print(*i) for i in Counter(sorted(input())).most_common(3)]