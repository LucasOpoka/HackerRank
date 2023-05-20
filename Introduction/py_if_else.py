#https://www.hackerrank.com/challenges/py-if-else

if __name__ == '__main__':
    n = int(input().strip())
    weird = 'Weird'
    not_weird = 'Not Weird'
    
    if n % 2 != 0:
        print(weird)
    elif n % 2 == 0:
        if n >= 2 and n <= 5:
            print(not_weird)
        elif n >= 6 and n <= 20:
            print(weird)
        elif n > 20:
            print(not_weird)