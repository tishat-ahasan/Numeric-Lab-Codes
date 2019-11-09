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


points = [
	[1., 1.],
	[-5., 5.],
	[-4.9, 10],
	[3.0, 2.],
	[2., 2.1],
	[5., 5.],
	[-3., -3.],
	[-2., 4.]
	]

x = linspace(-5., 5., 200)
y = f(points, x)

plt.plot(x, y)
for i in range(len(points)):
	plt.plot(points[i][0], points[i][1], 'o')
plt.show()