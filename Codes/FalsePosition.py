#finding the root of x^2-x-2 in
# the rang of 1<x<3 using
#false Position Method.
import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return x**2-x-2

x = np.linspace(-5,5,100)
y = f(x)


#plt.plot((-10,10), (0, 0), 'r--')

#we use 100 iteration

x1,x2 = -0.5,3
for i in range(0,10):
    x0 = x1 - f(x1)*((x2-x1)/(f(x2)-f(x1)))
    plt.plot((x1, x1), (0, f(x1)))
    plt.plot((x2, x2), (0, f(x2)))
    plt.plot((x1,x2),(f(x1),f(x2)))
    if f(x0)*f(x1)<0:
        x2 = x0
    else:
        x1 = x0

    plt.plot((-10, 10), (0, 0), 'r--')
    plt.plot((0, 0),(-10, 10) ,'r--')
    plt.plot((x0, x0), (0, f(x0)))

    plt.plot(x, y)
    plt.ylim(-5, 10)
    plt.show()



print(x1)