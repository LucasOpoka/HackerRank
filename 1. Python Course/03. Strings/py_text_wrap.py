#https://www.hackerrank.com/challenges/text-wrap

def wrap(string, max_width):
    indx_strt, indx_end = 0, max_width
    new_string = str()

    for i in range(len(string) // max_width):
        new_string += string[indx_strt:indx_end] + '\n'
        indx_strt, indx_end = indx_end, indx_end + max_width
    
    if indx_strt < len(string):
        new_string += string[indx_strt:] + '\n'
    
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)