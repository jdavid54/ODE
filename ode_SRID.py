import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 6e7
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0, D0 = 40000, 7200, 2600   #D0 initial number of deads 
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0 - D0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma, omega = 0.3, 7/40, 2.6/40
R0=beta/(gamma+omega)
print(beta,gamma)
print('R0=',R0)
# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma, omega):
    S, I, R, D = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I - omega * I
    dDdt = omega * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt, dDdt

# Initial conditions vector
y0 = S0, I0, R0, D0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, omega))
S, I, R, D = ret.T

print(R[-1]/1e6,D[-1]/1e6)
pic = max(I)
index= list(I).index(pic)
print (index, pic)
q = 1/R0
iMax = 1/q*(1+np.log(q*S0))
print(q,iMax)

scale = 1
# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
#ax = fig.add_subplot(111, axis_bgcolor='#dddddd', axisbelow=True)
ax.plot(t, S/scale, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/scale, 'r', alpha=0.5, lw=3, label='Infected')
ax.plot(t, R/scale, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t, D/scale, 'y', alpha=0.5, lw=3, label='Deads')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number')
ax.set_ylim(0,N/scale)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()

