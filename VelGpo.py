import numpy as np
import matplotlib.pyplot as plt
import math
"Declaramos variables"
x = 1 #Mantenemos un x fijo
E0 = 1
k1 = 10
k2 = 15
kg = (k1-k2)/2
kp = (k1+k2)/2
c = 1
omega_1 = c*k1
omega_2 = c*k2
omega_g = (omega_1-omega_2)/2
omega_p = (omega_1+omega_2)/2
"Se define un vector de tiempo variable"
t = np.linspace(-150,150,150)
Er = []
for i in t:
    Er.append(2*E0*math.cos(kp*x-omega_p*i)*math.cos(kg*x-omega_g*i))
Er = np.array(Er)
plt.grid()
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.xlim(t.min(),t.max())
plt.title('Superposición con velocidad de grupo y fase.')
plt.plot(t,Er)

