#https://www.hackerrank.com/challenges/no-idea

if __name__ == '__main__':
    
    nm = [int(i) for i in input().split()]
    array = [int(i) for i in input().split()]
    setA = set([int(i) for i in input().split()])
    setB = set([int(i) for i in input().split()])
    happy = 0
    
    for i in array:
        if i in setA:
            happy += 1
        if i in setB:
            happy -= 1
            
    print(str(happy))