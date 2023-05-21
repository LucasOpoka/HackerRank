#https://www.hackerrank.com/challenges/py-set-add

if __name__ == '__main__':
    n = int(input())
    i = 0
    dstnct_cntries = set()
    
    while i < n:
        cntry = input()
        dstnct_cntries.add(cntry)
        i += 1
        
    print(len(dstnct_cntries))