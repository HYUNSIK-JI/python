lines='Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive sytle and elegance. And this time everybody accepted his report.'
with open('words1.txt','w') as file:
	file.writelines(lines);
with open('words1.txt','r') as file:
	words1=file.read().split();
	for words1 in words1:
		if 'c' in words1:
			print(words1.strip(',.'));