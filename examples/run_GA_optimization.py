import numpy as np
import matplotlib.pyplot as plt
from src.spectrum  import simulate_spectrum
import pygad
from src.materials import MATERIALS

# pygad is a genetic algorithm (mixed discrete/continuous optimization) library for Python that provides a simple and efficient way to solve optimization problems. It allows you to define your own fitness function, which evaluates the quality of solutions, and then uses genetic operators like selection, crossover, and mutation to evolve a population of candidate solutions over multiple generations. In this example, we will use pygad to optimize both materials and thicknesses of layers in a photonic structure to achieve a desired transmission spectrum.
wavelengths=np.linspace(400e-9, 700e-9, 100)
n_substrate=1.5
n_in=1.0
polarization="TE"
angle_incidence=0
num_layers = 8


material_names = list(MATERIALS.keys())

def objective_function(ga_instance, solution, solution_idx):
    
    d_layers = np.array(solution[:num_layers])
    material_ids = np.array(solution[num_layers:], dtype=int)

    n_layers = np.array([
        MATERIALS[material_names[i]] for i in material_ids
    ])

    target_T = np.zeros_like(wavelengths)
    target_T[(wavelengths >= 500e-9) & (wavelengths <= 550e-9)] = 1
    R_spectrum, T_spectrum = simulate_spectrum(n_layers=n_layers, d_layers=d_layers, wavelengths=wavelengths, n_in=n_in, n_substrate=n_substrate, angle_incidence=angle_incidence, polarization=polarization)
    # To convert the minimization problem into a maximization problem for the genetic algorithm, we can take the inverse of the mean reflection. Adding a small constant (1e-9) prevents division by zero.
    loss = np.mean((T_spectrum - target_T)**2)
    fitness = 1.0 / (loss + 1e-9)

    return fitness



num_generations = 200
num_parents_mating = 4
sol_per_pop = 10
num_genes = 2 * num_layers  # Number of layers to optimize
#gene_space = [{"low": 50e-9, "high": 300e-9}, {"low": 50e-9, "high": 300e-9}, {"low": 50e-9, "high": 300e-9},{"low": 50e-9, "high": 300e-9},]
num_materials = len(MATERIALS)
gene_space = (
    [{"low": 100e-9, "high": 300e-9} for _ in range(num_layers)]
    +
    [list(range(num_materials)) for _ in range(num_layers)]
)
parent_selection_type = "sss"
keep_parents = 2
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 25


ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating, 
                       fitness_func=objective_function,
                       sol_per_pop=sol_per_pop, 
                       num_genes=num_genes,
                       gene_space=gene_space,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
optimized_d = np.array(solution[:num_layers])
material_ids = np.array(solution[num_layers:], dtype=int)
optimized_n_layers = np.array([
        MATERIALS[material_names[i]] for i in material_ids
    ])

R_spectrum, T_spectrum = simulate_spectrum(optimized_n_layers, optimized_d, wavelengths, n_in, n_substrate, angle_incidence, polarization)
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Optimized thicknesses (nm):", optimized_d * 1e9)
print("Optimized refractive indices:", optimized_n_layers)
target_T = np.zeros_like(wavelengths)
target_T[(wavelengths >= 500e-9) & (wavelengths <= 550e-9)] = 1
plt.plot(wavelengths*1e9, R_spectrum, label='Reflection')
plt.plot(wavelengths*1e9, T_spectrum, label='Transmission')
plt.plot(wavelengths * 1e9, target_T, "--", label="Target Transmission")
plt.xlabel('Wavelength (nm)')
plt.ylabel('Power')
plt.legend()


plt.show()

