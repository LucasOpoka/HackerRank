#https://www.hackerrank.com/challenges/crush

def arrayManipulation(n, queries):
    dict = {}
    for strt, stop, val in queries:
        dict[strt-1] = dict.get(strt-1, 0) + val
        dict[stop] = dict.get(stop, 0) - val

    mx, current_val = 0, 0
    for i in sorted(dict.keys()):
        current_val += dict[i]
        mx = max(mx,current_val)

    return mx

if __name__ == '__main__':
    n,m = map(int, input().split())
    qr = [list(map(int, input().split())) for _ in range(m)]
    print(arrayManipulation(n, qr))