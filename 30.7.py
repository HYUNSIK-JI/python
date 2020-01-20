korean,english,mathematics,science=map(int,input().split());
def get_score(*agrs):
	return min(agrs),max(agrs)
def get_average_score(**kwagrs):
	return sum(kwagrs.values())/len(kwagrs);

min_score,max_score=get_score(korean,english,mathematics,science);
average_score=get_average_score(korean=korean,english=english,mathematics=mathematics,science=science);

print('낮은점수:',min_score,'높은점수:',max_score,'평균점수:',average_score)

min_score,max_score=get_score(english,science);
average_score=get_average_score(english=english,science=science);

print('낮은점수:',min_score,'높은점수:',max_score,'평균점수:',average_score);