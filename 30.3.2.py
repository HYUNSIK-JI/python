def personal_info(**kwargs):
	for kw,agr in kwargs.items():
		print(kw,': ',agr,sep='');
personal_info(name='홍길동',age=30,address='서울시 괴산군')