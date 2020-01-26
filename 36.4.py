class person:
	def greeting(self):
		print('안녕하세요')
class student(person):
	def greeting(self):
		print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
james=student()
james.greeting()