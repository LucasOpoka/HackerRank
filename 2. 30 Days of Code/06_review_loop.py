#https://www.hackerrank.com/challenges/30-review-loop

for _ in range(int(input())):
    s = input()
    print(f'{s[::2]} {s[1::2]}')