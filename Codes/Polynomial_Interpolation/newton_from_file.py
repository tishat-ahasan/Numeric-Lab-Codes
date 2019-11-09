import numpy as np
def b(X, Y, r, l):
	if l==r:
		return Y[l]
	return ( b(X, Y, r, l+1) - b(X, Y, r-1, l) )/(X[r]-X[l])
	
X=[]
Y=[]

f = open('a.txt', 'r')
lines = f.readlines()
count = int(lines[0])
print(count)

for i in range(1, count+1):
	x_, y_ = (float(val) for val in lines[i].split())
	X.append(x_)
	Y.append(y_)
print(X)
print(Y)

def f(x):
	sum_ = 0.
	for i in range(len(X)):
		mul = b(X, Y, i, 0)
		for j in range(i):
			mul *= (x-X[j])
		sum_ += mul
	return sum_
	


#for i in range(len(X)):
#	print(b(X,Y,i,0))



import matplotlib.pyplot as plt
import numpy as np
x  = np.linspace(-10, 10, 200)
y = f(x)
plt.plot(x, y)
plt.plot(X, Y, 'o')
plt.show()