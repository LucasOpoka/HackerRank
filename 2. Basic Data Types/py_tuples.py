#https://www.hackerrank.com/challenges/python-tuples
#Run in PyPy3 to get the solution accepted!

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    
    print(hash(t))