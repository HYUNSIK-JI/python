start,stop=map(int,input().split());

i=start;
while True:
	if i==stop:
		break;
	if i%10!=3:
		print(i,end=' ');
		i=i+1;
		continue;
	i+=1;