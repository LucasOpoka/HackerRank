#https://www.hackerrank.com/challenges/re-group-groups

import re
try: print(re.search(r'([^\W_])\1+',input()).group(1))
except AttributeError: print(-1)
