class Trace:
	def __init__(self,func):
		self.func=func

	def __call__(self):
		print(self.func.__name__,'함수시작')
		print.func()
		print(self.func.__name__,'함수 끝')
@Trace
def hello():
	print('hello')

hello()