a=int(input());
b=int(input());
a={i for i in range(1,a+1) if a%i==0};
b={i for i in range(1,b+1) if b%i==0};

e=set.intersection(a,b);
total=0;
for i in e:
	total+=i;
print(total);