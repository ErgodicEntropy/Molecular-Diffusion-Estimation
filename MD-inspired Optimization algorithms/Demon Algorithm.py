#Demon algorithm: a Monte Carlo method (quasi-Ergodic) for efficiently sampling from the microcanonical ensemble NVE with one additional Degree of Freedom called "Demon" (here taken to be the reversed version of Maxwell's demon) that exchanges energy with the system to reach equilibrium without interacting with particles. This demon has an non-negative energy Ed of its own and the point is to reach thermodynamic equilibrium (maximum entropy) while also maintaining constant energy (energy conservation) = Solving the system -> defining the microscopic variables (velocity, positition,kinetic energy...etc) consistent with the macroscopic variables (temperature, heat capacity and pressure...etc). This inverse problem is resulting from reversed multiple realizability of the thermodynamic system; there are a lot of combinations of microscopic variables values that can lead to the same macroscopic variables values.

#the point of the algorithm is to lower the potential energy E in order to reach thermodynamic equilibrium while conserving total energy by storing lost E values in the demon energy Ed. In optimization problems, the potential energy E is the function we want to minimize

#Aside from conserving total energy, Ed Demon's energy plays the role of an exploration catalyzer/tolerance, the greater its value the more incentive/tendency there is to explore the search space

#dE < 0 = exploitation phase. Also, the thing about the Demon algorithm is that the exploitation-exploration trade-off is balanced via a feedback loop via having exploiting a solution adds up to Ed



import numpy as np
import itertools
import functools
import matplotlib.pyplot as plt
import random
import math


def Demon(N, Lmax, Vmax, Mmax, Tmax):
    Ed = 0 #Demon energy (non-negative)
    g = 9.8
    #Initialization of microstates defined by (position,velocity) pair
    x = np.zeros(N)
    v = np.zeros(N)
    m = np.zeros(N)
    dE = np.zeros(N)
    for k in range(N):
        x[k] = random.uniform(0,Lmax)
        v[k] = random.uniform(0,Vmax)
        m[k] = random.uniform(0,Mmax)
    #Shaking; Randomly change the microstate of a randomly chosen particle (physically feasible)
    t = 0
    while t < Tmax:
        p = int(random.uniform(0,N))
        x0 = x[p]
        v0 = v[p]
        xn = x0
        vn = v0
        while xn == x0 or vn == v0:
            xn = random.uniform(0,Lmax)
            vn = random.uniform(0,Vmax)
        dE[p] = m[p]*g*(xn - x0)
        if dE[p] < 0:
            x[p] = xn
            v[p] = vn
            Ed = Ed + np.abs(dE[p])
        elif Ed >= dE[p]:
            x[p] = xn
            v[p] = vn
            Ed = Ed - dE[p]
        t = t + 1

    s = int(np.where(dE == np.min(dE))[0])
    Sol1 = x[s]
    Sol2 = np.min(dE) + m[s]*g*Sol1

    return Sol1, Sol2


print(Demon(20,20,20,20,1000))


