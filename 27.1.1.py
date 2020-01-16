greet=['안녕하세요\n','파이썬\n','코딩 도장 입니다\n']

with open('hello.txt','w') as file:
	file.writelines(greet);