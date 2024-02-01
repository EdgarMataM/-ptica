import numpy as np
import matplotlib.pyplot as plt
"Declaramos variables"
I1 = 2
I2 = 2
"Se define un arreglo de angulo variable"
epsilon = np.linspace(-6*np.pi,6*np.pi,250)
IR = []
for i in epsilon:
    IR.append(I1+I2 +2*np.sqrt(I1*I2)*np.cos(i))
plt.grid()
plt.xlabel('Ángulo $\epsilon$.')
plt.ylabel('Irradianza $I$.')
plt.xlim(epsilon.min(),epsilon.max())
plt.title('Variación de irradianza para fuentes incoherentes.')
plt.plot(epsilon,IR)