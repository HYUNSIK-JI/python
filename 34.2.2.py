class person:
	def __init__(self,name,age,address):
		self.hello='안녕하세요.'
		self.name='지현식'
		self.age=26
		self.address=address
	def greeting(self):
		print('{0} 저는 {1}입니다 나이는 {2}입니다.'.format(self.hello,self.name,self.age))
maria=person('지현식',26,'서울시 천호동')
maria.greeting()

print('이름:',maria.name)
print('나이:',maria.age)
print('주소:',maria.address)