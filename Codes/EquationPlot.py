import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (-x**2+x+1)/x

X = np.linspace(-10,10,100)
Y = f(X)
plt.plot(X,Y)

plt.plot((0, 0), (min(Y)-2, max(Y)+2), 'r--')

plt.plot((-10,10), (0, 0), 'r--')
print(Y)

plt.show()
