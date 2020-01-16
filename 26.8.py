a={i for i in range(0,101,1) if i%3==0};
b={i for i in range(0,101,1) if i%5==0};
c=a&b;
print(a&b);
print(a.intersection(b));
print(c);