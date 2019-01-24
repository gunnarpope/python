# Use Runga-Kutta 45 to numerically solve the differential equation of the voltage discharge from a simple RC circuit
# by gunnar pope
# 01/24/19
# Usage: $ python RK4.py

# see https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

from scipy.integrate import solve_ivp

R = 1e6 #Ohms
C = 1e-6 #Farads

# dV/dt = -1/(R*C)*Vc
def f(t,y):
    dydt = -1.0/(R*C)*y
    return dydt 

# solve_ivp(fun, t_span, y0, method='RK45', t_eval=None, dense_output=False, events=None, vectorized=False, **options)
t_start = 0
t_end   = 10

# initial conditions (this could be a vector too [a, b, c, etc]
ics = [2] #volts


sol = solve_ivp(f, [t_start,t_end],ics, method='RK45')
print(sol.t)
print()
print(sol.y)

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(t_start,t_end,100)
vout = ics*np.exp(-1/(R*C)*t)

plt.plot(t,vout, label='exact solution')


plt.plot(sol.t, sol.y[0], label='RK4 Solution')
plt.title("A Numerical Methods Example Using RK4 In Python")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (v)")
plt.grid(True)
plt.legend()
plt.show()
