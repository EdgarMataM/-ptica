import numpy as np
import matplotlib.pyplot as plt
import math
"Declaramos variables"
x = 1 #Mantenemos un x fijo
E0 = 1
k1 = 11
k2 = 10.
kg = (k1-k2)/2
kp = (k1+k2)/2
c = 0.1
omega_1 = c*k1
omega_2 = c*k2
omega_g = (omega_1-omega_2)/2
omega_p = (omega_1+omega_2)/2
"Se define un vector de tiempo variable"
t = np.linspace(-100,100,100)
Er = []
E1 = []
E2 = []
for i in t:
    E1.append(E0*math.cos(k1*x-omega_1*i))
    E2.append(E0*math.cos(k2*x-omega_2*i))
    Er.append(2*E0*math.cos(kp*x-omega_p*i)*math.cos(kg*x-omega_g*i))
#for j in range(len(E1)):
#    Er.append(E1[j]+E2[j])

E1 = np.array(E1)
E2 = np.array(E2)
Er = np.array(Er)
plt.grid()
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.xlim(t.min(),t.max())
plt.title('Superposición con velocidad de grupo y fase.')
plt.plot(t,Er)
plt.plot(t,E1,'r')
plt.plot(t,E2,'g')