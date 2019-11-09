import numpy as np
def b(X, Y, r, l):
	if l==r:
		return Y[l]
	return ( b(X, Y, r, l+1) - b(X, Y, r-1, l) )/(X[r]-X[l])
	
X=[5, 7, 11, 13, 17]
Y=[150, 392, 1452, 2366, 5202]

def f(x):
	sum_ = 0.
	for i in range(len(X)):
		print(i)
		mul = b(X, Y, i, 0)
		for j in range(i):
			mul *= (x-X[j])
		sum_ += mul
	return sum_
	


for i in range(len(X)):
	print(b(X,Y,i,0))

print(f(9))


import matplotlib.pyplot as plt
import numpy as np
x  = np.linspace(1, 20)
y = f(x)
plt.plot(x, y)
plt.plot(X, Y, 'o')
plt.show()