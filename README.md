# Thin-Film Transfer Matrix Optimizer

A Python-based simulation and optimization tool for optical multilayer thin-film structures using the Transfer Matrix Method (TMM).

This project computes reflection and transmission spectra for arbitrary multilayer stacks and supports oblique incidence with TE and TM polarizations. It also includes thickness optimization using global optimization methods.

## Features

* Transfer Matrix Method for multilayer optical stacks
* Normal and oblique incidence
* TE and TM polarization support
* Wavelength-dependent reflection and transmission spectra
* Thickness optimization using differential evolution
* Angle sweep validation

## Project Structure

```text
photonics/
│
├── src/
│   ├── tmm.py
│   └── spectrum.py
│
├── examples/
│   ├── run_spectrum.py
│   ├── run_optimization.py
│   └── run_angle_sweep.py
│
├── README.md
```

## Example: Thickness Optimization

The optimizer finds layer thicknesses that minimize the average reflectance over the visible wavelength range from 400 nm to 700 nm.

## Validation

The TE/TM implementation was validated by sweeping the angle of incidence. For TM polarization, the reflectance shows a minimum near the Brewster angle, as expected physically.

For an air-to-glass interface:

```text
theta_B = arctan(n_substrate / n_in)
```

For `n_in = 1.0` and `n_substrate = 1.5`, this occurs near 56 degrees.

## Requirements

```text
numpy
matplotlib
scipy
```

## How to Run

From the project root folder:

```bash
python -m examples.run_spectrum
python -m examples.run_optimization
python -m examples.run_angle_sweep
```

## Author

Roya Ebrahimi Meymand
