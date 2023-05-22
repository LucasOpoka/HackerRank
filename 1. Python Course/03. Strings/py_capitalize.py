#https://www.hackerrank.com/challenges/capitalize

def solve(s):
    s = list(s)
    i = 0

    s[0] = s[0].capitalize()
    while i < len(s):
        if s[i - 1] == ' ':
            s[i] = s[i].capitalize()
        i += 1
        
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
