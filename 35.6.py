class Time:
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	@classmethod
	def from_string(cls):
		hour,minute,second=map(int,input().split(':'));
		a=cls(hour,minute,second)
		return a
	@staticmethod
	def is_time_vaild(time_string):
		hour,minute,second=map(int,input().split(':'));
		return 0<=hour<=24 and 0<=minute<=59 and 0<=second<=60

if Time.is_time_vaild('20:22:24'):
	t=Time.from_string()
	print(t.hour,t.minute,t.second)
else:
	print('잘못된 형식입니다.')