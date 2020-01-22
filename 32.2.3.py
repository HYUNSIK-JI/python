def f(x):
	return x>5 and x<10
a=[8,2,3,10,15,7,1,9,0,11]
b=list(filter(f,a));
print(b)
c=list(filter(lambda x:x>5 and x<10,a))
print(c);