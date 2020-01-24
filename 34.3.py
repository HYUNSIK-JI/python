class person:
	def __init__(self,name,age,address,wallet):
		self.hello='안녕하세요'
		self.name=name
		self.age=26
		self.address=address
		self.__wallet=wallet
	def pay(self,amount):
		self.__wallet-=amount
		print('이제 {0}원 남았네요'.format(self.__wallet))
maria=person('지현식',26,'서울시 강동구',10000)
maria.pay(3000)