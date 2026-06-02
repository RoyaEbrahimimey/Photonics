import numpy as np
import matplotlib.pyplot as plt
from src.spectrum  import simulate_spectrum
from scipy.optimize import differential_evolution

wavelengths=np.linspace(400e-9, 700e-9, 100)
n_substrate=1.5
n_in=1.0
polarization="TM"
angle_incidence=56
n_layers = np.array([1.45, 2.1, 1.45, 2.0])
initial_d = np.array([100e-9, 70e-9, 100e-9, 100e-9])
bounds = [
    (50e-9, 300e-9),
    (50e-9, 300e-9),
    (50e-9, 300e-9),
    (50e-9, 300e-9)
]
# Increase number of layer by adding more bounds & initial_d for optimization
def objective_function(d_layers, n_layers, wavelengths, n_in, n_substrate, angle_incidence, polarization):
    
    
    R_spectrum, T_spectrum = simulate_spectrum(n_layers, d_layers, wavelengths, n_in, n_substrate, angle_incidence, polarization)
    return np.mean(R_spectrum)  # Minimize reflection at the target wavelength



target= differential_evolution(objective_function, bounds=bounds, args=(n_layers, wavelengths, n_in, n_substrate, angle_incidence, polarization))
print(target)
optimized_d = target.x
R_spectrum, T_spectrum = simulate_spectrum(n_layers, optimized_d, wavelengths, n_in, n_substrate, angle_incidence, polarization)

plt.plot(wavelengths*1e9, R_spectrum, label='Reflection')
plt.plot(wavelengths*1e9, T_spectrum, label='Transmission')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Power')
plt.legend()


plt.show()