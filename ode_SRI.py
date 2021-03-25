import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
# days
ndays =100

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1., 0

# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 1.0/3.0, 1.0/10.0
r0=beta/gamma
print(beta,gamma)
print('R0=',r0)
# A grid of time points (in days)
t = np.linspace(0, ndays, ndays)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N 
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

print(S[-1],R[-1])
pic = max(I)
index= list(I).index(pic)
print (index, pic)

# IMax à revoir avec N
q = 1/r0
iMax = N/q*(1+np.log(q*S0/N))
print(q,iMax)

scale = 1000
# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, axisbelow=True)
#ax = fig.add_subplot(111, axis_bgcolor='#dddddd', axisbelow=True)
ax.plot(t, S/scale, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/scale, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/scale, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time in days')
ax.set_ylabel('Fraction of population')
#ax.set_ylim(0,1.2)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right'): #, 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.title('R0 ='+str(r0))
plt.show()