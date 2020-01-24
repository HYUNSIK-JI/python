class Annie:
	def __init__(self,health,mana,ap,skill):
		self.health=health
		self.mana=mana
		self.ap=ap
		self.__skill=skill
	def tibbers(self,ap):
		self.__skill=ap*0.65+400
		print('티버: 피해량 {0}'.format(self.__skill))
health,mana,ap=map(float,input().split())
power=Annie(health=health,mana=mana,ap=ap,skill=ap*0.65+400)
power.tibbers(ap);