maria={'korean':94,'english':91,'mathematics':89,'science':83};
size=len(maria.keys());
total=0;
for value in maria.values():
	total+=value;
average=(total/size);
print('평균:%0.2f' %average);