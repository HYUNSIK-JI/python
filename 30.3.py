def personal_info(name,age,address):
	print('이름:',name);
	print('나이:',age);
	print('주소:',address);
x={'name':'홍길동','age':30,'address':'충청북도 괴산군 괴산읍'}
personal_info(**x);