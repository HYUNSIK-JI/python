with open('words.txt','r') as file:
	count=0;
	words=file.readlines();
	for words in words:
		if len(words.strip('\n'))<=10:
			count+=1;
			print(words);
print(count);