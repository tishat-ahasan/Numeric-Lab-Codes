import random as rn
def f(points, x):
	res = 0.
	for i in range(len(points)):
		
		pro = 1.0
		for j in range(len(points)):
			if i != j:
				pro = pro * (x - points[j][0])/(points[i][0]-points[j][0])
		res = res + pro*points[i][1]
	
	
	
	return res
	



from numpy import *
import matplotlib.pyplot as plt


points = []

fil = open('a.txt', 'r')
lines = fil.readlines()
count = int(lines[0])
print(count)

for i in range(1, count+1):
	x_, y_ = (float(val) for val in lines[i].split())
	tmp = []
	tmp.append(x_)
	tmp.append(y_)
	points.append(tmp)
	print(points)


x = linspace(-10., 10., 200)
y = f(points, x)

plt.plot(x, y)
for i in range(len(points)):
	plt.plot(points[i][0], points[i][1], 'o')
plt.show()