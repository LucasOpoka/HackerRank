#https://www.hackerrank.com/challenges/map-and-lambda-expression

cube = lambda x: x**3 

def fibonacci(n):
    lst = [0,1,1]
    while len(lst) < n:
        lst.append(lst[-1]+lst[-2])
    return lst[:n] if n < 3 else lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))