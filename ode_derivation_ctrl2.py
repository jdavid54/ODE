import numpy as np
import matplotlib.pyplot as plt

nbx = 101
x = np.linspace(0, 10, nbx)
y = np.cos(x)

# préparation du tableau qui va recevoir les valeurs
yp = np.zeros(nbx-1)

# calcul des valeurs de la dérivée
for i in range(nbx-1): 
    yp[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])

plt.plot(x, y, label="f(x)")
plt.plot(x[0:nbx-1], yp, label="f'(x)")

plt.legend()
plt.show() 
