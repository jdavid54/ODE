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

# function that returns dy/dt
def model(y,t):
    k = 0.3
    dydt = -k * y
    return dydt

def main():
    # initial condition
    y0 = 5

    # time points
    t = np.linspace(0,20)

    # solve ODE
    y = odeint(model,y0,t)

    # plot results
    plt.plot(t,y)
    plt.xlabel('time')
    plt.ylabel('y(t)')
    plt.show()

if __name__ == '__main__':
    main()
