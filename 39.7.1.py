class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __getitem__(self, index):
        if index<self.stop-self.start:
            a=(((self.start+index)//60)//60)%24 #시간
            b=((self.start+index)//60)%60
            c=(self.start+index)%60
            return '{0:02d}:{1:02d}:{2:02d}'.format(a,b,c)
        else:
            raise IndexError
start,stop,index=map(int, input().split())
for i in TimeIterator(start, stop):
    print(i)
print('\n', TimeIterator(start, stop)[index], sep='')