#https://www.hackerrank.com/challenges/sparse-arrays

match_str = lambda x,y : [x.count(i) for i in y]

if __name__ == '__main__':
    str_lst = [input() for _ in range(int(input()))]
    queries = [input() for _ in range(int(input()))]
    print(*match_str(str_lst, queries), sep='\n')