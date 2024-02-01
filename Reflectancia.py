# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 21:20:38 2021

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


R_TE_i = []
R_TM_i = []
R_TE_e = []
R_TM_e = []

#Lista para variar ángulo de incidencia.
for i in range(10000):
    theta_i.append((math.pi/2)*i/10000)
    
#Término repetido en coeficientes que surgen de la ley de Snell.
for i in range(10000):
    snell_e.append(math.sqrt(n_e**2-(math.sin(theta_i[i]))**2))
    snell_i.append(cmath.sqrt(n_i**2-(math.sin(theta_i[i]))**2))

#Obtiene reflectancias.
for i in range(10000):
    R_TE_e.append((math.cos(theta_i[i])**2-2*
                   math.cos(theta_i[i])*snell_e[i]+n_e**2-
                   math.sin(theta_i[i])**2)/(math.cos(theta_i[i])**2
                   +2*math.cos(theta_i[i])*snell_e[i]+n_e**2
                   -math.sin(theta_i[i])**2))
    R_TM_e.append((n_e**4*math.cos(theta_i[i])**2
                   -2*n_e**2*math.cos(theta_i[i])*snell_e[i]+
                   n_e**2-math.sin(theta_i[i])**2)/
                  (n_e**4*math.cos(theta_i[i])**2+2*n_e**2
                   *math.cos(theta_i[i])*snell_e[i]+n_e**2-
                   math.sin(theta_i[i])**2))
    if n_i**2-(math.sin(theta_i[i]))**2 < 0:
        R_TE_i.append(0)
        R_TM_i.append(0)
    else:
        R_TE_i.append((math.cos(theta_i[i])**2-2*
            math.cos(theta_i[i])*snell_i[i]+n_i**2-
            math.sin(theta_i[i])**2)/(math.cos(theta_i[i])**2
            +2*math.cos(theta_i[i])*snell_i[i]+n_i**2-
            math.sin(theta_i[i])**2))
        R_TM_i.append((n_i**4*math.cos(theta_i[i])**2-2*n_i**2
        *math.cos(theta_i[i])*snell_i[i]+n_i**2-
        math.sin(theta_i[i])**2)/(n_i**4*math.cos(theta_i[i])**2
        +2*n_i**2*math.cos(theta_i[i])*snell_i[i]+n_i**2-
        math.sin(theta_i[i])**2))
        

#Lista para usar grados en lugar de radianes.   
for i in range(10000):
    grados.append(math.degrees(theta_i[i]))
    

plt.title('Reflectancia interna/externa.')
plt.xlabel('Ángulo de incidencia (grados).',family='serif',size=11)
plt.ylabel('Fracción de reflectancia.',family='serif',size=11)

plt.plot(grados[:],R_TE_e[:],c='#DF01A5',
         label = "Ref. TE Externa.")


plt.plot(grados[:],R_TM_e[:],c='#00BFFF',
         label = "Ref. TM Externa.")
plt.plot(grados[:],R_TE_i[:],c='#04B431',
         label = "Ref. TE Interna.")

plt.plot(grados[:],R_TM_i[:],c='#FF4000',
         label = "Ref. TM Interna.")

plt.xlim(0,90)
plt.ylim(-0.1,1)

plt.axvline(x=42.3, ymin=-0.2, ymax=1,linestyle='--')

plt.grid()
plt.legend(loc = "upper left",fontsize = 8.5)
