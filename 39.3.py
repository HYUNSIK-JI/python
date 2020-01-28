class counter:
	def __init__(self,stop):
		self.stop=stop
	def __getitem__(self,index):
		if index<self.stop:
			return index
		else:
			raise IndexError
print(counter(3)[0],counter(3)[1],counter(3)[2])

for i in counter(3):
	print(i,end=' ')