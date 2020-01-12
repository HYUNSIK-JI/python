x=int(input());
for i in range(0,x,1):
	for j in range(0,x*2-1,1):
			if j==int((0+x*2-1)/2)-i:
				for k in range(j-i,j+i+1,1):
						print('*',end='');
			else:
				print(' ',end='')