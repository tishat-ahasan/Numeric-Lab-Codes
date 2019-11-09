import numpy as np
x = [4., 9., 16.]
f = [2., 3., 4.]
x = [0., 1., 2., 3.]
f = [1., -1., -1., 0.]
x = [1., 3., 4., 7., 11., 13.]
f = [4., 9., 29., 39., 70., 85.]
x = []
f = []


fil = open('a.txt', 'r')
lines = fil.readlines()
count = int(lines[0])
print(count)

for i in range(1, count+1):
	x_, f_ = (float(val) for val in lines[i].split())
	x.append(x_)
	f.append(f_)


n = len(x) - 1
h = [0.]
for i in range(1, n+1):
    h.append(x[i]-x[i-1])
A = np.zeros((n+1,n+1))
B = np.zeros((n+1, 1))
for i in range(0, n+1):
    if i == 0:
        A[i][i] = 1.
    elif i == n:
        A[i][i] = 1.
    else:
        A[i][i] = 2.*(h[i] + h[i+1])
        A[i][i-1] = h[i]
        A[i][i+1] = h[i+1]

for i in range(0, n+1):
    if i == 0:
        B[i][0] = 0
    elif i == n:
        B[i][0] = 0
    else:
        B[i][0] = 6.*(
            (f[i+1]-f[i])/h[i+1] - (f[i]-f[i-1])/h[i]
        )
print(A)
print(B)
RES = np.matmul(np.linalg.inv(A), B)
print(RES)

Co = np.zeros((n,4))
for i in range(0, n):
	Co[i][0] = (RES[i+1][0] - RES[i][0]) / (6.*h[i+1])
	Co[i][1] = RES[i][0]/2.
	Co[i][2] = (f[i+1]-f[i])/h[i+1] - ((2.*h[i+1]*RES[i][0] + h[i+1]*RES[i+1][0]))/6.
	Co[i][3] = f[i]
print(Co)

import matplotlib.pyplot as plt
for i in range(n):
    X = np.linspace(x[i],x[i+1])
    Y = Co[i][3] + Co[i][2]*(X-x[i]) + Co[i][1]*(X-x[i])**2 + Co[i][0]*(X-x[i])**3
    plt.plot(X,Y)

X = 1.

Y = Co[0][3] + Co[0][2]*(X-x[0]) + Co[0][1]*(X-x[0])**2 + Co[0][0]*(X-x[0])**3
print(Y)
#print(Co[0][3])
plt.scatter(x,f)
plt.plot(X,Y)
plt.show()