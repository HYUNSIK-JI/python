class person:
	def greeting(self):
		print('안녕하세요')
class Student(person):
	def study(self):
		print('공부하기')
james=Student()
james.greeting()
james.study()