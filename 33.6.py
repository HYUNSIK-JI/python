def countdown(n):
	total=n+1
	def down():
		nonlocal total
		total-=1
		return total
	return down
n=int(input())
c=countdown(n)
for i in range(n):
	print(c(),end=' ')