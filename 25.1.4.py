x={'a':10,'b':20,'c':30,'d':40};
x.pop('a');#삭제하면서 값을 반환
del x['b'];#삭제
x.popitem();# 파이썬 3.6버전이상은 맨 뒷값을 삭제 3.6이하 버전은 삭제가 랜덤. 
x.clear(); #딕셔너리의 모든 키-값 삭제하기
print(x);