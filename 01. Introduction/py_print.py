#https://www.hackerrank.com/challenges/python-print

if __name__ == '__main__':
    n = int(input())
    i = 1
    number = 0
    
    while i <= n:
        exp_of_ten=0
        while i // 10**exp_of_ten != 0:
            exp_of_ten += 1
            
        number = number * 10**(exp_of_ten-1) + i * 10**(n-i)
        i += 1
    
    print(str(number))