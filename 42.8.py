def html_tag(x):
	def real_decorator(func):
		def wrapper():
			r=func()
			print('<{0}><{1}>{2}</{1}></{0}>.'.format(a,b,r))
			return r
		return wrapper
	return real_decorator
a,b=input().split()
@html_tag(a)
@html_tag(b)
def hello():
	return 'Hello,world!'
print(hello())