from abc import *

class studentBase():
	@abstractmethod
	def study(self):
		pass

	@abstractmethod
	def go_to_school(self):
		pass

class student(studentBase):
	def study(self):
		print('공부하기')

	def go_to_school(self):
		print('학교가기')

james=student()
james.study()
james.go_to_school()