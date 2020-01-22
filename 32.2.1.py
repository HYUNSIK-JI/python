def f(x):
	if x==1:
		return str(x)
	if x==2:
		return float(x)
	else:
		return x+10
a=[1,2,3,4,5,6,7,8,9,10]
d=list(map(f,a));
b=list(map(lambda x:str(x) if x%3==0 else x,a))
c=list(map(lambda x:str(x) if x==1 else float(x) if x==2 else x+10,a))
print(b)
print(c)
print(d)
