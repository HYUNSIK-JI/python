x=10 #전역 변수
def foo():
	global x #전역 변수 x를 사용하겟다고 설정
	x=20 #전역 변수
	print(x)#전역 변수 출력
foo()
print(x)# 전역 변수 출력