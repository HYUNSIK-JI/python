def find(word):
	result=False
	while True:
		line=(yield result)
		result=word in line
f=find('python')
next(f)

print(f.send('Hello,python!'))
print(f.send('Hello,World!'))
print(f.send('python Script'))

f.close()