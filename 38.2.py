try:
	x=int(input('나눌 숫자를 입력하세요'))
	y=10/x
except ZeroDivisionError:
	print('0으로는 나눌수 없습니다')
else:
	print(y)