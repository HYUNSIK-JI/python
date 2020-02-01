import re
print(re.search('^Hello','Hello,world!'))
print(re.search('world!$','Hello,world!'))
print(re.match('hello|world','hello'))