import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

y0 = 0
y1 = 2

def fungsi(x,r):
    y,z = r
    dy_dx = z
    #y'' - 3x = 0, y(0)=0 , y(1)=1
    dz_dx = 3*x
    return dy_dx, dz_dx

tebak = 0.5

t = np.linspace(0,y1,25)
solv = solve_ivp(fungsi, (0,y1), (y0,tebak), t_eval=t)
y,z = solv.y

plt.plot(t,y,"-")
plt.grid()
plt.show
