korean,english,mathematics,science=map(int,input().split());
def get_score(*agrs):
	average=((korean+english+mathematics+science)/4);
	return min(agrs),max(agrs),average
min_score,max_score,average_score=get_score(korean,english,mathematics,science);

print('낮은점수:',min_score,'높은점수:',max_score,'평균점수:',average_score)