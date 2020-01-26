class person:
	def greeting(self):
		print('안녕하세요.')
class university:
	def manage_credit(self):
		print('학점 관리')
class undergraudate(person,university):
	def study(self):
		print('공부하기')
james=undergraudate()
james.greeting()
james.manage_credit()
james.study()