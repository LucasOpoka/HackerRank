#https://www.hackerrank.com/challenges/python-lists

if __name__ == '__main__':
    N = int(input())
    i = 0
    lst = []
    
    while i < N:
        cmnd = input().split()
        
        if len(cmnd) == 3:
            exec(f'lst.insert({cmnd[1]},{int(cmnd[2])})')
        elif len(cmnd) == 2:
            exec(f'lst.{cmnd[0]}({int(cmnd[1])})')
        elif cmnd[0] in ['reverse','pop','sort']:
            exec(f'lst.{cmnd[0]}()')
        else:
            print(lst)
               
        i += 1