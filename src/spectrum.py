import numpy as np
from src.tmm import tmm

def simulate_spectrum(n_layers, d_layers, wavelengths, n_in, n_substrate, angle_incidence, polarization):
    #substrate refractive index=1.5
    #incident medium refractive index=1.0 (air)


    R_spectrum = []
    T_spectrum = []

    for w1 in wavelengths:
 
     r, R, t, T_power = tmm(n_substrate=n_substrate,n_layer=n_layers, n_in=n_in,d_layer=d_layers,wavelength=w1,angle_incidence=angle_incidence, polarization=polarization)
     
   
     # T_power = (n_substrate / n_in) * abs(t)**2
     # T = abs(t)**2
     R_spectrum.append(R)
     T_spectrum.append(T_power)


    return R_spectrum, T_spectrum


