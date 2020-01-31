class Multiple:
	def __init__(self,x):
		self.x=x
	def __call__(self,func):
		def wrapper(a,b):
			r=func(a,b)
			if r%3==0:
				print('{0}의 반환값은 {1}의 배수 입니다.'.format(func.__name__,self.x))
			else:
				print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__,self.x))
			return r
		return wrapper
@Multiple(3)
def add(a,b):
	return a+b
print(add(10,20))
print(add(a=2,b=5))