price = list(map(int, input().split(';')))
price.sort(reverse=True)

result=[];

for i in price:
	result.append('%9s' %format(i,','));
print(result);