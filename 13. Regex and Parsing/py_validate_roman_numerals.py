#https://www.hackerrank.com/challenges/validate-a-roman-number

regex_pattern = r"^C?M{,3}(CM|C)?D{,3}X?C{,3}X?L?I?X{,3}I?V?I{,3}$"

import re
print(str(bool(re.match(regex_pattern, input()))))