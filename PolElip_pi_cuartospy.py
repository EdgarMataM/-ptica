import numpy as np
import matplotlib.pyplot as plt

"Se definen amplitudes de E0"
E_0x = 1
E_0y = 5
"Se definen las fases tal que el desfase sea pi/4"
phi_x = np.pi/4
phi_y = 0
"Se define un vector de ángulo variable de 0 a 2 pi"
phi = np.linspace(0 , 2*np.pi)
"Guarda arreglos de las componentes para diferentes ángulos"
E_x = np.real(E_0x*np.exp(1j*(phi_x+phi)))
E_y = np.real(E_0y*np.exp(1j*(phi_y+phi)))

"Grafica la parte física de la onda"
plt.plot(E_x,E_y)
plt.grid(True)
plt.xlabel('$E_{x}$')
plt.ylabel('$E_{y}$')
plt.title('Polarización elíptica.')
plt.show()
