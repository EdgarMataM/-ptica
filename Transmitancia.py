# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 18:34:41 2021

@author: Edgar Mata
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

n_aire = 1
n_bk7 = 1.5

n_i = n_aire/n_bk7
n_e = n_bk7/n_aire

theta_i = []
grados = []


snell_i = []
snell_e = []


T_TE_i = []
T_TM_i = []
T_TE_e = []
T_TM_e = []

#Lista para variar ángulo de incidencia.
for i in range(10000):
    theta_i.append((math.pi/2)*i/10000)
    
#Término repetido en coeficientes que surgen de la ley de Snell.
for i in range(10000):
    snell_e.append(math.sqrt(n_e**2-(math.sin(theta_i[i]))**2))
    snell_i.append(cmath.sqrt(n_i**2-(math.sin(theta_i[i]))**2))
    
    
#Obtiene transmitancias.
for i in range(10000):
    T_TE_e.append((4*math.cos(theta_i[i])*snell_e[i])
                  /(math.cos(theta_i[i])+snell_e[i])**2)
    T_TM_e.append(((snell_e[i])/(math.cos(theta_i[i])))*
            ((2*n_e*math.cos(theta_i[i]))/(n_e**2*
            math.cos(theta_i[i])+snell_e[i]))**2)
    
    if n_i**2-(math.sin(theta_i[i]))**2 < 0:
        T_TE_i.append(0)
        T_TM_i.append(0)
    else:
        T_TE_i.append((1/n_i)*((2*snell_i[i])/
                    (math.cos(theta_i[i])+snell_i[i]))**2)
        T_TM_i.append(((snell_i[i])/(math.cos(theta_i[i])))*
                    ((2*n_i*math.cos(theta_i[i]))/(n_i**2*
                    math.cos(theta_i[i])+snell_i[i]))**2)



#Lista para usar grados en lugar de radianes.   
for i in range(10000):
    grados.append(math.degrees(theta_i[i]))
    
    
    
plt.title('Transmitancia interna/externa.')
plt.xlabel('Ángulo de incidencia (grados).',family='serif',size=11)
plt.ylabel('Fracción de transmitancia.',family='serif',size=11)

plt.plot(grados[:],T_TE_e[:],c='#DF01A5',
         label = "Trans. TE Externa.")

plt.plot(grados[:],T_TM_e[:],c='#00BFFF',
         label = "Trans. TM Externa.")
plt.plot(grados[:],T_TE_i[:],c='#04B431',
         label = "Trans. TE Interna.")
plt.plot(grados[:],T_TM_i[:],c='#FF4000',
         label = "Trans. TM Interna.")

plt.xlim(0,90)
plt.ylim(-0.1,1.5)

plt.axvline(x=42.3, ymin=-0.2, ymax=1,linestyle='--')

plt.grid()
plt.legend(loc = "upper left",fontsize = 8.5)
