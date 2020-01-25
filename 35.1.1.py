class person:
	bag=[]

	def put_bag(self,stuff):
		self.bag.append(stuff)
james=person()
james.put_bag('책')

maria=person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)