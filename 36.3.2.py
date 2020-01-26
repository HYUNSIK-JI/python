class person:
	def __init__(self):
		print('person__init__')
		self.hello='안녕하세요'
class student(person):
	pass
james=student()
print(james.hello)