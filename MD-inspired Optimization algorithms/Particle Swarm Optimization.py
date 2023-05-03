#Particle Swarm Opt in 1D = minimization problem
from matplotlib import pyplot as plt
import numpy as np
import random
import math
from scipy.stats import maxwell

mean, var, skew, kurt = maxwell.stats(moments='mvsk')

def PSO(f,x0,xf,N,w,c,s,delta,max_iter):
    X = np.zeros((max_iter,N)) #Positions
    V = np.zeros((max_iter,N)) #Velocities
    P = np.zeros((max_iter,N)) #Personal best
    G = np.zeros(max_iter) #Global best
    V[0]= np.linspace(maxwell.ppf(0.01),maxwell.ppf(0.99),N)
    for j in range(max_iter):
        G[j] = random.uniform(x0,xf)
    vmax = delta*(xf-x0) #Mean Free Path
    for k in range(N): #initialization step
        X[0][k]=random.uniform(x0,xf) #principle of maximum entropy
        #V[0][k]=random.normalvariate(0,1) #Maxwell-Boltzmann dist can do too
        P[0][k]=X[0][k]
        if f(P[0][k]) < f(G[0]):
            G[0] = P[0][k]
    for j in range(max_iter-1): #Implementation
        for k in range(N):
            r1 = random.uniform(0,1) #Psychological factors affected by mood(random)
            r2 = random.uniform(0,1) #Psychosocial factors affected by mood(random)
            if V[j][k] <= vmax:
                V[j+1][k] = w*V[j][k]+c*r1*(P[j][k]-X[j][k])+s*r2*(G[j]-X[j][k])
                X[j+1][k]= X[j][k] + V[j+1][k]
            else:
                V[j][k] = vmax
                X[j+1][k]= X[j][k] + vmax
            if f(P[j+1][k]) < f(X[j+1][k]):
                P[j+1][k]=P[j][k]
            else:
                P[j+1][k]=X[j+1][k]
            if f(P[j+1][k]) < f(G[j+1]):
                G[j+1]=P[j+1][k]

    return f(G[max_iter-1])




def quad(x):
    return x**2

print(PSO(quad,-100,100,1000,2,3,3,5,100))







