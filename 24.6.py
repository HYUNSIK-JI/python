price = list(map(int, input().split(';')))
price.sort(reverse=True)
for i in price:
	print('%9s' % format(i, ','))