#https://www.hackerrank.com/challenges/30-binary-numbers
#Out of curiosity I implemented my own way to convert decimal numbers to binary.
#Then I solved the rest of the problem with regular expressions.

import re
def DecToBin(n):
    binary = []
    while n >= 1:
        n, r = divmod(n, 2)
        binary.append(str(r))
    return ''.join(binary[::-1])

if __name__ == '__main__':
    n = int(input().strip())
    print(len(max(re.findall('(1+)', DecToBin(n)))))