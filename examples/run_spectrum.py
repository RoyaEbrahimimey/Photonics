import numpy as np
import matplotlib.pyplot as plt
from src.spectrum  import simulate_spectrum


wavelengths=np.linspace(400e-9, 700e-9, 100)
n_substrate=1.5
n_in=1.0
n_layers = np.array([1.45, 2.1, 1.45])
d_layers = np.array([10e-9, 70e-9, 10e-9])
angle_incidence = 0
polarization = "TE"
R_spectrum, T_spectrum = simulate_spectrum(n_layers, d_layers, wavelengths, n_in, n_substrate, angle_incidence, polarization)

plt.plot(wavelengths*1e9, R_spectrum, label='Reflection')
plt.plot(wavelengths*1e9, T_spectrum, label='Transmission')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Power')
# plt.legend()
# plt.grid()
#plt.tight_layout()

plt.show()