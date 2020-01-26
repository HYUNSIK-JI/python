class person:
	def greeting(self):
		print('안녕하세요.')
class personlist:
	def __init__(self):
		self.person.list=[]
	def append_person(self,person):
		self.person.list.append(person);
