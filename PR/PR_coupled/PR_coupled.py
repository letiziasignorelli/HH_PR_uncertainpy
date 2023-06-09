import numpy as np
import uncertainpy as un
import time
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
from math import exp


def soma( g_L = 0.1  ,  # [mS cm**-2]
          g_Na = 30. ,  # [mS cm**-2]
          C_m = 3.,     # membrane capacitance [uF cm**-2]
          E_K = -75. ,  # [mV]
          Vs0 = -68.,
          Vd0 = -68.
        ):
    
    # Fixed parameters
    p = 0.5      # proportion of the membrane area taken up by the soma
    g_c = 10.5     # [mS cm**-2]
        
    E_Na = 60.   # [mV]
    E_Ca = 80.
    E_L = -68.   # [mV]
    g_DR = 15.   # [mS cm**-2]
    g_Ca = 10.   # [mS cm**-2]
    g_AHP = 0.8  # [mS cm**-2]
    g_C = 15.    # [mS cm**-2]
    n0 = 0.001
    h0 = 0.999
    s0 = 0.009
    c0 = 0.007
    q0 = 0.01
    Ca0 = 0.2
    
    # setup time
    start_time = 0
    t_dur = 150     # [ms]
    t_span = (0, t_dur)

    def alpha_m(Vs):
        V1 = Vs + 46.9
        alpha = - 0.32 * V1 / (exp(-V1 / 4.) - 1.)
        return alpha

    def beta_m(Vs):
        V2 = Vs + 19.9
        beta = 0.28 * V2 / (exp(V2 / 5.) - 1.)
        return beta

    def alpha_h(Vs):
        alpha = 0.128 * exp((-43. - Vs) / 18.)
        return alpha

    def beta_h(Vs):
        V5 = Vs + 20.
        beta = 4. / (1 + exp(-V5 / 5.))
        return beta

    def alpha_n(Vs):
        V3 = Vs + 24.9
        alpha = - 0.016 * V3 / (exp(-V3 / 5.) - 1)
        return alpha

    def beta_n(Vs):
        V4 = Vs + 40.
        beta = 0.25 * exp(-V4 / 40.)
        return beta

    def alpha_s(Vd):
        alpha = 1.6 / (1 + exp(-0.072 * (Vd-5.)))
        return alpha

    def beta_s(Vd):
        V6 = Vd + 8.9
        beta = 0.02 * V6 / (exp(V6 / 5.) - 1.)
        return beta

    def alpha_c(Vd):
        V7 = Vd + 53.5
        V8 = Vd + 50.
        if Vd <= -10:
            alpha = 0.0527 * exp(V8/11.- V7/27.)
        else:
            alpha = 2 * exp(-V7 / 27.)
        return alpha

    def beta_c(Vd):
        V7 = Vd + 53.5
        if Vd <= -10:
            beta = 2. * exp(-V7 / 27.) - alpha_c(Vd)
        else:
            beta = 0.
        return beta

    def alpha_q(Ca):
        alpha = min(0.00002*Ca, 0.01)
        return alpha

    def beta_q(Ca):
        return 0.001

    def chi(Ca):
        return min(Ca/250., 1.)

    def m_inf(Vs):
        return alpha_m(Vs) / (alpha_m(Vs) + beta_m(Vs))

    def dVdt(t, V):

        Vs, Vd, n, h, s, c, q, Ca = V

        I_leak_s = g_L*(Vs - E_L)
        I_leak_d = g_L*(Vd - E_L)
        I_Na = g_Na * m_inf(Vs)**2 * h * (Vs - E_Na)
        I_DR = g_DR * n * (Vs - E_K)
        I_ds = g_c * (Vd - Vs)

        I_Ca = g_Ca * s**2 * (Vd - E_Ca)
        I_AHP = g_AHP * q * (Vd - E_K)
        I_C = g_C * c * chi(Ca) * (Vd - E_K)
        I_sd = -I_ds
        if t>stim_start and t<stim_end:
            dVsdt = (1./C_m)*( -I_leak_s - I_Na - I_DR + I_ds/p + I_stim/p )
        else:
            dVsdt = (1./C_m)*( -I_leak_s - I_Na - I_DR + I_ds/p)
        dVddt = (1./C_m)*( -I_leak_d - I_Ca - I_AHP - I_C + I_sd/(1-p) )
        dhdt = alpha_h(Vs)*(1-h) - beta_h(Vs)*h
        dndt = alpha_n(Vs)*(1-n) - beta_n(Vs)*n
        dsdt = alpha_s(Vd)*(1-s) - beta_s(Vd)*s
        dcdt = alpha_c(Vd)*(1-c) - beta_c(Vd)*c
        dqdt = alpha_q(Ca)*(1-q) - beta_q(Ca)*q
        dCadt = -0.13*I_Ca - 0.075*Ca

        return dVsdt, dVddt, dndt, dhdt, dsdt, dcdt, dqdt, dCadt


    V0 = [Vs0, Vd0, n0, h0, s0, c0, q0, Ca0]

    I_stim = 0.78 # [uA cm**-2]
    stim_start = 0 # [ms]
    stim_end = t_dur   # [ms]

    sol = solve_ivp(dVdt, t_span, V0, max_step=0.05)

    Vs, Vd, n, h, s, c, q, Ca = sol.y
    values = Vs
    dendrite = Vd
    time = sol.t

    # Time to start analysis
    time_sa = 40

    # Only return from 'time_sa' milliseconds onwards
    values = values[time > time_sa]
    dendrite = dendrite[time > time_sa]
    time = time[time > time_sa]

    info = {"stimulus_start": time[0], "stimulus_end": time[-1], "dendrite" : dendrite}

    return time, values, info
