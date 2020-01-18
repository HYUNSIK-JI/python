import pickle

with open('HYUNSIK.p','rb')as file:
	name=pickle.load(file);
	age=pickle.load(file);
	address=pickle.load(file);
	score=pickle.load(file);
	print(name);
	print(age);
	print(address);
	print(score);