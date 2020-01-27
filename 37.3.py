import math

class Point2D:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
p=[Point2D(),Point2D(),Point2D(),Point2D()]
p[0].x,p[0].y,p[1].x,p[1].y,p[2].x,p[2].y,p[3].x,p[3].y=map(int,input().split())

x=p[3].x-p[0].x
y=p[3].y-p[0].y
length=math.sqrt((x*x)+(y*y))
print(length)