import math
def prime_number(a,b):
	for i in range(a,b+1,1):
		n=2
		while n<=b:
			if i%i==0 and i//i==1:
				if i%n==0 and i==n:
					yield i
			n=n+1
a,b=map(int,input().split())
g=prime_number(a,b)
print(type(g))
for i in g:
	print(i,end=' ')