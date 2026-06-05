# Thin-Film Transfer Matrix Optimizer

A Python-based simulation and optimization tool for optical multilayer thin-film structures using the Transfer Matrix Method (TMM).

This project computes reflection and transmission spectra for arbitrary multilayer stacks and supports oblique incidence with TE and TM polarizations. It also includes thickness optimization using SciPy optimization method and PyGAD for both thicknesses and materials optimization.

## Features

* Transfer Matrix Method for multilayer optical stacks
* Normal and oblique incidence
* TE and TM polarization support
* Wavelength-dependent reflection and transmission spectra
* Thickness optimization using differential evolution
* Material and thickness optimization using PyGAD
* Angle sweep validation

## Project Structure

```text
photonics/ 
│ 
├── src/ 
│    ├── tmm.py 
│    ├── spectrum.py 
│    └── materials.py 
│
├── examples/ 
│    ├── run_spectrum.py 
│    ├── run_optimization.py
│    ├── run_GA_optimization.py
│    └── run_angle_sweep.py
│
├── README.md 
└── requirements.txt
```

## Example: Thickness and Material Optimization

The optimizer searches over both continuous layer thicknesses and discrete material choices. The merit function is defined from the mean-squared error between the simulated transmission spectrum and a target band-pass response, with high transmission desired between 500 nm and 550 nm.

## Validation

The TE/TM implementation was validated by sweeping the angle of incidence. For TM polarization, the reflectance shows a minimum near the Brewster angle, as expected physically.

## Requirements

```text
numpy
matplotlib
scipy
pygad
```

## How to Run

From the project root folder:

```bash
python -m examples.run_spectrum
python -m examples.run_optimization
python -m examples.run_GA_optimization
python -m examples.run_angle_sweep
```

## Author

Roya Ebrahimi Meymand
