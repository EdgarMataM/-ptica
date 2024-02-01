# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:33:00 2021

@author: Edgar Mata
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cmath


n_aire = 1
n_bk7 = 1.5

n_i = n_aire/n_bk7

theta_i = []
grados = []

phi_TE = []
phi_TM = []

#Lista para variar ángulo de incidencia.
for i in range(10000):
    theta_i.append((math.pi/2)*i/10000)
    
    
    
#Lista para usar grados en lugar de radianes.   
for i in range(10000):
    grados.append(math.degrees(theta_i[i]))
    
    
for i in range(10000):
    if grados[i] <= 42:
        phi_TE.append(0)
    else:
        if math.sin(theta_i[i])**2-n_i**2< 0:
            phi_TE.append(0)
        else:
            phi_TE.append(-2*math.atan((math.sqrt(math.sin(
                theta_i[i])**2-n_i**2))/(math.cos(theta_i[i]))))
            
for i in range(10000):
    if grados[i] <= 33.7:
        phi_TM.append(0)
    else:
        if grados[i] <= 42:
            phi_TM.append(math.pi)
        else:
            phi_TM.append(math.pi-2*math.atan((math.sqrt(
                math.sin(theta_i[i])**2-n_i**2))/
                (n_i**2*math.cos(theta_i[i]))))


plt.title('Desfase para coef. de reflexión.')
plt.xlabel('Ángulo de incidencia (grados).',family='serif',size=11)
plt.ylabel('Ángulo de desfase (rad).',family='serif',size=11)

plt.plot(grados[:],phi_TE[:],c='#00FF40',
         label = "Desfase para Reflección TE.")
plt.plot(grados[:],phi_TM[:],c='#FE2E64',
         label = "Desfase para Reflección TM.")


plt.axvline(x=42.3, ymin=-0.2, ymax=1,linestyle='--')

plt.grid()
plt.legend(loc = "lower left",fontsize = 8.5)