a[5][5]={};
d=1;
for(i=0; i<5; i++)
{
	for(j=0; j<5; j++)
	{
		a[i][j]=d;
		d++;
		}
	}
}

for(i=0; i<5; i++){
	for(j=0; j<5; j++){
		print('a[i][j]:',%d);
	}
}
