## Make your plots pretty in python

    $ python pretty_colors_plt.py
![coolwarm](pretty_colors_plt.png)

## Solving initial valued problems of ordinary differential equations (ODE's)
Apply Runge-Kutta 45 (RK45) to solve the differential equation for a RC voltage decay off a capacitor discharging through a resistor.

The voltage decay of a simple RC network is modeled in the time domain as:

    V(t) = Vo*e^(t/(RC))

where R is the resistance in Ohms and C is the capacitance in Farads and t is in units of time.

The time-domain solution shown above is the solution to the following equation that governs the RC circuit behavior.

    V'(t) = - 1/RC*V

where V'(t) is the derivative of voltage, V, over time. This is an ordinary differential equation which can be solved using numerical methods. In this example, we will use the Runge-Kutta method to numerically solve the ODE.

 Use Runge-Kutta 45 to numerically solve the differential equation of the voltage discharge from a simple RC circuit

```Python    
# RK4.py
# by gunnar pope
# 01/24/19
# Usage: $ python RK4.py

# references: https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html

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

# apply RK45 to numerically solve the differential equation, given the initial conditions and time span.
sol = solve_ivp(f, [t_start,t_end],ics, method='RK45')
print(sol.t)
print()
print(sol.y)

import matplotlib.pyplot as plt
import numpy as np

# compare the numerical solution to the solution in the time-domain.
t = np.linspace(t_start,t_end,100)
vout = ics*np.exp(-1/(R*C)*t)

plt.plot(t,vout, label='Exact Solution')
plt.plot(sol.t, sol.y[0], label='RK4 Solution')
plt.title("A Numerical Methods Example Using RK4 In Python")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (v)")
plt.grid(True)
plt.legend()
plt.show()

```

Usage:

    $ python RK4.py

![ode-solution](ode-solution.png)
