import numpy as np
import time
import matplotlib.pyplot as plt
from solve_PRmodel import solve_PRmodel

start_time = time.time()

t_dur = 10e3         # [ms]
g_c = 10.5          # [mS cm**-2]
I_stim = 0.78       # [uA cm**-2]
stim_start = 0      # [ms]
stim_end = t_dur    # [ms]

sol = solve_PRmodel(t_dur, g_c, I_stim, stim_start, stim_end)

Vs, Vd, n, h, s, c, q, Ca = sol.y
t = sol.t


f1 = plt.figure(1)
plt.plot(t*1e-3, Vs, '-', label='V_s')
plt.plot(t*1e-3, Vd, '-', label='V_d')
plt.title('Membrane potentials')
plt.xlabel('time [s]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')


f2 = plt.figure(2)
plt.plot(t[1400:2200], Vs[1400:2200], '-', label='V_s')
plt.plot(t[1400:2200], Vd[1400:2200], '-', label='V_d')
plt.title('Membrane potentials')
plt.xlabel('time [ms]')
plt.ylabel('[mV]')
plt.legend(loc='upper right')

plt.show()
