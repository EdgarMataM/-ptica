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

#Longitud de onda del rayo ORGIGINAL.
lambd = 632.8*(10**(-9))
sigma = 5.8*10**7
lambd_var = []          #Lista para usar diferentes longitudes de onda.
omega = []              #Lista para guardar frecuencias angulares.
alpha = []              #Lista para variar alpha.
beta = []               #Lista para variar beta.

#Llena la lista con longitudes de onda variables entre 632.8nm +- 100 nm.
for i in range(200):
    if i<=100:
        lambd_var.append(532.8*(10**(-9))+i*(10**(-9)))                
    else:
        lambd_var.append(632.8*(10**(-9))+(i/2)*(10**(-9)))
            

#Índice de refracción del prisma.
index = 1.9648
#Velocidad de la onda en el prisma.
v = 300000000/index

#Obtiene lista frecuencia angular.
for i in range(200):
    omega.append((2*3.1416*v)/lambd_var[i])


for i in range(200):
    alpha.append(omega[i]*math.sqrt((0.5*8.854*10**(-12)*
    0.99999*4*3.1416*10**(-7))*(math.sqrt(1+(sigma**2)/
    (omega[i]*omega[i]*(8.854*10**(-12))**2))-1)))
    beta.append(omega[i]*math.sqrt((0.5*8.854*10**(-12)*0.99999*4*3.1416*10**(-7))*(math.sqrt(1+(sigma**2)/(omega[i]*omega[i]*(8.854*10**(-12))**2))+1)))
    
#Ordena los elementos de las listas.
alpha.sort()
beta.sort()
omega.sort()
    
plt.subplot(1,2,1).title.set_text('alpha')
plt.scatter(omega[:],alpha[:])
plt.xlabel('Frecuencia angular (w)')
plt.ylabel('Constante de atenuación (alpha)')


plt.subplot(1,2,2).title.set_text('beta')
plt.scatter(omega[:],beta[:])
plt.xlabel('Frecuencia angular (w)')
plt.ylabel('Constante de atenuación (alpha)')

"""
https://books.google.com.mx/books?id=8aipFzSCKnkC&pg=PA470&dq=permitividad+dielectrica+cobre&hl=es-419&sa=X&ved=2ahUKEwiWsdeWzPjyAhXERjABHedjCBMQ6AF6BAgLEAI#v=onepage&q=permitividad%20dielectrica%20cobre&f=false
https://books.google.com.mx/books?id=t5GcXfN3LF4C&pg=PA134&dq=permitividad+diel%C3%A9ctrica+cobre&hl=es-419&sa=X&ved=2ahUKEwjG-NW37PnyAhUql2oFHRGpDhc4ChDoAXoECAYQAg#v=onepage&q=permitividad%20diel%C3%A9ctrica%20cobre&f=false
https://rmf.smf.mx/ojs/index.php/rmf/article/view/2539/2507

"""