#https://www.hackerrank.com/challenges/python-mutations

def mutate_string(string, position, character):
    str_list = list(string)
    str_list[position] = character
    new_string = ''.join(str_list)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)