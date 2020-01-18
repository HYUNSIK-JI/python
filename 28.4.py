words=['apache\n','decal\n','did\n','neep\n','noon\n','refer\n','river\n'];
with open('words2.txt','w') as file:
	file.writelines(words);
with open('words2.txt','r') as file:
	words1=file.readlines()
	for words1 in words1:
		if '\n' in words1:
			words2=list(words1.strip('\n'));
			words3=list((reversed(words2)));
			if words2==words3:
				print(words2);