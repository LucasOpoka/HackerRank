#https://www.hackerrank.com/challenges/re-findall-re-finditer

import re
v, c = '[aeiou]', '[qwrtypsdfghjklzxcvbnm]'
pt = '(?<=' + c +')' + v + '{2,}(?=' + c + ')'
lst = [i.group() for i in re.finditer(pt, input(), flags=re.I)]
print(*lst, sep='\n') if len(lst)>0 else print(-1)