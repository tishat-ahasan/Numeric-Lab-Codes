#finding the root of x^2-4x-10=0 in
# the rang of 1<x<3 using
#false Position Method.
import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return x**2-4*x-10

x = np.linspace(-5,10,100)
y = f(x)


#plt.plot((-10,10), (0, 0), 'r--')

#we use 100 iteration

x1,x2 = 4,2  #initial estimation
for i in range(0,10):
    x3 = ((f(x2)*x1) - (f(x1)*x2))/(f(x2)-f(x1))
    plt.plot((x1, x1), (0, f(x1)),label='point X1')
    plt.plot((x2, x2), (0, f(x2)),label='point X2')
    #plt.plot((x1,x2),(f(x1),f(x2)))
    x1 = x2
    x2 = x3

    plt.plot((-10, 10), (0, 0), 'r--')
    plt.plot((0, 0), (min(y)-2, max(y)+2), 'r--')
    plt.plot((x3, x3), (0, f(x3)),label='point X3')

    plt.plot(x, y,label='x^2-4x-10=0')
    #plt.ylim(-5, 10)
    plt.legend()
    plt.show()



print(x1)