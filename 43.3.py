import re
m=re.match('([0-9]+) ([0-9]+)','10 295')
print(m.group(1))
print(m.group(2))
print(m.group())
print(m.group(0))