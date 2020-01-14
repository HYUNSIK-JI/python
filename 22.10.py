a,b=map(int,input().split());
c=[2**i for i in range(a,b+1)];
del c[1];
del c[int(b)-3];
print(c);