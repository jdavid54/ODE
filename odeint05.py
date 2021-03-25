#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jean
#
# Created:     22/10/2017
# Copyright:   (c) Jean 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t):
    dxdt = 3.0 * np.exp(-t)
    dydt = -z[1] + 3
    dzdt = [dxdt,dydt]
    return dzdt


def main():
    # initial condition
    z0 = [0,0]

    # time points
    t = np.linspace(0,5)

    # solve ODE
    z = odeint(model,z0,t)
    print(z)

    # plot results
    plt.plot(t,z[:,0],'b-',label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
    plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=-y+3$')
    plt.ylabel('response')
    plt.xlabel('time')
    plt.legend(loc='best')
    plt.show()

if __name__ == '__main__':
    main()
