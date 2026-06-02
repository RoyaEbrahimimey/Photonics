import numpy as np
import matplotlib.pyplot as plt
from src.tmm import tmm


wavelength = 550e-9
angles = np.linspace(0, 89, 200)

n_substrate = 1.5
n_in = 1.0

n_layers = np.array([1.45, 2.1, 1.45, 2.0])
d_layers = np.array([100e-9, 70e-9, 100e-9, 100e-9])

R_TE = []
R_TM = []

for angle in angles:
    r_te, Rte, t_te, Tte = tmm(
        n_substrate=n_substrate,
        n_layer=n_layers,
        n_in=n_in,
        d_layer=d_layers,
        wavelength=wavelength,
        angle_incidence=angle,
        polarization="TE",
    )

    r_tm, Rtm, t_tm, Ttm = tmm(
        n_substrate=n_substrate,
        n_layer=n_layers,
        n_in=n_in,
        d_layer=d_layers,
        wavelength=wavelength,
        angle_incidence=angle,
        polarization="TM",
    )

    R_TE.append(Rte)
    R_TM.append(Rtm)

plt.plot(angles, R_TE, label="TE")
plt.plot(angles, R_TM, label="TM")
plt.xlabel("Angle of Incidence (degrees)")
plt.ylabel("Reflectance")
plt.legend()
plt.grid()
plt.show()