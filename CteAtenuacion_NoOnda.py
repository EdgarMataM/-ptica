# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:09:38 2021

@author: Edgar Mata
"""

"""
Mata Mendoza Edgar Eduardo. Programa para graficar alpha y beta.
"""

#Se importan librerías.
import matplotlib.pyplot as plt
import math
import numpy as np


lambd = 632.8*(10**(-9))    #Longitud de onda del rayo ORIGINAL.
sigma = 5.8*10**7           #Conductividad del cobre.
omega = []                  #Lista para guardar frecuencias angulares.
alpha = []                  #Lista para variar alpha.
beta = []                   #Lista para variar beta.

      

#Índice de refracción del prisma.
index = 1.9648
#Velocidad de la onda luego de pasar por el prisma.
v = 300000000/index

"""
Obtiene lista frecuencia angular con la long. de onda y
la velocidad tras atravesar el prisma.
 
"""
omega_or = (2*3.1416*v)/lambd

#Obtiene un rango para variar la frecuencia angular.
for i in range(150):
        omega.append(((i+1)*omega_or)/100)
    

#Obtiene listas de valores para alpha y beta.
for i in range(150):
    alpha.append(omega[i]*math.sqrt((0.5*8.854*10**(-12)*
    0.99999*4*3.1416*10**(-7))*(math.sqrt(1+(sigma**2)/
    (omega[i]*omega[i]*(8.854*10**(-12))**2))-1)))
                                                        
    beta.append(omega[i]*math.sqrt((0.5*8.854*10**(-12)*
    0.99999*4*3.1416*10**(-7))*(math.sqrt(1+(sigma**2)/
    (omega[i]*omega[i]*(8.854*10**(-12))**2))+1)))
    

#Ordena los elementos de las listas para graficar.
alpha.sort()
beta.sort()
omega.sort()
    

#Grafica la constante de atenuación.
plt.title('Constante de atenuación.')
plt.grid()
plt.plot(omega[:],alpha[:],c='#01DFA5')
plt.xlabel('Frecuencia angular (1/s)',family='serif',size=11)
plt.ylabel('Constante de atenuación (1/m)',family='serif',size=11)
plt.show()



#Grafica el número de onda.
plt.title('Número de onda.',)
plt.grid()
plt.plot(omega[:],beta[:],c='#BE81F7')
plt.xlabel('Frecuencia angular (1/s)',family='serif',size=11)
plt.ylabel('Número de onda (1/m)',family='serif',size=11)
plt.show()


