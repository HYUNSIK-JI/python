import pickle

name='HYUNSIK'
age=26
address='서울시 강동구 천호동 올림픽로 56-14길 1층'
score={'korean':90,'english':95,'mathematic':85,'science':82}

with open('HYUNSIK.p','wb') as file:
	pickle.dump(name,file)
	pickle.dump(age,file)
	pickle.dump(address,file)
	pickle.dump(score,file)