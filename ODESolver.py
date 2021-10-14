# this program requires 3 inputs-->1)model-the definition of the function that will give us the derivatives
#  2)initial conditions
# 3)time range
# sample basic eqn=> dy/dt=-ky(t); where y is the aforementioned 'model'

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# defining the model or the function
def model(y,t):
    k = 0.3
    dy_dt = -k * y
    return dy_dt


# defining the initial cond.s
y0 = 5


# creating time range
t = np.linspace(0, 20,5)  # linspave gives us evenly spaced numbers and a default amount of 50 numbers(can change)
print(t)
# solving
y = odeint(model,y0, t)  # thats just how odeint package works

# plotting
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
