class advancedList(list):
	def replace(self,old,new):
		while old in self:
			self[self.index(old)]=new
x=advancedList([1,2,3,1,2,3,1,2,3])
x.replace(1,100)
print(x)