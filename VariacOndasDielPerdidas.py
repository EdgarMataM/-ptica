import matplotlib.pyplot as plt
import numpy as np
"Generamos arreglos para variacion espacial y temporal."
z = np.arange(0,15,0.150)
t=np.arange(start=0, stop=100, step=100)
E = 0.5*np.exp(-0.333*z)*np.cos(1E+8*t-1.374*z)
H = 2.817*np.exp(-0.333*z)*np.cos(1E+8*t-1.374*z-(13.63)*(np.pi/180))
plt.plot(z, E, label='Campo E(z,t)')
plt.plot(z, H, color = '#DF5B4F', label='Campo H(z,t)')
plt.grid()
plt.title('Ondas en dieléctricos con pérdidas.')
plt.xlabel("Distancia z.")
plt.ylabel("Campos.")
plt.ylim(-1.6, 2.8)
plt.xlim(0, 15)
plt.legend()
