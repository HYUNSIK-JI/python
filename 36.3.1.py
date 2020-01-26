class person:
	def __init__(self):
		print('person __init__')
		self.hello='안녕하세요.'
class student(person):
	def __init__(self):
		print('student__init__')
		super().__init__()
		self.school='파이썬 코딩 도장'
james=student()
print(james.school)
print(james.hello)