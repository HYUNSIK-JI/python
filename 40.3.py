def number_generation():
	x=[1,2,3]
	yield from x
for i in number_generation():
	print(i)