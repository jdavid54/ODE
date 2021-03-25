import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# time points
nbx = 201
x = np.linspace(0,5,nbx)
y= 1-np.e**(-x)
#y= np.sin(x)
#y=x**2

# solve ODE
#y = odeint(model,y0,t)

# plot results
plt.plot(x,y)
#plt.xlabel('time')
#plt.ylabel('y(t)')
#plt.show()

# préparation du tableau qui va recevoir les valeurs
yp = np.zeros(nbx-1)

# calcul des valeurs de la dérivée
offset = 1.0
for i in range(nbx-1): 
    yp[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])

plt.plot(x, y, label="f(x)")
plt.plot(x[0:nbx-1], yp, label="f'(x)")

#dydt = -y + offset
y= -1+np.e**(-x) + offset
plt.plot(x, y, label="f'2(x)")
plt.grid(True)
plt.legend()
plt.show() 


