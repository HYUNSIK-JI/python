import re
print(re.match('h{3}','hhhello'))
print(re.match('(hello){3}','hellohellohelloworld'))

print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1000-1000'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}','010-1000-100'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}','02-100-1000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}','02-10-1000'))