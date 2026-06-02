import numpy as np
from numpy.linalg import inv


def tmm(n_substrate, n_layer, n_in, d_layer, wavelength, angle_incidence, polarization):
    n_layer = np.array(n_layer, dtype=complex)
    d_layer = np.array(d_layer, dtype=float)

    theta = angle_incidence * np.pi / 180
    k0 = 2 * np.pi / wavelength

    ky = n_in * k0 * np.sin(theta)

    k_in = np.sqrt((n_in * k0)**2 - ky**2)
    k_layer = np.sqrt((n_layer * k0)**2 - ky**2)
    k_substrate = np.sqrt((n_substrate * k0)**2 - ky**2)

    polarization = polarization.upper()
    # print(polarization)
    if polarization == "TE":
        q_in = k_in / k0
        q_layer = k_layer / k0
        q_sub = k_substrate / k0

    elif polarization == "TM":
        q_in = k_in / (k0 * n_in**2)
        q_layer = k_layer / (k0 * n_layer**2)
        q_sub = k_substrate / (k0 * n_substrate**2)

    else:
        raise ValueError("polarization must be 'TE' or 'TM'")

    T = np.eye(2, dtype=complex)

    for i in range(len(n_layer)):
        delta = k_layer[i] * d_layer[i]

        T_main = np.array([
            [np.cos(delta), 1j * np.sin(delta) / q_layer[i]],
            [1j * q_layer[i] * np.sin(delta), np.cos(delta)]
        ], dtype=complex)

        T = T_main @ T

    A = np.array([[1, 1], [-q_in, q_in]], dtype=complex)
    B = np.array([[1, 1], [-q_sub, q_sub]], dtype=complex)

    S = inv(A) @ inv(T) @ B

    r = S[1, 0] / S[0, 0]
    t = 1 / S[0, 0]

    R = abs(r)**2
    T_power = np.real(q_sub / q_in) * abs(t)**2

    return r, R, t, T_power