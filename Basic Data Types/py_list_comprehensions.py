#https://www.hackerrank.com/challenges/list-comprehensions

if __name__ == '__main__':
    x, y, z, n = int(input()), int(input()), int(input()), int(input())
    
    lst = [[i,j,k] for i in range(x+1) for j in range(y+1)for k in range(z+1) if sum([i,j,k]) != n]

    print(lst)