import re
print(re.sub('apple|orange','fruit','apple box orange tree'))
print(re.sub('[0-9]+','n','1 2 Fizz 4 Buzz Fizz 7 8'))

def multiple10(m):
	n=int(m.group())
	return str(n*10)
print(re.sub('[0-9]+',multiple10,'1 2 Fizz 4 Buzz Fizz 7 8'))