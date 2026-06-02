import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv


# wavelengths=np.linspace(400e-9, 700e-9, 100)
# n_substrate=1.5
# n_in=1.0
# R_spectrum=[]
# T_spectrum=[]


def TMM(n_substrate, n_layer, n_in, d_layer, wavelength, angle_incidence):
   
    k=n_layer*2*np.pi/wavelength
    
    T=np.eye(2)
    for i in range(len(n_layer)):
        n_layer = np.array(n_layer, dtype=complex)
        d_layer = np.array(d_layer, dtype=float)
        T_main=np.array([[np.cos(k[i]*d_layer[i]), 1j*np.sin(k[i]*d_layer[i])/n_layer[i]], [1j*n_layer[i]*np.sin(k[i]*d_layer[i]), np.cos(k[i]*d_layer[i])]])
        T = T_main @ T;
        
    A=np.array([[1,1],[-n_in,n_in]])
    B=np.array([[1,1],[-n_substrate,n_substrate]])
    S=inv(A)@inv(T)@B
    r=S[1,0]/S[0,0]
    t=1/S[0,0]
    return r, t  # Optional



# n_layers = np.array([1.45, 2.1, 1.45])
# d_layers = np.array([100e-9, 70e-9, 100e-9])

for w1 in wavelengths:
 
   r, t = TMM(n_substrate=1.5,n_layer=n_layers, n_in=1.0,d_layer=d_layers,wavelength=w1,angle_incidence=0,)
   R = abs(r)**2
   
   T_power = (n_substrate / n_in) * abs(t)**2
   R_spectrum.append(R)
   T_spectrum.append(T_power)

plt.plot(wavelengths*1e9, R_spectrum, label='Reflection')
plt.plot(wavelengths*1e9, T_spectrum, label='Transmission')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Power')
# plt.legend()
# plt.grid()
#plt.tight_layout()

plt.show()

#print("R =", R)
#print("T =", T_power)
#print("R + T =", R + T_power)