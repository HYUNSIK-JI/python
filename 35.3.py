class person:
	count=0

	def __init__(self):
		person.count += 1

	@classmethod
	def print_count(cls):
		print('{0}명 생성되었습니다.'.format(cls.count))

james=person()
maria=person()

person.print_count()