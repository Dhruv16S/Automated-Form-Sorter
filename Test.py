

# import re
# string = '''
# Mr. Schafer
# Mrs. robinson
# Mr Smith
# Mrs Smith
# Ms Davis
# '''
# print(re.findall(r'Mr?s?\.?[A-Z][a-zA-Z]+',string))

import re
str1 = '''demonetization zuz craze zebra zaz bizua chip'''
# str1 = " zaz "
res = re.findall(r"[^Zz]\w+[Zz]+\w+[^Zz]",str1)
print(res)