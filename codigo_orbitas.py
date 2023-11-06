# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 09:44:10 2023

@author: santiago
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

G=1
M1=1
M2=10
x1=1
x2=(M1*x1)/M2
w=np.sqrt((M1+M2)*G/(x1+x2)**3)

x0=-0.29344173582112392474269213106493#posición
y0=0#posición
z0=0#velocidadx
u0=5#velocidady

tf=10#tiempo final
n=100000#numero de intervalos
h=tf/n

X=[x0]
Y=[y0]
Z=[z0]
U=[u0]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x0,y0,'gd',MarkerSize=5)

def dx(x,y,z,u):
    return z  
def dy(x,y,z,u):
    return u
def dz(x,y,z,u):
    return x*w**(2)-(((x+x1)*G*M1)/((x+x1)**(2)+y**(2))**(3/2))-(((x-x2)*G*M2)/((x-x2)**(2)+y**(2))**(3/2))-2*w*u
def du(x,y,z,u):
    return y*w**(2)-(((y)*G*M1)/((x+x1)**(2)+y**(2))**(3/2))-(((y)*G*M2)/((x-x2)**(2)+y**(2))**(3/2))+2*w*z

for i in range(0,n):
    k1=dx(x0,y0,z0,u0)
    L1=dy(x0,y0,z0,u0)
    m1=dz(x0,y0,z0,u0)
    n1=du(x0,y0,z0,u0)
    k2=dx(x0+(3*h*k1/4),y0+(3*h*L1/4),z0+(3*h*m1/4),u0+(3*h*m1/4))
    L2=dy(x0+(3*h*k1/4),y0+(3*h*L1/4),z0+(3*h*m1/4),u0+(3*h*m1/4))
    m2=dz(x0+(3*h*k1/4),y0+(3*h*L1/4),z0+(3*h*m1/4),u0+(3*h*m1/4))
    n2=du(x0+(3*h*k1/4),y0+(3*h*L1/4),z0+(3*h*m1/4),u0+(3*h*m1/4))
    xi=x0+((1/3)*k1+(2/3)*k2)*h
    yi=y0+((1/3)*L1+(2/3)*L2)*h
    zi=z0+((1/3)*m1+(2/3)*m2)*h
    ui=u0+((1/3)*n1+(2/3)*n2)*h
    X.append(xi)
    Y.append(yi)
    Z.append(zi)
    U.append(ui)
    x0=xi
    y0=yi
    z0=zi
    u0=ui

min_limit = min(min(X), min(Y), min(Z))
max_limit = max(max(X), max(Y), max(Z))
ax.set_xlim(min_limit, max_limit)
ax.set_ylim(min_limit, max_limit)
ax.set_zlim(min_limit, max_limit)

ax.plot(X,Y,'k')
ax.plot(-x1,0,'bo',MarkerSize=np.sqrt(M1)*8)
ax.plot(x2,0,'ro',MarkerSize=np.sqrt(M2)*8)
ax.plot(x0,y0,'gd',MarkerSize=5)
plt.show()