#https://www.hackerrank.com/challenges/find-a-string

def count_substring(string, sub_string):
    i = 0
    count = 0

    while i < len(string):
        if string[i:].find(sub_string) >= 0:
            i += string[i:].find(sub_string) + 1
            count += 1
        else:
            i += 1
    
    return(str(count))

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)