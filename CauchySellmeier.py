# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 19:50:06 2021

@author: Edgar Mata
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def cauchy(a,b):
    n = []
    lamda = []
    l_final = 1500*10**(-6)
    
    for i in range(1000):
        lamda.append((l_final/1000)*(i+1))
    
    for i in range(1000):
        n.append(a+b/(lamda[i]**2))
        
    return n
    
    
def sellmeier(b1,b2,b3,c1,c2,c3):
    n = []
    lamda = []
    l_final = 2000*10**(-6)

    for i in range(1000):
        lamda.append((l_final/1000)*(i+1))
    lamda_a = np.array(lamda)

    for i in range(1000):
        if (1+(b1*lamda_a[i]**2)/(lamda_a[i]**2-c1)+
            (b2*lamda_a[i]**2)/(lamda_a[i]**2-c2)+
            (b3*lamda_a[i]**2)/(lamda_a[i]**2-c3)) < 0:
            n.append(0)
        else:
            n.append(math.sqrt(1+(b1*lamda_a[i]**2)/
            (lamda_a[i]**2-c1)+(b2*lamda_a[i]**2)/
            (lamda_a[i]**2-c2)+(b3*lamda_a[i]**2)/
            (lamda_a[i]**2-c3)))

    return n


#Crea listas para ec. de Cauchy.
bk7_C = []
pmma_C = []
su8_C = []
fuse_C = []

#Crea listas para ec. de Sellmeier.
bk7_S = []
pmma_S = []
su8_S = []
fused_S = []

#Constantes para Cauchy.
A_bk7 = 1.5046
B_bk7 = 0.0042*10**-6
C_bk7 = 0

A_pmma = 1.479
B_pmma = 5.48*10**(-3)*10**-6
C_pmma = -1.72*10**(-4)

A_su8 = 1.5525
B_su8 = 0.0629*10**-6
C_su8 = 0.00014

A_fused = 1.4492
B_fused = 0.00312*10**-6
C_fused = 0


#Constantes para Sellmeier.
B1_bk7 = 1.0396
B2_bk7 = 0.23179
B3_bk7 = 1.01046
C1_bk7 = 0.0060006*10**-6
C2_bk7 = 0.020017*10**-6
C3_bk7 = 103.560*10**-6

"""
B1_bk7 = 1.03961212
B2_bk7 = 0.231792344
B3_bk7 = 1.01046945
C1_bk7 = 0.00600069867*10**-6
C2_bk7 = 0.0200179144*10**-6
C3_bk7 = 103.560653*10**-6
"""

B1_pmma = 1.179
B2_pmma = 2.56*10**-3
B3_pmma = 3.67*10**-2
C1_pmma = 1.02*10**-2*10**-6
C2_pmma = 5.42*10**-2*10**-6
C3_pmma = 14.528*10**-2*10**-6


B1_su8 = 1.4031
B2_su8 = 0.23176
B3_su8 = 0.93905
C1_su8 = 0.01058*10**-6
C2_su8 = 0.049323*10**-6
C3_su8 = 112.406*10**-6


B1_fused = 0.6961663
B2_fused = 0.4079426
B3_fused = 0.8974794
C1_fused = 0.00467914826*10**-6
C2_fused = 0.0135120631*10**-6
C3_fused = 97.9340025*10**-6




#Lista para longitud de onda.
l_onda = []
l_ondaA = []
l_final = 1.500*10**(-6)
l_finalA = 1*10**(-9)


#Long. de onda variable (micrometros).
for i in range(1000):
    l_onda.append((l_final/1000)*(i+1))
    
for i in range(1000):
    l_ondaA.append((l_finalA/1000)*(i+1))
    
    

"""
Dispersión para Cauchy.
"""
bk7_C = cauchy(A_bk7,B_bk7)
pmma_C = cauchy(A_pmma,B_pmma)
su8_C = cauchy(A_su8,B_su8)
fused_C = cauchy(A_fused,B_fused)

"""
Dispersión para Sellmeier.
"""

bk7_S = sellmeier(B1_bk7,B2_bk7,B3_bk7,C1_bk7,C2_bk7,C3_bk7)
pmma_S = sellmeier(B1_pmma,B2_pmma,B3_pmma,C1_pmma,C2_pmma,C3_pmma)
su8_S = sellmeier(B1_su8,B2_su8,B3_su8,C1_su8,C2_su8,C3_su8)
fused_S = sellmeier(B1_fused,B2_fused,B3_fused,C1_fused,C2_fused,
                    C3_fused)

#GRÁFICAS.
plt.title('Dispersión para BK7.')
plt.plot(l_onda[:],bk7_C[:],c='#FF0080',label = "Cauchy.")
plt.plot(l_onda[:],bk7_S[:],c='#00FFFF',label = "Sellmeier.")
plt.xlabel('Longitud de onda.',family='serif',size=11)
plt.ylabel('Índice de refracción.',family='serif',size=11)
plt.xlim(0.2*10**-6,1.5*10**-6)
plt.ylim(1.5,1.6)
plt.legend(loc = "upper right")
plt.show()


plt.title('Dispersión para PMMA.')
plt.plot(l_onda[:],pmma_C[:],c='#FF0080',label = "Cauchy.")
plt.plot(l_onda[:],pmma_S[:],c='#00FFFF',label = "Sellmeier.")
plt.xlabel('Longitud de onda.',family='serif',size=11)
plt.ylabel('Índice de refracción.',family='serif',size=11)
plt.xlim(0.3*10**-6,1.5*10**-6)
plt.ylim(1,2)
plt.legend(loc = "upper right")
plt.show()


plt.title('Dispersión para SU-8/SF2.')
plt.plot(l_onda[:],su8_C[:],c='#FF0080',label = "Cauchy SU-8.")
plt.plot(l_onda[:],su8_S[:],c='#00FFFF',label = "Sellmeier SF2.")
plt.xlabel('Longitud de onda.',family='serif',size=11)
plt.ylabel('Índice de refracción.',family='serif',size=11)
plt.xlim(0.2*10**-6,1.5*10**-6)
plt.ylim(1,2)
plt.legend(loc = "upper right")
plt.show()


plt.title('Dispersión para Sílica Fundida.')
plt.plot(l_onda[:],fused_C[:],c='#FF0080',label = "Cauchy.")
plt.plot(l_onda[:],fused_S[:],c='#00FFFF',label = "Sellmeier.")
plt.xlabel('Longitud de onda.',family='serif',size=11)
plt.ylabel('Índice de refracción.',family='serif',size=11)
plt.xlim(0.2*10**-6,1.5*10**-6)
plt.ylim(1,2)
plt.legend(loc = "upper right")
plt.show()

