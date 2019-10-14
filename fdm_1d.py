#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:22:13 2019
-Delta_u=sinx
u(0)=0,u(2*pi)=0
@author: jun
"""

import numpy as np
from numpy.linalg import solve
def fdm_1d(a,b,N):
    h=(b-a)/N
    x=np.linspace(a,b,N+1)
    A=np.zeros(shape=(N+1,N+1))
    A[0,0] = 1
    A[N,N] = 1
    for i in range(1,N):
        A[i,i]=2/(h**2)
        A[i+1,i]= -1/(h**2)
        A[i,i+1]= -1/(h**2)
    F=np.zeros(shape=(N+1,1))
    F[0,0]=0
    F[N,0]=0
    for i in range(N+1):
        F[i]=np.sin(x[i])
    U_h=solve(A,F)
    return U_h
# In[]:test
a = 0
b =2*np.pi
N = 100
x =  np.linspace(a,b,N+1)
uh = fdm_1d(a,b,N)
true_solution = np.sin(x)
import matplotlib.pyplot as plt
plt.plot(x,uh,'r',x,true_solution,'b')
