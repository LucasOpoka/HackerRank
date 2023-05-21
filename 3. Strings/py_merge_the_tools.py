#https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string, k):
    substr_n = int(len(string)/k)

    for i in range(substr_n):
        substr = list(string[i*k : (i+1)*k])
        substr_nd = []
        [substr_nd.append(c) for c in substr if c not in substr_nd]
        print(''.join(substr_nd))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)