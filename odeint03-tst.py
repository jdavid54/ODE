import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



# time points
nbx = 101
x = np.linspace(-5,5,nbx)
y= np.e**(-x)
#y= np.sin(x)
#y=x**2

# solve ODE
#y = odeint(model,y0,t)

# plot results
plt.plot(x,y)
#plt.xlabel('time')
#plt.ylabel('y(t)')
#plt.show()

# préparation des tableaux qui vont recevoir les valeurs
xnew = np.zeros(nbx-1)
yp = np.zeros(nbx-1)

# calcul des abscisses et des valeurs de la dérivée
for i in range(nbx-1): 
    xnew[i] = (x[i] + x[i+1]) / 2
    yp[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])

plt.plot(x, y, label="f(x)")
plt.plot(xnew, yp, label="f'(x)")

plt.legend()
plt.show() 


