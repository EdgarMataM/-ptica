import matplotlib.pyplot as plt
import numpy as np
"Valores del medio y la onda."
mu_0=1.26E-06; mu_r=1
mu=mu_r*mu_0
eps_0=8.85E-012; eps_r=50
eps=eps_r*eps_0
long_onda=1.75
beta=2*np.pi/long_onda
omega= beta/np.sqrt(mu*eps)
E0=20*np.pi
H0=np.sqrt(eps/mu)*E0
z = np.arange (0,100,0.5)
t=np.arange(0,100,0.5)
E = E0*np.cos(omega*t-beta*z)
H = H0*np.cos(omega*t-beta*z)
plt.plot(z, E, label='Campo E(z,t)')
plt.plot(z, H, color = '#DF5B4F', label='Campo H(z,t)')
plt.xlabel("Distancia z.")
plt.ylabel("Campos.")
plt.xlim(z.min(),z.max())
plt.title('Ondas en dieléctricos sin pérdidas.')
plt.grid()
plt.legend(loc ='lower right')