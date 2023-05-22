#https://www.hackerrank.com/challenges/30-recursion

def factorial(n):
    if n-1 >= 1:
        return n*factorial(n-1)
    else:
        return n

if __name__ == '__main__':
    n = int(input().strip())
    result = factorial(n)
    print(result)