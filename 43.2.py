import re
print(re.match('[0-9]*','1234'))
print(re.match('[0-9]+','1234'))
print(re.match('[0-9]+','abcd'))

print(re.match('a*b','b'))
print(re.match('a+b','b'))
print(re.match('a*b','aab'))
print(re.match('a+b','aab'))