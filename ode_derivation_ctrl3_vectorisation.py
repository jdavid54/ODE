import numpy as np
import matplotlib.pyplot as plt

#https://courspython.com/derivee-fonction.html

nbx = 101
x = np.linspace(0, 10, nbx)
y = np.cos(x)

# calcul des abscisses et des valeurs de la dérivée
xnew = (x[:-1] + x[1:]) / 2
yp = (y[1:] - y[:-1]) / (x[1:] - x[:-1])

plt.plot(x, y, label="f(x)")
plt.plot(xnew, yp, label="f'(x)")

plt.legend()
plt.show()

# calcul des valeurs de la dérivée
#sans xnew
yp = (y[1:] - y[:-1]) / (x[1:] - x[:-1])

plt.plot(x, y, label="f(x)")
plt.plot(x[:-1], yp, label="f'(x)")

plt.legend()
plt.show()
